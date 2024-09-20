from open_ai_api import transcribe_audio, analyze_image


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
            print("\nTranscribed Text from Audio:\n")
            print(result)
        except Exception as e:
            print(f"An error occurred: {e}")
    elif option == "2":
        image_path = input("Enter the path to the image file: ")
        try:
            result = analyze_image(image_path)
            print("\nAnalysis of the Image:\n")
            print(result)
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid option selected.")


if __name__ == "__main__":
    main()
