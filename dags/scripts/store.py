import json
import os


def save_articles_to_file(article_data, output_filename):
    """Save article data to a JSON file with indentation."""
    with open(output_filename, 'w') as file:
        json.dump(article_data, file, indent=4)


def setup_version_control():
    """Initialize DVC in the project directory if not already set up."""
    if not os.path.exists('.dvc'):
        os.system('dvc init')


def track_file_with_dvc(file_path):
    """Add the specified file to DVC and Git, then push to the DVC remote storage."""
    os.system(f'dvc add {file_path}')
    os.system(f'git add {file_path}.dvc .gitignore')
    os.system(f'git commit -m "Add/update {file_path}"')
    os.system(f'dvc push {file_path}')


def process_and_store_articles(articles):
    filename = 'articles.json'
    save_articles_to_file(articles, filename)
    setup_version_control()
    track_file_with_dvc(filename)


if __name__ == "__main__":
    example_articles = [
        {'title': 'Example Title 1', 'link': 'http://example.com/1', 'description': 'Description 1'},
        {'title': 'Example Title 2', 'link': 'http://example.com/2', 'description': 'Description 2'},
    ]
    process_and_store_articles(example_articles)
