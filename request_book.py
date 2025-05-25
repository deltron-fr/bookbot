import requests

def save_file_content():
    url = "https://www.gutenberg.org/cache/epub/41445/pg41445.txt"
    response = requests.get(url)
    text = response.text

    with open("./books/frankenstein.txt", 'w', encoding='utf-8') as file_write:
        file_write.write(text)