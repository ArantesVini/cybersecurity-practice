import argparse
import re
import requests
from bs4 import BeautifulSoup


def scrape_emails(url, max_depth=100):
    session = requests.Session()
    urls = set([url])
    scraped_urls = set()
    emails = set()
    depth = 0

    while urls and depth < max_depth:
        depth += 1
        url = urls.pop()
        scraped_urls.add(url)

        try:
            response = session.get(url)
            response.raise_for_status()
        except (requests.exceptions.RequestException, ValueError):
            continue

        new_emails = set(re.findall(
            r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
        emails.update(new_emails)

        soup = BeautifulSoup(response.text, features="lxml")

        for link in soup.find_all('a', href=True):
            link_url = link['href']
            if link_url.startswith('mailto:'):
                emails.add(link_url[7:])
            elif link_url.startswith(('http://', 'https://')):
                urls.add(link_url)
            elif link_url.startswith('/'):
                urls.add(url + link_url)
            else:
                urls.add(url + '/' + link_url)

    return emails


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Scrape emails from a website')
    parser.add_argument('url', help='The URL to scrape')
    parser.add_argument('--depth', type=int, default=100,
                        help='The maximum depth to crawl')
    args = parser.parse_args()

    emails = scrape_emails(args.url, args.depth)

    for email in emails:
        print(email)
