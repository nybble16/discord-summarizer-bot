# discord-summarizer-bot

`discord-summarizer-bot` is a Discord bot designed to provide concise summaries of channel conversations using OpenAI's GPT-4. It's built to help users catch up on missed discussions quickly and efficiently.

## Features

- Summarizes Discord channel messages over a specified time period.
- Uses OpenAI's GPT-4 for accurate and coherent summaries.
- Easy to deploy and use within any Discord server.
- Customizable summary timeframes.

## Installation

To install and run `discord-summarizer-bot` on your server, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/nybble16/discord-summarizer-bot.git
   ```
2. Install the required dependencies:
   ```bash
   cd discord-summarizer-bot
   pip install -r requirements.txt
   ```
3. To get your `discord-summarizer-bot` up and running, you'll need to configure your API keys as follows:
   1. OpenAI API Key 
      - Go to [OpenAI's API platform](https://beta.openai.com/signup/) and sign up for an account if you haven't already. 
      - Once you have an account, navigate to the API section and generate a new API key. 
      - Set the API key as an environment variable:
        ```bash
        export OPENAI_API_KEY='your_openai_api_key'
   2. Discord Bot Token
      - Head over to the [Discord Developer Portal](https://discord.com/developers/applications).
      - Create a new application and add a bot to it.
      - Under the "Bot" section, find and copy your bot token.
      - Set the token as an environment variable:
         ```bash
         export DISCORD_SUMMARY_BOT_TOKEN='your_discord_bot_token'
4. Confirm that the environment variables are set up:
    - `OPENAI_API_KEY`: Your OpenAI API key.
    - `DISCORD_SUMMARY_BOT_TOKEN`: Your Discord bot token.

5. Run the bot:
   ```bash
   python bot.py

## Usage

After inviting the bot to your Discord server, you can use the following commands:

- `/summary`: Summarizes the last day's messages in all channels.
- `/summary 2d`: Summarizes the last 2 days' messages in all channels.
- `/summary 6h`: Summarizes the last 6 hours' messages in all channels.
- `/summary 5m`: Summarizes the last 5 minutes' messages in all channels.


## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Tomasz Zmarz - [@nybble16](https://github.com/nybble16)

Project Link: [https://github.com/nybble16/discord-summarizer-bot](https://github.com/nybble16/discord-summarizer-bot)

## Acknowledgments

- [OpenAI](https://openai.com/)
- [Discord.py](https://github.com/Rapptz/discord.py)
