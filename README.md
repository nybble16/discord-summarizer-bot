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
3. Set up your environment variables:
    - `OPENAI_API_KEY`: Your OpenAI API key.
    - `DISCORD_SUMMARY_BOT_TOKEN`: Your Discord bot token.

4. Run the bot:
   ```bash
   python bot.py
   ```

## Usage

After inviting the bot to your Discord server, you can use the following commands:

- `/summary 1d`: Summarizes the last day's messages in all channels.
- `/summary 6h`: Summarizes the last 6 hours' messages in all channels.

## Configuration

You can configure the bot further by editing the `config.py` file (if you have one) or directly within the bot's code to adjust the summary length, targeted channels, and more.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Tomasz Zmarz - [@nybble16](https://github.com/nybble16)

Project Link: [https://github.com/nybble16/discord-summarizer-bot](https://github.com/nybble16/discord-summarizer-bot)

## Acknowledgments

- [OpenAI](https://openai.com/)
- [Discord.py](https://github.com/Rapptz/discord.py)
