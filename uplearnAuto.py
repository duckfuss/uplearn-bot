from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from multiprocessing import Process

class uplearnLazy():
    def __init__(self) -> None:
        self.browser = webdriver.Firefox()
    def login(self):
        usrnme = None
        while not usrnme:
            try:
                usrnme = self.browser.find_element(By.ID, "input-1")
                pwd = self.browser.find_element(By.ID, "input-2")
                enterButton = self.browser.find_element(By.TAG_NAME, "button")
                usrnme.send_keys("fussd001@chartersschool.org.uk")
                pwd.send_keys("uplearnG0ldf!sh")
                enterButton.click()
            except NoSuchElementException:
                time.sleep(1)
    def answerQuestion(self, element):
        Button = self.browser.find_element(By.XPATH, element)
        self.browser.execute_script("arguments[0].click();", Button)
        submitButton = self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div/div[2]/div[2]/div/button")
        self.browser.execute_script("arguments[0].click();", submitButton)
        time.sleep(1.1)
        continueButton = None
        while not continueButton:
            try:
                continueButton = self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div/div[2]/div[2]/div/button[2]")
            except NoSuchElementException:
                time.sleep(0.1)
                print("waited")
        self.browser.execute_script("arguments[0].click();", continueButton)
    def returnToQuiz(self, quizElement):
        return1, return2 = None, None
        while not return1:
            try:
                return1 = self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/header/div/span[3]/a")
            except NoSuchElementException:
                time.sleep(0.2)
        self.browser.execute_script("arguments[0].click();", return1)
        while not return2:
            try:
                return2 = self.browser.find_element(By.XPATH, quizElement)
            except NoSuchElementException:
                time.sleep(0.2)
        self.browser.execute_script("arguments[0].click();", return2)

class physicsBot(uplearnLazy):
    def __init__(self) -> None:
        uplearnLazy.__init__(self)
        self.browser.get("https://web.uplearn.co.uk/learn/physics-1/kinematics/displacementtime-and-velocitytime-mastery-2-quizzes")
        self.login()
        self.answers = {"B":"/html/body/div[1]/div/div/div/main/div/div[2]/div[1]/div[1]/div/section/div/label[2]",
                        "C":"/html/body/div[1]/div/div/div/main/div/div[2]/div[1]/div[1]/div/section/div/label[3]"}
    def quizKinematics(self):
        time.sleep(0.5)
        startButton = None
        while not startButton:
            try:
                startButton = self.browser.find_element(By.XPATH, '//button[@class="sc-EElJA sc-eXuhCa jgIuES dpmZGi"]')
                startButton.click()
            except NoSuchElementException: 
                time.sleep(0.5)
        for i in range(3):
            self.answerQuestion(self.answers["B"])
            self.answerQuestion(self.answers["C"])
        self.answerQuestion(self.answers["B"])
        self.returnToQuiz("/html/body/div[1]/div/div/ul/li[17]/a/div")

class chemBot(uplearnLazy):
    def __init__(self) -> None:
        uplearnLazy.__init__(self)
        self.browser.get("https://web.uplearn.co.uk/learn/chemistry-ocr-2/forces-on-electrons/forces-on-electrons-fluency-quiz-1-quizzes")
        self.login()
        self.forcesOnElectronsAnswers = {0: "/html/body/div[1]/div/div/div/main/div/div[2]/div[1]/div[1]/div/section/div/label[2]/p/span/span",
                        1: "/html/body/div[1]/div/div/div/main/div/div[2]/div[1]/div[1]/div/section/div/label[4]/p/span/span",
                        2: "/html/body/div[1]/div/div/div/main/div/div[2]/div[1]/div[1]/div/section/div/label[3]/p/span/span",
                        3: "/html/body/div[1]/div/div/div/main/div/div[2]/div[1]/div[1]/div/section/div/label[1]/p/span/span",
                        4: "/html/body/div[1]/div/div/div/main/div/div[2]/div[1]/div[1]/div/section/div/label[5]/p/span/span",
                        5: "/html/body/div[1]/div/div/div/main/div/div[2]/div[1]/div[1]/div/section/div/label[4]/p/span/span"}
    def quizForcesOnElectrons(self):
        time.sleep(0.5)
        startButton = None
        while not startButton:
            try:
                startButton = self.browser.find_element(By.XPATH, '//button[@class="sc-EElJA sc-eXuhCa jgIuES dpmZGi"]')
                startButton.click()
            except NoSuchElementException: 
                time.sleep(0.5)
        for i in range(6):
            self.answerQuestion(self.forcesOnElectronsAnswers[i])
        self.returnToQuiz("/html/body/div[1]/div/div/ul/li[4]/a/div/div[1]")

def loopA():
    physDuck = physicsBot()
    while True:
        physDuck.quizKinematics()
def loopB():
    chemDuck = chemBot()
    while True:
        chemDuck.quizForcesOnElectrons()

if __name__ == '__main__':
    Process(target=loopA).start()
    #Process(target=loopB).start()