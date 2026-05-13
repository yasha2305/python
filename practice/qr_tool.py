import qrcode
import cv2

# Generate QR Code
def generate_qr():
    data = input("Enter text or URL: ").strip()

    if not data:
        print("Invalid input.")
        return

    img = qrcode.make(data)

    filename = "qrcode.png"
    img.save(filename)

    print(f"QR Code saved as {filename}")

# Scan QR Code
def scan_qr():
    detector = cv2.QRCodeDetector()

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Could not access webcam.")
        return

    print("Scanning QR Code...")
    print("Press 'q' to quit.\n")

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        data, bbox, _ = detector.detectAndDecode(frame)

        if data:
            print("\nQR Code Detected:")
            print("Data:", data)

            if bbox is not None:
                for i in range(len(bbox)):
                    pt1 = tuple(map(int, bbox[i][0]))
                    pt2 = tuple(map(int, bbox[(i + 1) % len(bbox)][0]))

                    cv2.line(frame, pt1, pt2, (0, 255, 0), 2)

        cv2.imshow("QR Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Main menu
def main():
    while True:
        print("\n--- QR TOOL ---")
        print("1. Generate QR Code")
        print("2. Scan QR Code")
        print("3. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            generate_qr()

        elif choice == "2":
            scan_qr()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()