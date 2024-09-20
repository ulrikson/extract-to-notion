# Audio and Image Text Extractor To Notion

This application allows you to transcribe audio files or extract text from image files using the OpenAI API. The extracted text is then uploaded to a user-specified database in Notion using the Notion API.

## Key Features

- **Audio Transcription**: Convert audio files into text using the OpenAI API.
- **Image Text Extraction**: Extract text from image files using the OpenAI API.
- **Notion Integration**: Upload the extracted text to a specified database in Notion.

## Prerequisites

- Python installed on your machine
- OpenAI API key
- Notion API key and database ID

## Installation

Create a `.env` file in the root directory and add your OpenAI and Notion API keys:

```env
OPENAI_API_KEY=your_openai_api_key
NOTION_API_KEY=your_notion_api_key
NOTION_DATABASE_ID=your_notion_database_id
```

## Usage

```python
python main.py
```

The extracted text will be automatically uploaded to the specified Notion database.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.