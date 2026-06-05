import requests
from concurrent.futures import ThreadPoolExecutor

# Check one URL
def check_url(url):
    try:
        response = requests.get(
            url,
            timeout=5
        )

        return (
            url,
            response.status_code
        )

    except:
        return (
            url,
            "FAILED"
        )

# Main Program
def main():

    urls = []

    print(
        "Enter URLs "
        "(type done to finish):"
    )

    while True:

        url = input("> ")

        if url.lower() == "done":
            break

        urls.append(url)

    print("\nChecking links...\n")

    with ThreadPoolExecutor(
        max_workers=10
    ) as executor:

        results = executor.map(
            check_url,
            urls
        )

    print(
        "===== RESULTS ====="
    )

    for url, status in results:

        if status == 200:

            print(
                f"✅ {url} "
                f"(Working)"
            )

        elif status == "FAILED":

            print(
                f"❌ {url} "
                f"(Failed)"
            )

        else:

            print(
                f"⚠️ {url} "
                f"(Status: {status})"
            )

if __name__ == "__main__":
    main()