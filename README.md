# Audio and Image Text Extractor To Notion

## My Goal

I use Notion for taking notes. When I record voice notes, I want to transcribe them and send them to Notion. So, I built this application. It transcribes audio files and extracts text from images using the OpenAI API. The extracted text is uploaded to a Notion database specified by the user.

Features

- **Audio Transcription**: Convert audio files into text using the OpenAI API.
- **Image Text Extraction**: Extract text from image files using the OpenAI API.
- **Notion Integration**: Upload the extracted text to a specified database in Notion.

## Getting Started
### Prerequisites

- Python installed on your machine
- OpenAI API key
- Notion API key and database ID

### Installation

Create a `.env` file in the root directory and add your OpenAI and Notion API keys:

```env
OPENAI_API_KEY=your_openai_api_key
NOTION_API_KEY=your_notion_api_key
NOTION_DATABASE_ID=your_notion_database_id
```

### Usage

```python
python main.py
```

The extracted text will be automatically uploaded to the specified Notion database.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
