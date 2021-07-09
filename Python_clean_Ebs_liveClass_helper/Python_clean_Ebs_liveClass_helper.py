from Ebs_helper import *
from os_manage import *
from Find_live_class_helper import *
from tkinter import *
from tkinter import messagebox as msgbox
from selenium import webdriver
import Find_live_class_helper
import tkinter.ttk as ttk
import threading
import chromedriver_autoinstaller
import random
import time



class MAIN_WORK_PLACE:
    task_kill = False #외부에서 Main_finder()를 끄는데 사용
    

    def __init__(self, driver, root):
        self.driver = driver
        self.root = root

    """각각 id와 pw를 읽음
        """
    def read_id(self):
        line = read_FILE()
        print(line)
        if str(line[0]) == "FINE":
            return line[1]
        else:
            return "Err"

    def read_pw(self):
        line = read_FILE()
        print(line)
        if str(line[0]) == "FINE":
            return line[2]
        else:
            return "Err"
        
    


    def Work(self):
#        beepsound()
         
        """로그인을 하고 클래스 목록으로 들어갑니다.

        Args:
            min = random.randrange(2000, 5000)
            time.sleep(min/1000)를 사용하는 이유는
            1초 미만의 간격을 주고 이부분을 들어갈경우 ebs에서 특정 사이트로 리디렉션을 하기 때문입니다.
        """
  
        alert_pass(self.driver)
        self.driver.get('https://www.ebsoc.co.kr/')
        alert_pass(self.driver)
        self.driver.implicitly_wait(5)
        alert_pass(self.driver)

        alert_pass(self.driver)
        id = self.read_id()
        print(f"입력 받은 id:{id}")
        pw = self.read_pw()
        print(f"입력 받은 pw:{pw}")
        login(self.driver, id, pw)
        self.driver.implicitly_wait(5)
        min = random.randrange(2000, 5000)
        time.sleep(min/1000)

        alert_pass(self.driver)
        self.driver.get('https://sel3.ebsoc.co.kr/class')
        alert_pass(self.driver)
        

       


    def go_want_site(self, url):
        """사용자가 원하는 클래스로 들어갑니다.

        Args:
            Main_finder를 별도로 분리해서 호출하는 이유는 Main_finder함수를 별도로 다시 사용해야 할경우가 생길수 있기 때문입니다.
            (Gui.py Refind()참고)
        """
        #print("hello")
        print(url)
        self.driver.get(str(url))
        time.sleep(1)
        alert_pass(self.driver)
        refresh(self.driver)
        self.Main_finder()


    def Main_finder(self):
        """클래스가 열렸는지 확인합니다.
            
        """


        live_Down = Find_live_class_helper.Live(self.driver)
        live_Up = Find_live_class_helper.Live(self.driver)
        # live_LookUp = Find_live_class_helper.Live(self.driver) #Look up: 조회
        while True:

            alert_pass(self.driver)
            Down = '#page > div.page_classmain > div:nth-child(2) > div:nth-child(2) > div > ul > li:nth-child('+str(live_Down.paragraph)+') > a'
            Up = '#page > div.page_classmain > div:nth-child(1) > div:nth-child(2) > div > ul > li:nth-child('+str(live_Up.paragraph)+') > a'
            Look_UP = '#page > div.bg_main_tit > div > div.fr > div > a.btn.btn_md.btn.btn_keycolor'
    
            print("온클 라이브 일정을 탐색하는중....")

            if live_Up.Check_live_class_Tab() == True:
                break
            elif self.task_kill == True:
                return 0
            live_Up.finder(Up)

            print("화상수업 안내를 탐색하는중....")

            if live_Down.Check_live_class_Tab() == True:
                break
            elif self.task_kill == True:
                return 0
            live_Down.finder(Down)
            # print(live_Down.paragraph)

        #    print("종례를 탐색하는중....")
        #    if live_Down.Check_live_class_Tab() == True:
        #        break
        #    elif self.task_kill == True:
        #        return 0
        #    live_LookUp.finder(Look_UP)
        #    
        # 주석을 풀경우 조회도 탐색 가능
            alert_pass(self.driver)
    
            refresh(self.driver)
        beepsound(2)
        msgbox.showinfo("알림!","클래스가 열렸습니다!")