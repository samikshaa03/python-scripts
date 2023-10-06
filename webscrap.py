import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = 'http://quotes.toscrape.com/'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract data from the page
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    tags = soup.find_all('div', class_='tags')

    # Loop through the extracted data and print it
    for i in range(len(quotes)):
        print("Quote:", quotes[i].text)
        print("Author:", authors[i].text)
        tag_list = [tag.text for tag in tags[i].find_all('a', class_='tag')]
        print("Tags:", ', '.join(tag_list))
        print()
else:
    print('Failed to retrieve the web page.')

