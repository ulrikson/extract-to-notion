from open_ai_api import transcribe_audio, analyze_image
from notion_api import create_page


def main():
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
            create_page(title_content=file_path, content=result)
            print("\nTranscription has been added to Notion.")
        except Exception as e:
            print(f"An error occurred: {e}")
    elif option == "2":
        image_path = input("Enter the path to the image file: ")
        try:
            result = analyze_image(image_path)
            create_page(title=image_path, body=result)
            print("\nImage analysis has been added to Notion.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid option selected.")


if __name__ == "__main__":
    main()
