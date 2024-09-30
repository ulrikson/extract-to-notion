from open_ai_api import transcribe_audio, analyze_image
from notion_api import create_page


def prompt_create_page(title, body):
    """
    Prompts the user to create a Notion page with the given title and body.

    Args:
        title (str): The title of the Notion page.
        body (str): The body content of the Notion page.
    """
    create_page_option = input(
        "Do you want to create a Notion page with the result? (y/n): "
    )
    if create_page_option.lower() == "y":
        create_page(title=title, body=body)
        print("\nThe result has been added to Notion.")


def main():
    """
    Main function to handle user input and perform actions based on the selected option.

    1. Transcribe Audio: Asks for the path to an audio file.
        Calls the transcribe_audio function and creates a Notion page with the transcription result.
    2. Analyze Image: Asks for the path to an image file.
        Calls the analyze_image function and creates a Notion page with the analysis result.

    Handles exceptions and prints appropriate error messages.

    Raises:
         Exception: If an error occurs during transcription or image analysis.
    """
    option = input(
        "Choose an option:\n1. Transcribe Audio\n2. Analyze Image\nEnter 1 or 2: "
    )

    if option == "1":
        file_path = input("Enter the path to the audio file: ")
        language = (
            input(
                "Enter the language ('en' for English, 'sv' for Swedish, or press Enter for auto-detect): "
            )
            or "auto"
        )
        try:
            result = transcribe_audio(file_path, language)
            print(result, "\n")
            prompt_create_page(title=file_path, body=result)
        except Exception as e:
            print(f"An error occurred: {e}")
    elif option == "2":
        file_path = input("Enter the path to the image file: ")
        try:
            result = analyze_image(file_path)
            print(result, "\n")
            prompt_create_page(title=file_path, body=result)
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid option selected.")


if __name__ == "__main__":
    main()
