import requests
import time

# Check website status
def check_website(url):

    try:
        start_time = time.time()

        response = requests.get(url, timeout=5)

        end_time = time.time()

        response_time = end_time - start_time

        print(f"\nWebsite: {url}")
        print(f"Status Code : {response.status_code}")
        print(f"Response Time: {response_time:.2f} seconds")

        if response.status_code == 200:

            if response_time < 1:
                print("Status: FAST & ONLINE ✅")

            elif response_time < 3:
                print("Status: ONLINE ⚠️")

            else:
                print("Status: SLOW RESPONSE 🐢")

        else:
            print("Status: ISSUE DETECTED ❌")

    except requests.exceptions.RequestException:
        print(f"\nWebsite: {url}")
        print("Status: OFFLINE ❌")

# Main program
def main():

    print("=== WEBSITE STATUS CHECKER ===\n")

    websites = []

    while True:

        url = input(
            "Enter website URL "
            "(or type 'done'): "
        ).strip()

        if url.lower() == "done":
            break

        if not url.startswith("http"):
            url = "https://" + url

        websites.append(url)

    if not websites:
        print("No websites provided.")
        return

    for site in websites:
        check_website(site)

if __name__ == "__main__":
    main()