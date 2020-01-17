#!/usr/local/bin/python3
from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytesseract
# Defino la URL-principal y la ruta al driver de chrome
main_url = 'http://158.69.76.135/level3.php' # URL principal
chromedriver = './chromedriver'
# Abrimos una ventana con la URL-principal
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
)
for i in range(1024):
    browser = webdriver.PhantomJS(executable_path='/Users/holberton/hodor/level_3/phantomjs-2.1.1-macosx/bin/phantomjs', desired_capabilities=dcap)
    browser.get(main_url)
    browser.save_screenshot('screen.png')
    captcha = Image.open('screen.png')
    left = 0
    top = 695
    right = 65
    bottom = 726
    captcha1 = captcha.crop((left, top, right, bottom))
    captcha1.save("captcha.png")
    text = pytesseract.image_to_string(Image.open('captcha.png'))
    formulario = browser.find_element_by_name('id')
    captchafield = browser.find_element_by_name('captcha')
    submit = browser.find_element_by_name('holdthedoor')
    formulario.send_keys('1160')
    captchafield.send_keys(text)
    submit.click()
    browser.close()
