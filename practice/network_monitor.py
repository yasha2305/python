
import csv
import queue
import re
import socket
import threading
import time
import tkinter as tk

from collections import defaultdict
from datetime import datetime
from tkinter import ttk, messagebox, filedialog


APP_NAME = "NetWatch | Network Monitor"
CHECK_INTERVAL = 10
CONNECTION_TIMEOUT = 3

DEFAULT_HOSTS = [
    "google.com",
    "github.com",
    "python.org",
]

BG = "#f1f5f9"
DARK = "#172554"
BLUE = "#2563eb"
GREEN = "#15803d"
RED = "#dc2626"
ORANGE = "#c2410c"


def validate_hostname(host):
    """Accept a hostname or IPv4 address, not a URL or arbitrary input."""
    host = host.strip().lower()

    if not host or len(host) > 253:
        return False

    if "://" in host or "/" in host or ":" in host:
        return False

    if host.startswith(".") or host.endswith("."):
        return False

    if not re.fullmatch(r"[a-z0-9.-]+", host):
        return False

    labels = host.split(".")

    for label in labels:
        if (
            not label
            or len(label) > 63
            or label.startswith("-")
            or label.endswith("-")
        ):
            return False

    return True


def check_host(host):
    """
    Check TCP connectivity to port 443.
    This measures connection establishment, not full HTTPS health.
    """
    started = time.perf_counter()

    try:
        with socket.create_connection(
            (host, 443), timeout=CONNECTION_TIMEOUT
        ):
            latency_ms = (time.perf_counter() - started) * 1000

        return {
            "host": host,
            "status": "ONLINE",
            "latency": latency_ms,
            "error": "",
            "timestamp": datetime.now().astimezone().isoformat(
                timespec="seconds"
            ),
        }

    except (OSError, TimeoutError) as error:
        return {
            "host": host,
            "status": "OFFLINE",
            "latency": None,
            "error": str(error)[:180],
            "timestamp": datetime.now().astimezone().isoformat(
                timespec="seconds"
            ),
        }


