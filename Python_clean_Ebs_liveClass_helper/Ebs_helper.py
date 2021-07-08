from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException, ElementNotSelectableException
import random
import time


def refresh(driver):
    driver.refresh()


def alert_pass(driver):
    """사이트에서 지속적으로 발생하는 오류창을 닫아줍니다.
    Args:
        시스템 오류입니다.
        새로고침 해주시기 바랍니다
        등의 창이 지속적으로 뜨는것을 캔슬하고
        창에 나왔던 텍스트를 리턴합니다.
    """
    try:
        driver.implicitly_wait(5)
        alert = driver.switch_to.alert
        message = alert.text
        print(message)
        alert.dismiss()
        return message
    except NoAlertPresentException:
        return 'no alert'

def login(driver, id, pw):
    try:
        Attending_button = driver.find_element_by_class_name('btn_menu')
        Attending_button.click()
        Attending_button = driver.find_element_by_class_name('btn_login')
        Attending_button.click()
    except:
        try:
            Attending_button = driver.find_element_by_class_name('txt')
            Attending_button.click()
        except:
            print('오류!!!!!!!!!')
        
    """사이트에 로그인합니다.
    Args:
        id (String): 사용자 아이디
        pw (String): 사용자 비밀번호
    """
    driver.find_element_by_class_name('id_input.txt_type').send_keys(id)
    driver.find_element_by_class_name('pw_input.txt_type').send_keys(pw)
    time.sleep(1)
    driver.find_element_by_class_name('img_type').click()
    alert_pass(driver)