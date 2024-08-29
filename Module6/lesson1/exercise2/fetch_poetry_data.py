
import requests

def fetch_poems_by_author(author_name):
    url = f"https://poetrydb.org/author/{author_name}"
    try:
        response = requests.get(url)
        poems = response.json()

        if isinstance(poems, list):
            for poem in poems:
                title = poem.get("title", "No Title")
                lines = poem.get("lines", "No Lines")
                print(f"Title: {title}\n{' '.join(lines[:5])}...\n")

        else:
            status = poems.get("status")
            reason = poems.get("reason", "Unknown error")
            print(f"Error: {status}: {reason}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


fetch_poems_by_author("Emily Dickinson")