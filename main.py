import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.download_speed = None
        self.upload_speed = None
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        print("Running speed test... please wait ⏳")

        self.driver.find_element(By.CSS_SELECTOR, ".start-text").click()
        WebDriverWait(self.driver, 120).until(
            lambda d: d.find_element(By.CSS_SELECTOR, "span.download-speed").text != ""
        )

        self.download_speed = self.driver.find_element(By.CSS_SELECTOR, "span.download-speed").text
        self.upload_speed = self.driver.find_element(By.CSS_SELECTOR, "span.upload-speed").text

        print(f"Download: {self.download_speed} Mbps")
        print(f"Upload: {self.upload_speed} Mbps")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        wait = WebDriverWait(self.driver, 30)

        # Login
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "text")))
        email_input.send_keys(TWITTER_EMAIL)
        email_input.send_keys(Keys.ENTER)
        time.sleep(2)

        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

        # Compose tweet
        tweet_box = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Post text"]'))
        )
        tweet_box.send_keys(
            f"Hey Internet Provider, why is my internet speed {self.download_speed} down/"
            f"{self.upload_speed} up when I pay for {self.down} down/{self.up} up?"
        )

        tweet_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-testid="tweetButtonInline"]'))
        )
        tweet_button.click()
        print("Tweet sent successfully 🐦")

        self.driver.quit()

# Run
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
