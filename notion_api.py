import os
import requests
from dotenv import load_dotenv


def load_env_variables():
    load_dotenv()
    notion_api_key = os.getenv("NOTION_API_KEY")
    notion_db_id = os.getenv("NOTION_DB_ID")
    return notion_api_key, notion_db_id


def get_headers(notion_api_key):
    return {
        "Authorization": f"Bearer {notion_api_key}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
    }


def get_data(notion_db_id, title_content, body_content):
    return {
        "parent": {"database_id": notion_db_id},
        "properties": {
            "Name": {"title": [{"text": {"content": title_content}}]},
        },
        "children": [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": body_content,
                            },
                        }
                    ]
                },
            }
        ],
    }


def create_page():
    notion_api_key, notion_db_id = load_env_variables()
    url = "https://api.notion.com/v1/pages"
    headers = get_headers(notion_api_key)
    data = get_data(notion_db_id)

    response = requests.post(url, headers=headers, json=data)
    return response.json()


if __name__ == "__main__":
    response = create_page()
    print(response)
