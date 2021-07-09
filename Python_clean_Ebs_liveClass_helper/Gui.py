from tkinter import *
from selenium import webdriver
from tkinter import messagebox as msgbox
import os
import chromedriver_autoinstaller
import Python_clean_Ebs_liveClass_helper
import threading
import winsound as sd 
import time


root = Tk()
chromedriver_autoinstaller.install(True)
driver = webdriver.Chrome()
main = Python_clean_Ebs_liveClass_helper.MAIN_WORK_PLACE(driver, root)


root.title("라이브 수업 대기 장치")
root.iconbitmap('MO-supp-E.ico')
root.geometry("300x100")
root.resizable(False, False)

variable = StringVar()
variable.set("수업")

#--------------------------------------------------------------------좌하단 고정

def stop():
    driver.quit()
    root.quit()
    print("프로그램이 종료 되었습니다.")
    return 0

def get_id():
    msgbox.showinfo("알림","아이디 변경은 ID.txt파일을 통해 해주시기 바랍니다.")

#--------------------------------------------------------------------첫번째 화면

def bt1_fuction():
    threading.Thread(target=main.Work).start()
    e.pack()
    button.pack()
    button1.pack()
    btn1.pack_forget()
    get_idButton.pack_forget()

#--------------------------------------------------------------------두번째 화면
def get_url(url):
    main.task_kill = False
    print(url)
    threading.Thread(target=lambda:main.go_want_site(url)).start()

def e_function():
    # readOnlyText.pack()
    button.pack_forget()
    button1.pack_forget()
    e.pack_forget()
    url = e.get()
    get_url(url)
    button2.pack()
    button3.pack()

def ThisTab_function():
    button.pack_forget()
    button1.pack_forget()
    e.pack_forget()
    url = driver.current_url
    get_url(url)
    button2.pack()
    button3.pack()
    
#--------------------------------------------------------------------세번째 화면

def Refind():
    main.task_kill = True
    time.sleep(1)
    main.task_kill = False
    threading.Thread(target=lambda:main.Main_finder()).start()

def Restart_th():
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    driver.get('https://sel3.ebsoc.co.kr/class')
    return 0

def Restart():
    main.task_kill = True
    e.pack()
    button.pack()
    button1.pack()
    button2.pack_forget()
    button3.pack_forget()
    threading.Thread(target=lambda:Restart_th()).start()

#--------------------------------------------------------------------

#--------------------------------------------------------------------좌하단 고정

stopButton = Button(root, text = '프로그램 종료', command=stop)
stopButton.pack(side="right", anchor="s")

get_idButton = Button(root, text = '아이디 변경', command=get_id)
get_idButton.pack(side="bottom", anchor="e")

#--------------------------------------------------------------------첫번째 화면

btn1 = Button(root, text="로그인", command=bt1_fuction)
btn1.pack()

#--------------------------------------------------------------------두번째 화면

e = Entry(root, width = 30, bg = 'light blue')
e.insert(0,"링크를 입력해주세요")
button = Button(root, text = '입력한 링크에서 자동 대기', command=e_function)
button1 = Button(root, text = '또는 현재 탭에서 자동 대기', command=ThisTab_function)

#--------------------------------------------------------------------세번째 화면

button2 = Button(root, text = "목록으로 가기", command=Restart)
button3 = Button(root, text = "탐색 다시 시작(탐색이 중지됐으면)", command=Refind)

root.mainloop()