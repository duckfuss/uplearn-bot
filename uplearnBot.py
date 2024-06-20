from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains


browser = webdriver.Firefox()
browser.get('https://web.uplearn.co.uk/learn/physics-1/kinematics/displacementtime-and-velocitytime-mastery-2-quizzes')


usrnme = browser.find_element(By.ID, "input-1")
pwd = browser.find_element(By.ID, "input-2")
enterButton = browser.find_element(By.TAG_NAME, "button")

usrnme.send_keys("fussd001@chartersschool.org.uk")
pwd.send_keys("uplearnG0ldf!sh")

enterButton.click()
browser.get('https://web.uplearn.co.uk/learn/physics-1/kinematics/displacementtime-and-velocitytime-mastery-2-quizzes')
startButton = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div/button")