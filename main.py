# general libraries
import os
import time
import requests
from dotenv import load_dotenv

# functions
from llm_functions import generate_script, generate_caption
from email_functions import send_email_with_attachments

# load environment variables
load_dotenv()

if __name__ == "__main__":
    response = requests.get(os.getenv("WEEKLY_BOOKS"))
    books = response.json()
    files = list()
    for book in books:
        script = generate_script(book["title"], book["authors"], book["description"])
        caption = generate_caption(book["title"], book["authors"], book["description"])
        files.append({
            "title": book["title"],
            "weekday": book["weekday"],
            "authors": book["authors"],
            "script": script,
            "caption": caption
        })
        time.sleep(30)
        print(f"{book['title']} captioned and scripted...")
    send_email_with_attachments(files)