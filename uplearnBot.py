from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains


def login():
    usrnme = browser.find_element(By.ID, "input-1")
    pwd = browser.find_element(By.ID, "input-2")
    enterButton = browser.find_element(By.TAG_NAME, "button")

    usrnme.send_keys("fussd001@chartersschool.org.uk")
    pwd.send_keys("uplearnG0ldf!sh")
    enterButton.click()

def answerQuestion(element):
    time.sleep(t)
    Button = browser.find_element(By.XPATH, element)
    browser.execute_script("arguments[0].click();", Button)
    submitButton = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div/div[2]/div[2]/div/button")
    browser.execute_script("arguments[0].click();", submitButton)
    time.sleep(t)
    continueButton = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div/div[2]/div[2]/div/button[2]")
    browser.execute_script("arguments[0].click();", continueButton)

def clickSubmitContinue():
    submitButton = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div/div[2]/div[2]/div/button")
    browser.execute_script("arguments[0].click();", submitButton)
    time.sleep(t)
    continueButton = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div/div[2]/div[2]/div/button[2]")
    browser.execute_script("arguments[0].click();", continueButton)

def returnToQuiz(quizElement):
    time.sleep(t)
    return1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/header/div/span[3]/a")
    browser.execute_script("arguments[0].click();", return1)
    time.sleep(t)
    return2 = browser.find_element(By.XPATH, quizElement)
    browser.execute_script("arguments[0].click();", return2)

def quizBCBC(n):
    time.sleep(t)
    startButton = browser.find_element(By.XPATH, '//button[@class="sc-EElJA sc-eXuhCa jgIuES dpmZGi"]')
    startButton.click()
    for i in range(n):
        time.sleep(t)
        
        bButton = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div/div[2]/div[1]/div[1]/div/section/div/label[2]")
        browser.execute_script("arguments[0].click();", bButton)
        clickSubmitContinue()

        time.sleep(t)
        cButton = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div/div[2]/div[1]/div[1]/div/section/div/label[3]")
        browser.execute_script("arguments[0].click();", cButton)
        
        clickSubmitContinue()
        print("i:", i, n)
    time.sleep(t)
    bButton = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div/div[2]/div[1]/div[1]/div/section/div/label[2]")
    browser.execute_script("arguments[0].click();", bButton)
    clickSubmitContinue()
    returnToQuiz("/html/body/div[1]/div/div/ul/li[17]/a/div")

def quizForcesOnElectrons():
    time.sleep(t)
    startButton = browser.find_element(By.XPATH, '//button[@class="sc-EElJA sc-eXuhCa jgIuES dpmZGi"]')
    startButton.click()
    for i in range(6):
        answerQuestion(forcesOnElectronsAnswers[i])
    returnToQuiz("/html/body/div[1]/div/div/ul/li[4]/a/div/div[1]")
   


forcesOnElectronsAnswers = {0: "/html/body/div[1]/div/div/div/main/div/div[2]/div[1]/div[1]/div/section/div/label[2]/p/span/span",
                            1: "/html/body/div[1]/div/div/div/main/div/div[2]/div[1]/div[1]/div/section/div/label[4]/p/span/span",
                            2: "/html/body/div[1]/div/div/div/main/div/div[2]/div[1]/div[1]/div/section/div/label[3]/p/span/span",
                            3: "/html/body/div[1]/div/div/div/main/div/div[2]/div[1]/div[1]/div/section/div/label[1]/p/span/span",
                            4: "/html/body/div[1]/div/div/div/main/div/div[2]/div[1]/div[1]/div/section/div/label[5]/p/span/span",
                            5: "/html/body/div[1]/div/div/div/main/div/div[2]/div[1]/div[1]/div/section/div/label[4]/p/span/span"}


t=1.5
browser = webdriver.Firefox()
'''
# PHYSICS QUIZ:
browser.get('https://web.uplearn.co.uk/learn/physics-1/kinematics/displacementtime-and-velocitytime-mastery-2-quizzes')
login()
for i in range(100):
    quizBCBC(3)
'''


# CHEM QUIZ:
browser.get("https://web.uplearn.co.uk/learn/chemistry-ocr-2/forces-on-electrons/forces-on-electrons-fluency-quiz-1-quizzes")
login()
quizForcesOnElectrons()