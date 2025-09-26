# Manga Cover Bot 🤖📚

[![Manga Cover Bot](https://github.com/elxecutor/cover-bot/actions/workflows/manga-bot.yml/badge.svg)](https://github.com/elxecutor/cover-bot/actions/workflows/manga-bot.yml)

An automated bot that fetches random manga covers from MangaDex and posts them to X (Twitter).

## Features

- 🎲 Fetches random manga covers from top-rated English manga on MangaDex
- 🐦 Posts to X (Twitter) with manga title
- 🔄 Automated GitHub Actions workflow
- 🛡️ Error handling and cleanup

## Setup

### 1. X (Twitter) API Credentials

You'll need to create a Twitter Developer account and get API credentials:

1. Go to [Twitter Developer Portal](https://developer.twitter.com/)
2. Create a new app
3. Generate API keys and tokens

### 2. Environment Variables

Create a `.env` file in the project root:

```env
X_API_KEY=your_api_key
X_API_SECRET=your_api_secret
X_ACCESS_TOKEN=your_access_token
X_ACCESS_TOKEN_SECRET=your_access_token_secret
X_BEARER_TOKEN=your_bearer_token
```

### 3. GitHub Secrets (for automated workflow)

In your GitHub repository, go to Settings > Secrets and variables > Actions, and add:

- `X_API_KEY`
- `X_API_SECRET`
- `X_ACCESS_TOKEN`
- `X_ACCESS_TOKEN_SECRET`
- `X_BEARER_TOKEN`

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Manual Run
```bash
python main.py
```

### Automated Schedule
The GitHub Actions workflow runs every 90 minutes automatically. You can also trigger it manually from the Actions tab.

## Configuration

### Manga Selection
The bot fetches from the top 608 rated English manga on MangaDex. Modify `core/manga_cover.py` to change this behavior.

## File Structure

```
├── main.py                 # Main entry point
├── requirements.txt        # Python dependencies
├── core/
│   ├── manga_cover.py     # MangaDex API integration
│   └── x_poster.py        # X (Twitter) posting
└── .github/workflows/
    └── manga-bot.yml      # GitHub Actions workflow
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.