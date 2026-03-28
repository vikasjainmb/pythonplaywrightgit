from playwright.sync_api import sync_playwright

def before_scenario(context, scenario):
    headless = context.config.userdata.get("headless", "true").lower() in ("1", "true", "yes")
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()

def after_scenario(context, scenario):
    if getattr(context, "page", None):
        context.page.close()
    if getattr(context, "browser", None):
        context.browser.close()
    if getattr(context, "playwright", None):
        context.playwright.stop()