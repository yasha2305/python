import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

root = tk.Tk()
root.title("Python IDE")
root.geometry("900x600")

current_file = None

# New File
def new_file():
    global current_file
    editor.delete("1.0", tk.END)
    current_file = None

# Open File
def open_file():
    global current_file

    file = filedialog.askopenfilename(
        filetypes=[("Python Files", "*.py")]
    )

    if file:
        current_file = file

        with open(file, "r", encoding="utf-8") as f:
            editor.delete("1.0", tk.END)
            editor.insert(tk.END, f.read())

# Save File
def save_file():
    global current_file

    if current_file is None:

        current_file = filedialog.asksaveasfilename(
            defaultextension=".py",
            filetypes=[("Python Files", "*.py")]
        )

    if current_file:

        with open(
            current_file,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(
                editor.get(
                    "1.0",
                    tk.END
                )
            )

# Run Code
def run_code():

    save_file()

    try:
        result = subprocess.run(
            ["python", current_file],
            capture_output=True,
            text=True
        )

        output.delete("1.0", tk.END)

        output.insert(
            tk.END,
            result.stdout
        )

        output.insert(
            tk.END,
            result.stderr
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )

# Menu
menu = tk.Menu(root)

file_menu = tk.Menu(
    menu,
    tearoff=0
)

file_menu.add_command(
    label="New",
    command=new_file
)

file_menu.add_command(
    label="Open",
    command=open_file
)

file_menu.add_command(
    label="Save",
    command=save_file
)

menu.add_cascade(
    label="File",
    menu=file_menu
)

menu.add_command(
    label="Run",
    command=run_code
)

root.config(menu=menu)

# Editor
editor = tk.Text(
    root,
    font=("Consolas", 12)
)

editor.pack(
    fill="both",
    expand=True
)

# Output Window
output = tk.Text(
    root,
    height=10,
    bg="black",
    fg="white"
)

output.pack(fill="x")

root.mainloop()