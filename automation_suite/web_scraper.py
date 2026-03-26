import requests
from bs4 import BeautifulSoup
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://example.com"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, verify=False)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract multiple elements
    headings = soup.find_all("h1")
    paragraphs = soup.find_all("p")
    links = soup.find_all("a")

    with open("scraped_data.txt", "w") as f:
        f.write("HEADINGS:\n")
        for h in headings:
            f.write(h.text + "\n")

        f.write("\nPARAGRAPHS:\n")
        for p in paragraphs:
            f.write(p.text + "\n")

        f.write("\nLINKS:\n")
        for a in links:
            f.write(a.get("href", "") + "\n")

    print("Data extracted successfully")

else:
    print("Failed to fetch data")