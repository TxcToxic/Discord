from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import json
import sys

os.system("title Selenium Console   Program by -TOXIC-#1835")


def sPrint(str):
    for l in str:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(.1)
    sys.stdout.write("\n")


def checkForDriver():
    if os.path.exists("./bin/chromedriver.exe"):
        print("Chromedriver exists...")
        pass
    else:
        print("Chromedriver does not exist!\n"
              "INSTALL https://chromedriver.storage.googleapis.com/index.html?path=105.0.5195.52/")
        while True:
            sys.stdout.write("!")
            sys.stdout.flush()
            time.sleep(1)


def checkForConfig():
    if os.path.exists("./bin/config.json"):
        print("Config exists...")
    else:
        data = {
            "token": "TOKEN",
            "email": "E-MAIL-ADDRESS",
            "password": "PASSWORD",
            "useToken": 0,
            "_c": "0 = use email & password | 1 = use token"
        }
        open("./bin/config.json", "w").write(json.dumps(data, indent=4))
        print("Config file created...")
        quit()


print("checking for requires...")
time.sleep(2)
if os.path.exists("./bin"):
    print("Bin folder exists...")
    time.sleep(1.5)
    checkForDriver()
    time.sleep(1.5)
    checkForConfig()
    time.sleep(1.5)
    sPrint("Everything is great program will launch in 5 seconds...")
    time.sleep(5)
    os.system("cls")
else:
    os.mkdir("./bin")
    print("Bin folder created...")
    data = {
        "token": "TOKEN",
        "email": "E-MAIL-ADDRESS",
        "password": "PASSWORD",
        "useToken": 0,
        "_c": "0 = use email & password | 1 = use token"
    }
    open("./bin/config.json", "w").write(json.dumps(data, indent=4))
    print("Config file created...")
    quit()

with open("./bin/config.json", "r") as file:
    tf = json.load(file)
useToken = tf["useToken"]
loadingTimeout = 3
PATH = "./bin/chromedriver.exe"
if useToken == 0:
    email = tf["email"]
    password = tf["password"]
    driver = webdriver.Chrome(PATH)
    driver.set_window_size(height=1000, width=1000)
    driver.get("https://discord.com/login/")
    time.sleep(loadingTimeout)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input').send_keys(email)
    time.sleep(1.8)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input').send_keys(password)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "button-1cRKG6").click()
    os.system("cls")
elif useToken == 1:
    token = tf["token"]
    driver = webdriver.Chrome(PATH)
    driver.set_window_size(height=1000, width=1000)
    driver.get("https://discord.com/login/")
    time.sleep(loadingTimeout)
    js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
    driver.execute_script(js + f'login("{token}")')
    os.system("cls")
else:
    os.system("cls")
    sPrint("Unkown login method | break in 5 seconds...")
    time.sleep(5)
    quit()
