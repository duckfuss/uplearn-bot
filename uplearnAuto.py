#!/opt/homebrew/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
import time



class uplearnLazy():
    def __init__(self) -> None:
        self.options = Options()
        #self.options.add_argument("--headless") # uncomment for headless mode
        self.browser = webdriver.Firefox(options=self.options)
        self.answersDict = {"A": "/html/body/div[1]/div/div/div/main/div/div[2]/div[1]/div[1]/div/section/div/label[1]",
                            "B": "/html/body/div[1]/div/div/div/main/div/div[2]/div[1]/div[1]/div/section/div/label[2]",
                            "C": "/html/body/div[1]/div/div/div/main/div/div[2]/div[1]/div[1]/div/section/div/label[3]",
                            "D": "/html/body/div[1]/div/div/div/main/div/div[2]/div[1]/div[1]/div/section/div/label[4]",
                            "E": "/html/body/div[1]/div/div/div/main/div/div[2]/div[1]/div[1]/div/section/div/label[5]"}
    def login(self):
        usrnme = None
        username = input('what is your username? ')
        password = input('what is your password? ')
        while not usrnme: # wait for page to load
            try:
                usrnme = self.browser.find_element(By.ID, "input-1")
                pwd = self.browser.find_element(By.ID, "input-2")
                enterButton = self.browser.find_element(By.TAG_NAME, "button")
                usrnme.send_keys(username)
                pwd.send_keys(password)
                enterButton.click()
            except NoSuchElementException:
                time.sleep(1)
    def xpathClick(self, path, click=True):
        btn, c = None, 0
        while not btn:
            c+=1
            try:    btn = self.browser.find_element(By.XPATH, path)
            except NoSuchElementException:  time.sleep(0.1)
            if c > 100:
                print("timeout looking for: ", path)
                return btn
        if click:   
            self.browser.execute_script("arguments[0].click();", btn)
        return btn

    def returnToQuiz(self, quizElement):
        self.xpathClick("/html/body/div[1]/div/div/div/header/div/span[3]/a") # return
        self.xpathClick(quizElement)

    def quizController(self, answersList):
        self.xpathClick('/html/body/div[1]/div/div/div/main/div/button') # click start
        for i in range(6):
            self.xpathClick(self.answersDict[answersList[i]]) # click button
            self.xpathClick("/html/body/div[1]/div/div/div/main/div/div[2]/div[2]/div/button") # click submit
            time.sleep(1) # neccesary delay to circumnavigate uplearns spam filters
            self.xpathClick("/html/body/div[1]/div/div/div/main/div/div[2]/div[2]/div/button[2]") # click continue
        

class physicsBot(uplearnLazy):
    def __init__(self) -> None:
        uplearnLazy.__init__(self)
        self.browser.get("https://web.uplearn.co.uk/learn/physics-1/kinematics/displacementtime-and-velocitytime-mastery-2-quizzes")
        self.login()

    def quizKinematics(self):
        self.quizController(["B", "C", "B", "C", "B", "C", "B"])
        self.returnToQuiz("/html/body/div[1]/div/div/ul/li[17]/a/div")


class chemBot(uplearnLazy):
    def __init__(self) -> None:
        uplearnLazy.__init__(self)
        self.browser.get("https://web.uplearn.co.uk/learn/chemistry-ocr-2/forces-on-electrons/forces-on-electrons-fluency-quiz-1-quizzes")
        self.login()

    def quizForcesOnElectrons(self):
        self.quizController(["B", "D", "C", "A", "E", "D"])
        self.returnToQuiz("/html/body/div[1]/div/div/ul/li[4]/a/div/div[1]")



def loopA():
    physDuck = physicsBot()
    count = 0
    initial = time.perf_counter()
    while True:
        tic = time.perf_counter()
        physDuck.quizKinematics()
        count += 1
        tD = time.perf_counter() - tic
        rT = time.strftime("%H:%M:%S", time.gmtime(time.perf_counter() - initial))
        print(count, f"quizes \t in {tD:0.4f} s\t",
              f"{7/tD:0.4f} quiz/s\t", 
              f"{14/tD:0.4f} xp/s\t", 
              f"{(72*(tD))/14:0.4f} s = 1hr\t", # uplearn counts 72 xp as 1hr
              f"{14*count:0.4f} tot xp\t",
              f"{(14*count)/72:0.4f} tot hrs\t"
              f"in", rT)
def loopB():
    chemDuck = chemBot()
    while True:
        chemDuck.quizForcesOnElectrons()

loopA()

'''
Multithreading is possible below, but you must first hardcode the username and
password fields in uplearnLazy, as input() doesn't work with multithreading

from multiprocessing import Process
if __name__ == '__main__':
    #Process(target=loopA).start() # uncomment to run this thread
    Process(target=loopB).start()
'''