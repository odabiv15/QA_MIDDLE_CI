import allure
from allure_commons.types import AttachmentType


def add_screenshot(driver):
    allure.attach(
        driver.get_screenshot_as_png(),
        name="screenshot",
        attachment_type=AttachmentType.PNG,
    )


def add_console_logs(driver):
    logs = "".join(
        f'{log["message"]}\n'
        for log in driver.execute("getLog", {"type": "browser"})["value"]
    )
    allure.attach(logs, "browser_logs", AttachmentType.TEXT, ".log")


def add_page_source(driver):
    allure.attach(
        driver.page_source,
        "page_source",
        AttachmentType.HTML,
        ".html",
    )


def add_video(driver, selenoid_url="https://selenoid.qa.guru/wd/hub"):
    # https://host/wd/hub → https://host/video/<session>.mp4
    base = selenoid_url.rstrip("/").removesuffix("/wd/hub")
    video_url = f"{base}/video/{driver.session_id}.mp4"
    html = (
        "<html><body>"
        "<video width='100%' height='100%' controls autoplay>"
        f"<source src='{video_url}' type='video/mp4'>"
        "</video>"
        "</body></html>"
    )
    allure.attach(
        html,
        "video_" + driver.session_id,
        AttachmentType.HTML,
        ".html",
    )
