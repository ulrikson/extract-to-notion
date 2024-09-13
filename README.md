# OpenAI Whisper Transcription Script

A simple Python script that uses the OpenAI Whisper API to transcribe audio files in English or Swedish. The script reads your OpenAI API key from a `.env` file for security.

## Features

- **Transcribe Audio Files:** Supports various audio formats like MP3, WAV, M4A, and FLAC.
- **Language Support:** Transcribe in English (`en`), Swedish (`sv`), or auto-detect the language.
- **Secure API Key Handling:** Utilizes a `.env` file to keep your OpenAI API key secure.
- **Easy to Use:** Simple command-line interface for quick transcription.

## Requirements

- Python 3.6 or higher
- OpenAI account with an API key
- `pip` package manager

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your_username/your_repository.git
cd your_repository
```

### 2. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install openai python-dotenv
```

### 3. Set Up the `.env` File

Create a `.env` file in the project directory and add your OpenAI API key:

```env
OPENAI_API_KEY=your_api_key_here
```

**Note:** Replace `your_api_key_here` with your actual OpenAI API key.

## Usage

Run the script using Python:

```bash
python your_script_name.py
```

When prompted:

1. **Enter the Path to the Audio File:**

   Provide the full path or relative path to the audio file you wish to transcribe.

2. **Enter the Language:**

   - Type `en` for English.
   - Type `sv` for Swedish.
   - Press **Enter** to auto-detect the language.

### Example

```bash
Enter the path to the audio file: samples/meeting_notes.mp3
Enter the language ('en' for English, 'sv' for Swedish, or press Enter for auto-detect): en

Transcribed Text:

[Your transcribed text will appear here]
```

## Supported Audio Formats

The script supports the following audio formats:

- **MP3**
- **WAV**
- **M4A**
- **FLAC**
- **WEBM**
- **MP4**
- **MPEG**
- **MPGA**
- **M4A**
- **OGG**
- **WMA**
- **3GP**

## File Structure

```
your_repository/
│
├── your_script_name.py      # The main Python script
├── .env                     # Environment file containing the API key
├── requirements.txt         # Optional: List of dependencies
└── README.md                # This README file
```

## Troubleshooting

- **API Key Not Found:**

  If you receive an error about the API key not being found, ensure that:

  - The `.env` file is in the same directory as your script.
  - The key in the `.env` file is correctly named `OPENAI_API_KEY`.

- **Invalid API Key:**

  Make sure your API key is valid and has the necessary permissions.

- **File Not Found:**

  Ensure the path to your audio file is correct. Use an absolute path if necessary.

- **Unsupported File Format:**

  Confirm that your audio file is in a supported format listed above.

## Customization

- **Changing the Model:**

  The script uses the `whisper-1` model by default. You can change the model by modifying the `model` parameter in the `transcribe_audio` function:

  ```python
  def transcribe_audio(client, file_path, language='auto', model='your_model_choice'):
      # Rest of the code...
  ```

- **Improving Transcription Accuracy:**

  - Use high-quality audio recordings.
  - Minimize background noise.
  - Ensure clear pronunciation in the audio.

## Security

- **API Key Safety:**

  - Do not share your API key publicly.
  - Ensure your `.env` file is included in your `.gitignore` file to prevent it from being pushed to GitHub.

- **Environment Variables:**

  Consider setting the `OPENAI_API_KEY` as an environment variable on your system instead of using a `.env` file.

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**

   Click on the 'Fork' button on the top right to create a copy of this repository on your GitHub account.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/your_username/your_repository.git
   ```

3. **Create a New Branch**

   ```bash
   git checkout -b feature/your_feature_name
   ```

4. **Make Changes**

   Add your improvements or new features.

5. **Commit and Push**

   ```bash
   git add .
   git commit -m "Add your commit message here"
   git push origin feature/your_feature_name
   ```

6. **Create a Pull Request**

   Open a pull request on the original repository to merge your changes.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [OpenAI](https://www.openai.com/) for providing the Whisper API.
- [Python Dotenv](https://github.com/theskumar/python-dotenv) for managing environment variables.

## Contact

For any questions or suggestions, please open an issue or contact me at [erik@billebjer.se](mailto:erik@billebjer.se).
