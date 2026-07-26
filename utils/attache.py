import time
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

import allure
from allure_commons.types import AttachmentType

SELENOID_VIDEO_URL = "https://user1:1234@selenoid.qa.guru/video/{}.mp4"


def add_screenshot(driver, name="screenshot"):
    allure.attach(
        driver.get_screenshot_as_png(),
        name=name,
        attachment_type=AttachmentType.PNG,
    )


def add_logs(driver, name="browser_logs"):
    try:
        logs = driver.get_log("browser")
        log_text = "\n".join(
            f"[{entry['level']}] {entry['message']}" for entry in logs
        ) or "Логи браузера пусты"
    except Exception as error:
        log_text = f"Не удалось получить логи браузера: {error}"

    allure.attach(log_text, name=name, attachment_type=AttachmentType.TEXT)


def add_video(session_id, name="video"):
    url = SELENOID_VIDEO_URL.format(session_id)
    video = b""

    for _ in range(15):
        try:
            with urlopen(url, timeout=10) as response:
                video = response.read()
            if video and len(video) > 1000:
                break
        except (URLError, HTTPError, TimeoutError, OSError):
            pass
        time.sleep(1)

    if video:
        allure.attach(video, name=name, attachment_type=AttachmentType.MP4)
