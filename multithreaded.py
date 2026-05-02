import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed

urls = [
    "https://example.com",
    "https://httpbin.org/html",
    "https://www.python.org",
]

def fetch_title(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title and soup.title.string else "No Title Found"

        return f"{url} --> {title}"

    except Exception as e:
        return f"{url} --> Error: {type(e).__name__}: {e}"

def main():
    print("Fetching titles using multithreading...\n")

    results = [None] * len(urls)

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(fetch_title, url): i for i, url in enumerate(urls)}

        for future in as_completed(futures):
            index = futures[future]
            results[index] = future.result()

    for res in results:
        print(res)

if __name__ == "__main__":
    main()