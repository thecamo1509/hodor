#!/usr/local/bin/python3
from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pytesseract
import time
# Definimos la URL-principal y la ruta al driver de chrome
main_url = 'http://158.69.76.135/level3.php' # URL principal
chromedriver = './chromedriver'
# Abrimos una ventana con la URL-principal
#browser = webdriver.PhantomJS(executable_path='/Users/holberton/hodor/level_3/phantomjs-2.1.1-macosx/bin/phantomjs')
browser = webdriver.Chrome(executable_path='/Users/holberton/hodor/level_3/chromedriver')
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
print(text)
formulario = browser.find_element_by_name('id')
captchafield = browser.find_element_by_name('captcha')
submit = browser.find_element_by_name('holdthedoor')
formulario.send_keys('1')
captchafield.send_keys(text)
submit.click()
browser.close()
