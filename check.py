from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config


def CheckForTicket(driver, last_ticket):
    driver.refresh()

    iframe = driver.find_element(By.XPATH, "(//div[@role='feed'])")  # scrolls to feed element
    ActionChains(driver).scroll_to_element(iframe).perform()
    wait = WebDriverWait(driver, 10)
    first_post = wait.until(
        EC.presence_of_element_located((By.XPATH, "(//div[@role='feed'])")))  # waits then looks at feed
    crop = first_post.text.find("All reactions:")  # cropping everything after all reactions to prevent amount of likes and comments
    post_text = first_post.text[:crop]             # affecting the script
    print(post_text[-15:])
    print(last_ticket[-15:])

    for key in config.FSK:
        if key in post_text.lower() and "out" not in post_text.lower() and post_text[-15:] != last_ticket[-15:]:
            print("text detected!")
            return True, post_text
    return False, post_text
