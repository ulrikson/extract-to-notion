import os
import requests
from dotenv import load_dotenv


def load_env_variables():
    """
    Loads environment variables for Notion API.

    This function loads the environment variables from a .env file using the load_dotenv() function.
    It retrieves the Notion API key and the Notion database ID from the environment variables.

    Returns:
        tuple: A tuple containing the Notion API key and the Notion database ID.
    """
    load_dotenv()
    notion_api_key = os.getenv("NOTION_API_KEY")
    notion_db_id = os.getenv("NOTION_DB_ID")
    return notion_api_key, notion_db_id


def get_headers(notion_api_key):
    """
    Generate the headers required for making requests to the Notion API.

    Args:
        notion_api_key (str): The API key for authenticating with the Notion API.

    Returns:
        dict: A dictionary containing the necessary headers for the Notion API requests.
    """
    return {
        "Authorization": f"Bearer {notion_api_key}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
    }


def get_data(notion_db_id, title_content, body_content):
    """
    Constructs a dictionary payload for creating a new page in a Notion database.

    Args:
        notion_db_id (str): The ID of the Notion database where the page will be created.
        title_content (str): The title content for the new page.
        body_content (str): The body content for the new page.

    Returns:
        dict: A dictionary representing the payload to create a new page in the specified Notion database.
    """
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


def create_page(title, body):
    """
    Creates a new page in a Notion database.

    Args:
        title (str): The title of the new page.
        body (str): The content/body of the new page.

    Returns:
        dict: The JSON response from the Notion API containing details of the created page.

    Raises:
        requests.exceptions.RequestException: If there is an issue with the HTTP request.
    """
    notion_api_key, notion_db_id = load_env_variables()
    url = "https://api.notion.com/v1/pages"
    headers = get_headers(notion_api_key)
    data = get_data(notion_db_id, title, body)

    response = requests.post(url, headers=headers, json=data)
    return response.json()


if __name__ == "__main__":
    response = create_page(
        "Test Title", "This is a test page created using the Notion API."
    )
    print(response)
