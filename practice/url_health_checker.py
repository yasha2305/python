import requests

while True:

    url = input("\nWebsite URL (exit to quit): ")

    if url.lower() == "exit":
        break

    try:

        response = requests.get(url, timeout=5)

        print("Status Code :", response.status_code)

        if response.status_code == 200:
            print("✅ Website is Online")
        else:
            print("⚠ Website returned an error")

    except Exception:
        print("❌ Website is Offline")