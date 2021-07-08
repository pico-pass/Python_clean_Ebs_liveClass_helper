from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException, ElementNotSelectableException
import time

class Live:
    paragraph = 1
    def __init__(self, driver):
        self.driver = driver

    def alert_return(self):
        """사이트에서 지속적으로 발생하는 오류창을 닫아줍니다.

        Args:
            시스템 오류입니다.
            새로고침 해주시기 바랍니다
            등의 창이 지속적으로 뜨는것을 캔슬하고
            창에 나왔던 텍스트를 리턴합니다.
        """
        try:
            alert = self.driver.switch_to.alert
            message = alert.text
            print(message)
            alert.dismiss()
            return message
        except NoAlertPresentException:
            return 'no alert'

    def alert_pass(self):
        while True:
            self.driver.implicitly_wait(5)
            time.sleep(1)
            err = self.alert_return()
            #print(err)
            #if err.find('새로고침') > 0:
             #   self.alert_return()
              #  print('refresh')
               # self.driver.refresh()
            if err == 'no alert':
                break

    def Check_Condition(self):
        """만약 클릭한 대상이 사용자가 해당하는 화상수업이 아니라면 다음 버튼을 클릭합니다.

        Args:
            해당 화상수업 학생이 아니라는 알림이 나온다면
            pargraph 값을 추가해 다음 버튼을 클릭합니다.
        """
        if self.alert_return()=='해당 화상수업 학생이 아닙니다.':
            # self.paragraph +=1 안정성을 위해 함수를 비활성화 함
            return False
        else:
            return True
            
    def Check_live_class_Tab(self):
        """수업 대기 창으로 전환이 되었는지 확인합니다.

        Args:
            만약 url 창에 meeting이라는 단어가 감지되면 True를 그게 아니라면 False를 리턴합니다.
            수업이 끝나면 https://ebs3-meeting.dooray.com/onclass/thank-you라는 주소로 가게 되는데
            수업이 끝난 창은 이를 이용하여 구분을 할수있도록 url.find('thank-you') == '-1'를 사용하였습니다
        """
        Stop = False

        for i in range(0, len(self.driver.window_handles)):
            self.alert_pass()
            self.driver.switch_to.window(self.driver.window_handles[i])
            self.driver.implicitly_wait(5)
            url = self.driver.current_url
            if (url.find('meeting') > 0) and (str(url.find('thank-you')) == '-1'):
                Stop = True
                
        if Stop == False:
            self.driver.switch_to.window(self.driver.window_handles[0])
        return Stop
    
    def finder(self, target):
        """수업이 열렸는지를 확인하고 열렸다면 버튼을 클릭합니다.

        Args:
            try로 버튼요소의 유무를 확인하고 Check_Condition()를 이용해 메세지를 분석 할 수 있습니다.
        """
        self.alert_pass() 
        try:
            target = self.driver.find_element_by_css_selector(target)
            target.click()
        except NoSuchElementException:
            print('NoSuchElement')
        except AttributeError:
            print('Timeout')
            pass
        self.Check_Condition()