import time
import uuid
from playwright.sync_api import sync_playwright

def get_uuid():
    uuid_str = str(uuid.uuid4()).replace('-', '')
    return uuid_str

num = 0
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('')
    page.locator('xpath=/html/body/div[1]/div[2]/div/div[6]/div/div[2]/div[1]/div/ul/li[2]').click()
    time.sleep(2)
    page.locator('xpath=/html/body/div[1]/div[2]/div/div[6]/div/div[2]/div[2]/div[2]/ul/li[2]/div[2]/div/div[1]').click()
    time.sleep(2)
    while True:
        try:
            for i in range(5):
                print("抓取抓取的图片数量：{}".format(str(num)))
                uuid_str = get_uuid()
                page.locator('xpath=/html/body/div[11]/div/div[3]/div/div[2]/div[1]/div[2]/canvas').screenshot(path="./test_images/{}.png".format(uuid_str))
                page.locator('xpath=/html/body/div[11]/div/div[3]/div/div[4]/div[2]/span[2]/img').click()
                num += 1
                page.mouse.move(0,0)
                time.sleep(2)
            page.reload()
            time.sleep(3)
            page.locator('xpath=/html/body/div[1]/div[2]/div/div[6]/div/div[2]/div[1]/div/ul/li[2]').click()
            time.sleep(2)
            page.locator(
                'xpath=/html/body/div[1]/div[2]/div/div[6]/div/div[2]/div[2]/div[2]/ul/li[2]/div[2]/div/div[1]').click()
            time.sleep(2)
        except Exception as e:
            print("err:", e)
            print("出错了，重新启动浏览器！")
            time.sleep(5)
            browser.close()
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto('')
            page.locator('xpath=/html/body/div[1]/div[2]/div/div[6]/div/div[2]/div[1]/div/ul/li[2]').click()
            time.sleep(2)
            page.locator(
                'xpath=/html/body/div[1]/div[2]/div/div[6]/div/div[2]/div[2]/div[2]/ul/li[2]/div[2]/div/div[1]').click()
            time.sleep(2)
    page.pause()