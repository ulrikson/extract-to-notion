import os
from dotenv import load_dotenv
from openai import OpenAI


def transcribe_audio(client, file_path, language="auto", model="whisper-1"):
    """
    Transcribes the given audio file using OpenAI's Whisper API.

    :param client: OpenAI client instance.
    :param file_path: Path to the audio file.
    :param language: Language code ('en' for English, 'sv' for Swedish, or 'auto' for auto-detect).
    :param model: Model to use for transcription.
    :return: Transcribed text.
    """
    with open(file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model=model, file=audio_file, language=language
        )
    return transcription.text


if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("API key not found. Please set OPENAI_API_KEY in your .env file.")
        exit(1)

    client = OpenAI(api_key=api_key)

    file_path = input("Enter the path to the audio file: ")
    language = (
        input(
            "Enter the language ('en' for English, 'sv' for Swedish, or press Enter for auto-detect): "
        )
        or "auto"
    )

    try:
        result = transcribe_audio(client, file_path, language)
        print("\nTranscribed Text:\n")
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
