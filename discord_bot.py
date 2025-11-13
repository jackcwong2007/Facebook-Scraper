import discord
import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from check import CheckForTicket
import time
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("bot logged in")
    last_ticket = "abc"

    driver = webdriver.Chrome()
    driver.get(config.GROUP_LINK)

    # fill in phone number
    text_box = driver.find_element(by=By.CSS_SELECTOR, value="#email")
    text_box.send_keys(config.PHONE_NUMBER)

    # fill in password
    text_box = driver.find_element(by=By.CSS_SELECTOR, value="#pass")
    text_box.send_keys(config.PASSWORD)

    # click the log in button
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="#loginbutton")
    submit_button.click()

    time.sleep(40)
    # DO CAPTCHA IN 40 SECONDS
    # SAY YOU DON'T WANT NOTIFICATIONS
    # SORT POSTS BY NEW NOT MOST RELEVANT

    while True:
        a = CheckForTicket(driver, last_ticket)
        last_ticket = a[1]
        if a[0]:  # checkforticket returns True!
            # discord bot function goes right here
            channel = client.get_channel(config.CHANNEL_ID)
            await channel.send("@everyone go go go go go!!!!")
            channel = client.get_channel(config.TEXT_CHANNEL_ID) #sends text in channel for testing purposes
            await channel.send(last_ticket)

        time.sleep(random.random() * 90)
        # adds a random time delay to the check, makes it more "human"

client.run(config.BOT_TOKEN)






