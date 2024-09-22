from open_ai_api import transcribe_audio, analyze_image
from notion_api import create_page


def main():
    """
    Main function to handle user input for transcribing audio or analyzing images.

    Prompts the user to choose between two options:
    1. Transcribe Audio: Asks for the path to an audio file and the language for transcription.
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
            create_page(title=file_path, body=result)
            print("\nTranscription has been added to Notion.")
        except Exception as e:
            print(f"An error occurred: {e}")
    elif option == "2":
        file_path = input("Enter the path to the image file: ")
        try:
            result = analyze_image(file_path)
            print(result)
            create_page(title=file_path, body=result)
            print("\nImage analysis has been added to Notion.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid option selected.")


if __name__ == "__main__":
    main()
