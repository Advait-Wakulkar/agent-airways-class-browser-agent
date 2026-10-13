"""The starting browser tools for the shared Agent Airways class project.

Students will add tools here through reviewed pull requests.
Each tool should do one understandable job and return an observation.
"""

from playwright.sync_api import sync_playwright

SITE_URL = "https://onyourmark.github.io/browser-agent-form/travel/"

playwright = None
browser = None
page = None


def start_browser():
    """Start a visible Chromium window on the student's computer."""
    global playwright, browser, page
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=400)
    page = browser.new_page()
    page.set_default_timeout(5000)


def close_browser():
    if browser is not None:
        browser.close()
    if playwright is not None:
        playwright.stop()


def observe_page():
    """Read evidence from the real browser, rather than trusting the model."""
    if page is None:
        return {"url": "", "title": "", "heading": "", "visible_text": ""}

    heading = ""
    if page.locator("h1").count() > 0:
        heading = page.locator("h1").first.inner_text().strip()

    body_text = page.locator("body").inner_text()
    if len(body_text) > 1200:
        body_text = body_text[:1200]

    return {
        "url": page.url,
        "title": page.title(),
        "heading": heading,
        "visible_text": body_text,
    }


def open_site():
    """Open the fixed, fake practice site. There is no arbitrary URL tool."""
    response = page.goto(SITE_URL, wait_until="domcontentloaded")
    if response is not None and not response.ok:
        raise ValueError("Website returned HTTP " + str(response.status))
    return observe_page()


def read_page():
    """Read the current page without changing it."""
    return observe_page()
