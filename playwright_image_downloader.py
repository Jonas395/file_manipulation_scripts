import asyncio
import os
import requests
from playwright.async_api import async_playwright, expect
from urllib.parse import urlparse

from file_utility import ensure_directory

directory = "images" # Directory to save images

website = ""
image_locator = ""
next_button = ""

async def accept_cookies(page):
    await page.get_by_role("button", name="Accept").click() # Adjust the selector as needed


async def download_image_from_locator(page, locator_str, save_dir=directory):
    img_element = page.locator(locator_str)
    img_url = await img_element.get_attribute("src")

    if not img_url:
        raise ValueError(f"No image found inside locator {locator_str}")

    if img_url.startswith('/'):
        img_url = page.url.rsplit('/', 1)[0] + img_url

    filename = os.path.basename(urlparse(img_url).path)
    if not filename:
        filename = "downloaded_image.jpg"

    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, filename)

    response = requests.get(img_url)
    response.raise_for_status()
    with open(save_path, "wb") as f:
        f.write(response.content)

    print(f"✅ Image downloaded: {os.path.abspath(save_path)}")
    return save_path



async def main():
    ensure_directory(directory)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(website)
        #await accept_cookies(page) # Accept cookies if necessary

        while True:
            try:
                await download_image_from_locator(page, image_locator)
                next_button = page.get_by_role("link", name="Next >") # Adjust the selector as needed
                await next_button.click()


            except Exception:
                await print("No next page or navigation did not occur. Stopping.")
                break
        await browser.close()

#os.environ["PWDEBUG"] = "1"
asyncio.run(main())
