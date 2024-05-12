import requests
from bs4 import BeautifulSoup


def fetch_articles(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Checks for HTTP request errors
    except requests.RequestException as e:
        return {'error': str(e)}

    soup = BeautifulSoup(response.content, 'html.parser')
    collected_articles = []

    for anchor in soup.find_all('a', attrs={'data-testid': ['external-anchor', 
                            'internal-link']}):
        headline = anchor.find('h2', attrs={'data-testid': 'card-headline'})
        summary = anchor.find('p', attrs={'data-testid': 'card-description'})
        if headline and summary:
            collected_articles.append({
                'title': headline.text.strip(),
                'description': summary.text.strip(),
                'link': anchor['href'] if anchor['href'].startswith('http') 
                else 'https://www.bbc.com' + anchor['href']
            })

    return collected_articles


def display_bbc_articles():
    target_url = 'https://www.bbc.com'
    articles = fetch_articles(target_url)
    if 'error' in articles:
        print(f"Failed to retrieve data: {articles['error']}")
    else:
        for article in articles:
            print(article['title'], article['link'], article['description'])


if __name__ == "__main__":
    display_bbc_articles()
