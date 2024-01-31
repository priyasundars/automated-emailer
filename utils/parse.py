import re
import requests
from bs4 import BeautifulSoup


def get_rates():
    # Send a GET request to the URL
    url = "https://www.rbi.org.in/"
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all table rows (tr)
    table_rows = soup.find_all("tr")

    # Initialize an empty dictionary
    data = {}

    # Iterate over table rows
    for row in table_rows:
        # Find the two table data elements (td)
        cells = row.find_all("td")
        if len(cells) == 2:
            # Extract the key and value
            key = cells[0].get_text(strip=True)
            value = cells[1].get_text(strip=True)
            value = re.sub(r"[:%*\n\r#]", "", value).strip()
            # Add the key-value pair to the dictionary
            data[key] = value

    # Print the resulting dictionary
    print("Data retriving data from rbi")
    return data
