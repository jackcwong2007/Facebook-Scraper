# Facebook Scraper Bot
Discord bot that scrapes a Facebook group feed for posts with specific text and notifies a Discord channel when a post that contains any of the words is found.

You can find a demo [here](https://youtube.com/shorts/C31ymE5Jk1s?feature=share)

# What it does
- Uses Selenium to open a Facebook group feed and read the latest post(s).
- Detects text matching trigger words you configure.
- When it finds a new candidate post, sends notifications to one or more Discord channels via a bot.
- Adds a small randomized delay between checks to avoid constant polling.

# How to use
- Clone this repo
- Install required packages (Selenium, discord.py, python 3.8+)
- Fill out config.py with your own information
- Run discord_bot.py
- Complete captcha, disable notifications, sort posts by most relevant (you have a 40s grace period to do this)
