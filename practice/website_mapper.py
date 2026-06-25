import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

visited = set()

def crawl(url, domain, depth):

    if depth == 0 or url in visited:
        return

    visited.add(url)

    try:

        response = requests.get(
            url,
            timeout=5
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        print(url)

        for link in soup.find_all("a"):

            href = link.get("href")

            if not href:
                continue

            full_url = urljoin(
                url,
                href
            )

            if (
                urlparse(full_url).netloc
                == domain
            ):

                crawl(
                    full_url,
                    domain,
                    depth - 1
                )

    except:
        pass

start_url = input(
    "Website URL: "
)

domain = urlparse(
    start_url
).netloc

crawl(
    start_url,
    domain,
    2
)