import re


def normalize_text(input_text):
    """Normalize whitespace, remove punctuation, and trim whitespace from the text."""
    normalized_text = re.sub(r'\s+', ' ', input_text)  # Collapse multiple whitespaces into one
    normalized_text = re.sub(r'[^\w\s]', '', normalized_text)  # Remove all non-word characters except spaces
    return normalized_text.strip()  # Remove leading and trailing whitespace


def clean_article_data(article_data):
    """Clean the text fields in each article dictionary."""
    for article in article_data:
        article['title'] = normalize_text(article['title'])
        article['description'] = normalize_text(article['description'])
    return article_data


if __name__ == "__main__":
    sample_articles = [
        {'title': 'New Discoveries @ the Moon!', 'link': 'http://example.com/1', 'description': 'Explore more; about space...'},
        {'title': 'Tech Advances in 2024', 'link': 'http://example.com/2', 'description': 'Tech is evolving rapidly - see how!'},
    ]
    cleaned_articles = clean_article_data(sample_articles)
    print(cleaned_articles)
