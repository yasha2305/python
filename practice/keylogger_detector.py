import psutil
import time

# Suspicious keywords
SUSPICIOUS_NAMES = [
    "keylogger",
    "hook",
    "spy",
    "logger",
    "monitor"
]

def scan_processes():
    found = []

    for process in psutil.process_iter(['pid', 'name']):
        try:
            # Handle empty process names safely
            process_name = str(process.info['name']).lower()

            for keyword in SUSPICIOUS_NAMES:
                if keyword in process_name:
                    found.append(
                        (process.info['pid'], process.info['name'])
                    )

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            continue

    return found


def main():
    print("=" * 50)
    print("   KEYLOGGER DETECTOR STARTED")
    print("=" * 50)

    try:
        while True:
            print("\nScanning system for suspicious processes...\n")

            threats = scan_processes()

            if threats:
                print("⚠ Suspicious processes found:\n")

                for pid, name in threats:
                    print(f"PID: {pid} | Process: {name}")

            else:
                print("✅ No suspicious processes detected.")

            print("\nNext scan in 10 seconds...")
            print("Press CTRL + C to stop.\n")

            time.sleep(10)

    except KeyboardInterrupt:
        print("\n\nProgram stopped safely by user.")
        print("Exiting Keylogger Detector...")


if __name__ == "__main__":
    main()