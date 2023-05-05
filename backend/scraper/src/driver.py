import seleniumwire.undetected_chromedriver.v2 as uc
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_driver(proxy: str) -> uc:
    options = uc.ChromeOptions()
    options.headless = True
    options.add_argument('--disable-notifications')
    options.add_argument('--incognito')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--mute-audio')
    options.add_argument('--disable-setuid-sandbox')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-web-security')

    proxy_options = {
        'proxy': {
            'http': proxy,
            'https': proxy,
        }
    }
    service = Service(ChromeDriverManager().install())
    return uc.Chrome(service=service, options=options, seleniumwire_options=proxy_options, use_subprocess=True)
