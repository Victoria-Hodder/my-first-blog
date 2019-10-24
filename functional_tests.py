from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Victoria' in browser.title

# bug - selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.