class NetworkMonitor:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_NAME)
        self.root.geometry("1100x720")
        self.root.minsize(850, 570)
        self.root.configure(bg=BG)

        self.events = queue.Queue()
        self.stop_event = threading.Event()
        self.worker = None

        self.hosts = list(DEFAULT_HOSTS)
        self.results = {}
        self.history = []
        self.transitions = defaultdict(int)
        self.previous_status = {}
        self.lock = threading.Lock()
        self.running = False

        self.build_ui()
        self.refresh_table()
        self.root.after(150, self.process_events)
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    # ---------------- UI ----------------

    def build_ui(self):
        header = tk.Frame(self.root, bg=DARK, padx=22, pady=18)
        header.pack(fill="x")

        tk.Label(
            header,
            text="NETWATCH",
            font=("Segoe UI", 23, "bold"),
            bg=DARK, fg="white"
        ).pack(anchor="w")

        tk.Label(
            header,
            text="Network Connectivity and Availability Monitor",
            font=("Segoe UI", 10),
            bg=DARK, fg="#cbd5e1"
        ).pack(anchor="w", pady=(4, 0))

        cards = tk.Frame(self.root, bg=BG)
        cards.pack(fill="x", padx=14, pady=12)

        self.host_count = self.make_card(
            cards, "MONITORED HOSTS", "0", BLUE
        )
        self.online_count = self.make_card(
            cards, "ONLINE", "0", GREEN
        )
        self.offline_count = self.make_card(
            cards, "OFFLINE", "0", RED
        )
        self.average_latency = self.make_card(
            cards, "AVG LATENCY", "N/A", ORANGE
        )

        controls = tk.Frame(self.root, bg=BG, padx=18, pady=5)
        controls.pack(fill="x")

        tk.Label(
            controls, text="Hostname:",
            bg=BG, fg=DARK,
            font=("Segoe UI", 10, "bold")
        ).pack(side="left")

        self.host_var = tk.StringVar()

        tk.Entry(
            controls, textvariable=self.host_var,
            width=24, font=("Segoe UI", 10)
        ).pack(side="left", padx=8)

        tk.Button(
            controls, text="Add Host",
            command=self.add_host,
            bg=BLUE, fg="white", relief="flat",
            padx=12, pady=7
        ).pack(side="left", padx=3)

        self.start_button = tk.Button(
            controls, text="Start Monitoring",
            command=self.start_monitoring,
            bg=GREEN, fg="white", relief="flat",
            padx=12, pady=7
        )
        self.start_button.pack(side="left", padx=3)

        self.stop_button = tk.Button(
            controls, text="Stop",
            command=self.stop_monitoring,
            bg=RED, fg="white", relief="flat",
            padx=12, pady=7, state="disabled"
        )
        self.stop_button.pack(side="left", padx=3)

        self.remove_button = tk.Button(
            controls, text="Remove Selected",
            command=self.remove_host,
            bg="#e2e8f0", fg=DARK, relief="flat",
            padx=12, pady=7
        )
        self.remove_button.pack(side="left", padx=3)

        tabs = ttk.Notebook(self.root)
        tabs.pack(fill="both", expand=True, padx=18, pady=10)

        self.status_tab = tk.Frame(tabs, bg=BG)
        self.history_tab = tk.Frame(tabs, bg=BG)

        tabs.add(self.status_tab, text="Live Status")
        tabs.add(self.history_tab, text="Event History")

        self.build_status_table()
        self.build_history_table()

        footer = tk.Frame(self.root, bg=BG, padx=18, pady=8)
        footer.pack(fill="x")

        self.status_message = tk.StringVar(
            value="Ready. Start monitoring to check hosts."
        )

        tk.Label(
            footer, textvariable=self.status_message,
            bg=BG, fg="#475569", anchor="w"
        ).pack(side="left", fill="x", expand=True)

        tk.Button(
            footer, text="Export CSV",
            command=self.export_csv,
            bg=BLUE, fg="white", relief="flat",
            padx=12, pady=7
        ).pack(side="right")

    def make_card(self, parent, title, value, color):
        frame = tk.Frame(parent, bg="white", padx=14, pady=12)
        frame.pack(side="left", fill="x", expand=True, padx=5)

        tk.Label(
            frame, text=title,
            bg="white", fg="#64748b",
            font=("Segoe UI", 9, "bold")
        ).pack(anchor="w")

        number = tk.Label(
            frame, text=value,
            bg="white", fg=color,
            font=("Segoe UI", 19, "bold")
        )
        number.pack(anchor="w", pady=(5, 0))
        return number

    def build_status_table(self):
        container = tk.Frame(self.status_tab, bg="white")
        container.pack(fill="both", expand=True, padx=10, pady=10)

        columns = (
            "host", "status", "latency",
            "last_check", "checks", "changes"
        )

        self.status_table = ttk.Treeview(
            container, columns=columns,
            show="headings", selectmode="browse"
        )

        labels = {
            "host": "Hostname",
            "status": "Status",
            "latency": "Latency",
            "last_check": "Last Checked",
            "checks": "Checks",
            "changes": "Status Changes",
        }

        widths = {
            "host": 180,
            "status": 100,
            "latency": 100,
            "last_check": 190,
            "checks": 90,
            "changes": 120,
        }

        for col in columns:
            self.status_table.heading(col, text=labels[col])
            self.status_table.column(
                col, width=widths[col], anchor="center"
            )

        self.status_table.tag_configure(
            "ONLINE", foreground=GREEN
        )
        self.status_table.tag_configure(
            "OFFLINE", foreground=RED
        )

        scroll = ttk.Scrollbar(
            container, orient="vertical",
            command=self.status_table.yview
        )
        self.status_table.configure(yscrollcommand=scroll.set)

        self.status_table.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

    def build_history_table(self):
        container = tk.Frame(self.history_tab, bg="white")
        container.pack(fill="both", expand=True, padx=10, pady=10)

        columns = ("time", "host", "status", "latency", "details")

        self.history_table = ttk.Treeview(
            container, columns=columns, show="headings"
        )

        labels = {
            "time": "Timestamp",
            "host": "Hostname",
            "status": "Status",
            "latency": "Latency",
            "details": "Details",
        }

        widths = {
            "time": 190,
            "host": 150,
            "status": 100,
            "latency": 100,
            "details": 400,
        }

        for col in columns:
            self.history_table.heading(col, text=labels[col])
            self.history_table.column(
                col, width=widths[col], anchor="w"
            )

        self.history_table.tag_configure(
            "ONLINE", foreground=GREEN
        )
        self.history_table.tag_configure(
            "OFFLINE", foreground=RED
        )

        scroll = ttk.Scrollbar(
            container, orient="vertical",
            command=self.history_table.yview
        )
        self.history_table.configure(yscrollcommand=scroll.set)

        self.history_table.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

    # ---------------- HOST MANAGEMENT ----------------

    def add_host(self):
        host = self.host_var.get().strip().lower()

        if not validate_hostname(host):
            messagebox.showerror(
                "Invalid Hostname",
                "Enter a hostname such as example.com, without https:// "
                "or a path."
            )
            return

        if host in self.hosts:
            messagebox.showinfo(
                "Already Added", f"{host} is already being monitored."
            )
            return

        self.hosts.append(host)
        self.host_var.set("")
        self.refresh_table()
        self.update_cards()

        self.status_message.set(f"Added {host}")

    def remove_host(self):
        selection = self.status_table.selection()

        if not selection:
            messagebox.showwarning(
                "Select Host", "Select a host in Live Status first."
            )
            return

        values = self.status_table.item(
            selection[0], "values"
        )
        host = values[0]

        if not messagebox.askyesno(
            "Remove Host", f"Stop tracking {host}?"
        ):
            return

        self.hosts = [item for item in self.hosts if item != host]
        self.results.pop(host, None)
        self.previous_status.pop(host, None)
        self.transitions.pop(host, None)

        self.refresh_table()
        self.update_cards()
        self.status_message.set(f"Removed {host}")

    # ---------------- MONITORING ENGINE ----------------

    def start_monitoring(self):
        if self.running:
            return

        if not self.hosts:
            messagebox.showwarning(
                "No Hosts", "Add at least one hostname first."
            )
            return

        self.running = True
        self.stop_event.clear()

        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.status_message.set("Monitoring started.")

        self.worker = threading.Thread(
            target=self.monitor_worker,
            daemon=True
        )
        self.worker.start()

    def stop_monitoring(self):
        if not self.running:
            return

        self.running = False
        self.stop_event.set()

        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.status_message.set("Stopping monitoring...")

    def monitor_worker(self):
        while not self.stop_event.is_set():
            with self.lock:
                hosts = list(self.hosts)

            for host in hosts:
                if self.stop_event.is_set():
                    break

                result = check_host(host)
                self.events.put(("result", result))

            # Wait interruptibly instead of freezing the GUI.
            self.stop_event.wait(CHECK_INTERVAL)

        self.events.put(("stopped", None))

    def process_events(self):
        try:
            while True:
                event, payload = self.events.get_nowait()

                if event == "result":
                    self.handle_result(payload)

                elif event == "stopped":
                    self.running = False
                    self.start_button.config(state="normal")
                    self.stop_button.config(state="disabled")
                    self.status_message.set("Monitoring stopped.")

        except queue.Empty:
            pass

        if self.root.winfo_exists():
            self.root.after(150, self.process_events)

    def handle_result(self, result):
        host = result["host"]
        old = self.previous_status.get(host)
        new = result["status"]

        self.results[host] = result

        if old is not None and old != new:
            self.transitions[host] += 1

            details = (
                f"Status changed from {old} to {new}"
            )
        elif old is None:
            details = "Initial connectivity check"
        elif new == "OFFLINE":
            details = result["error"]
        else:
            details = "Connection successful"

        self.previous_status[host] = new

        record = {
            **result,
            "details": details,
            "latency_text": (
                f"{result['latency']:.2f} ms"
                if result["latency"] is not None else "N/A"
            ),
        }

        self.history.append(record)

        self.history_table.insert(
            "", 0,
            values=(
                result["timestamp"],
                host,
                new,
                record["latency_text"],
                details
            ),
            tags=(new,)
        )

        # Keep the visible history bounded for long-running sessions.
        children = self.history_table.get_children()
        if len(children) > 1000:
            self.history_table.delete(children[-1])

        self.refresh_table()
        self.update_cards()

        self.status_message.set(
            f"{host}: {new} | {record['latency_text']} | "
            f"Checked at {result['timestamp']}"
        )

    # ---------------- DASHBOARD UPDATES ----------------

    def refresh_table(self):
        if not hasattr(self, "status_table"):
            return

        self.status_table.delete(*self.status_table.get_children())

        for host in self.hosts:
            result = self.results.get(host, {})

            status = result.get("status", "WAITING")
            latency = result.get("latency")
            latency_text = (
                f"{latency:.2f} ms"
                if latency is not None else "N/A"
            )

            timestamp = result.get("timestamp", "Not checked")

            checks = sum(
                1 for record in self.history
                if record["host"] == host
            )

            self.status_table.insert(
                "", "end",
                values=(
                    host,
                    status,
                    latency_text,
                    timestamp,
                    checks,
                    self.transitions[host]
                ),
                tags=(status,) if status in ("ONLINE", "OFFLINE") else ()
            )

    def update_cards(self):
        online = sum(
            1 for host in self.hosts
            if self.results.get(host, {}).get("status") == "ONLINE"
        )

        offline = sum(
            1 for host in self.hosts
            if self.results.get(host, {}).get("status") == "OFFLINE"
        )

        latencies = [
            self.results[host]["latency"]
            for host in self.hosts
            if host in self.results
            and self.results[host]["status"] == "ONLINE"
            and self.results[host]["latency"] is not None
        ]

        average = (
            f"{sum(latencies) / len(latencies):.2f} ms"
            if latencies else "N/A"
        )

        self.host_count.config(text=str(len(self.hosts)))
        self.online_count.config(text=str(online))
        self.offline_count.config(text=str(offline))
        self.average_latency.config(text=average)

    # ---------------- EXPORT ----------------

    def export_csv(self):
        if not self.history:
            messagebox.showinfo(
                "No Data", "Run monitoring before exporting history."
            )
            return

        path = filedialog.asksaveasfilename(
            title="Export Network History",
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            initialfile="network_history.csv"
        )

        if not path:
            return

        try:
            with open(
                path, "w", newline="", encoding="utf-8-sig"
            ) as file:
                writer = csv.writer(file)

                writer.writerow([
                    "Timestamp", "Hostname", "Status",
                    "Latency (ms)", "Error", "Details"
                ])

                for record in self.history:
                    writer.writerow([
                        record["timestamp"],
                        record["host"],
                        record["status"],
                        (
                            f"{record['latency']:.2f}"
                            if record["latency"] is not None else ""
                        ),
                        record["error"],
                        record["details"],
                    ])

            messagebox.showinfo(
                "Export Complete", f"History saved to:\n{path}"
            )

        except OSError as error:
            messagebox.showerror("Export Error", str(error))

    def close(self):
        self.stop_event.set()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkMonitor(root)
    root.mainloop()
