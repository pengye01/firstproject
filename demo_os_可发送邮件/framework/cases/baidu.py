from  selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys
from  selenium.webdriver.support.ui import Select
from  selenium.common.exceptions import NoSuchElementException
import  unittest,re,time
from ddt import ddt,data,unpack
from castro import  Castro
@ddt
class Baidu(unittest.TestCase):
    def setUp(self):

        self.screenCaoture=Castro(filename='testbadidu.swf')
        self.screenCaoture.start()
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url='https://www.baidu.com/'
        self.verificationErrors = []
        self.accept_net_alert=True
    @ data(('selenium',),('appuim',))
    @unpack
    def test_baidu(self,keyw):
        """百度搜索{0}""".format(keyw)
        driver=self.driver
        driver.get(self.base_url)

        driver.find_element_by_id("kw").send_keys(keyw)
        time.sleep(0.5)
        # print(self.driver.title)
        driver.get_screenshot_as_base64()
        # driver.get_screenshot_as_file('selenium0.png')
        driver.find_element_by_id("su").click()
        time.sleep(1)
        driver.get_screenshot_as_base64()

        # driver.get_screenshot_as_file('selenium.png')
        driver.close()
    # 百度社设置用例
    def test_baidu_set(self):
        """百度设置"""
        driver=self.driver
        #进入搜索设置页
        driver.get(self.base_url+"gaoji/preferences.html")
        # 设置每页搜索结果为100条
        # //*[@id="restore"]
        time.sleep(0.5)
        driver.find_element_by_id("restore")
        driver.get_screenshot_as_file('restore.png')

        m =driver.find_element_by_name("NR")
        time.sleep(1)
        # driver.get_screenshot_as_file('NR.png')
        driver.get_screenshot_as_base64()

        m.find_element_by_xpath("//option[@value='20']").click()
        # driver.get_screenshot_as_file('value.png')
        driver.get_screenshot_as_base64()

        time.sleep(1)
        # 保存设置的信息
        driver.find_element_by_xpath("/html/body/form/div/input").click()
        time.sleep(0.1)
        # driver.get_screenshot_as_file('input0.png')
        # driver.get_screenshot_as_file('input.png')
        # self.close_alert_get_its_text()
        # alert=driver.switch_to_alert().accept()
        # alert_text = alert.text
        # print(alert_text)
    def is_element_present(self,how,what):
        try:self.driver.find_element(by=how,value=what)
        except NoSuchElementException as e:return False
        return  True
    def is_alert_paresent(self):
        try: self.driver.switch_to_alert()
        except NoSuchElementException as e: return  False
        return  True
    def close_alert_get_its_text(self):
        try:
            alert=self.driver.switch_to_alert()
            alert_text=alert.text
            if self.accept_net_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_net_alert=True
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)
        self.screenCaoture.stop()
if __name__ == '__main__':
    unittest.main()