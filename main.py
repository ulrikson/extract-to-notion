import os
import base64
import requests
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


def encode_image(image_path):
    """
    Encodes the image at the given path to a base64 string.

    :param image_path: Path to the image file.
    :return: Base64-encoded string of the image.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def analyze_image(api_key, image_path, model="gpt-4o-mini"):
    """
    Analyzes the given local image file using OpenAI's Vision capabilities.

    :param api_key: Your OpenAI API key.
    :param image_path: Path to the image file.
    :param model: Model to use for image analysis.
    :return: Description or transcription of the image content.
    """
    base64_image = encode_image(image_path)
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    # Determine the image MIME type
    mime_type = "image/jpeg"
    if image_path.lower().endswith(".png"):
        mime_type = "image/png"
    elif image_path.lower().endswith(".gif"):
        mime_type = "image/gif"

    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Transcribe the text in this image:"},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:{mime_type};base64,{base64_image}"},
                    },
                ],
            }
        ],
        # "max_tokens": 300,
    }
    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=payload
    )
    response_data = response.json()
    if response.status_code == 200:
        return response_data["choices"][0]["message"]["content"]
    else:
        error_message = response_data.get("error", {}).get(
            "message", "Unknown error occurred."
        )
        raise Exception(f"API Error: {error_message}")


if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("API key not found. Please set OPENAI_API_KEY in your .env file.")
        exit(1)

    client = OpenAI(api_key=api_key)

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
            result = transcribe_audio(client, file_path, language)
            print("\nTranscribed Text from Audio:\n")
            print(result)
        except Exception as e:
            print(f"An error occurred: {e}")
    elif option == "2":
        image_path = input("Enter the path to the image file: ")
        try:
            result = analyze_image(api_key, image_path)
            print("\nAnalysis of the Image:\n")
            print(result)
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid option selected.")
