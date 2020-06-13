
import unittest,sys
from  selenium import  webdriver
from time import  sleep
from bs4 import  BeautifulSoup
from  selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import  WebDriverWait
from  selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions

class Find_Element(unittest.TestCase):
    # self.BROWSER=BROWSER

    def setUp(self):
        # desired_caps={}
        # desired_caps['platfrom']='WINDOWS'
        # desired_caps['browserName']='internet explorer'
        self.driver=webdriver.Chrome()
        # self.driver=webdriver.Remote('http://192.168.1.101:5555/wd/hub',desired_caps)
        self.driver.maximize_window()
        url='https://lady.vip.com/'
        self.driver.get(url)

    def test02(self):
        a_content=self.driver.find_element_by_class_name('c-page').find_element_by_class_name('main-nav').\
            find_elements_by_tag_name('a')
        # for content in a_content:
        #     print(content.text)

        pagesoures = self.driver.page_source
        soup = BeautifulSoup(pagesoures)
        title_text=soup.title.string
        # content = self.driver.find_element_by_tag_name('head').find_element_by_tag_name('title').text
        print(title_text)

    def test03(self):
        search=self.driver.find_element_by_class_name('c-page-header').\
            find_element_by_class_name('head-logo').\
            find_element_by_class_name('c-search-form')
        search.find_element_by_class_name('J-search-input').send_keys('连衣裙')
        sleep(2)
        cl=WebDriverWait(search,10).until(expected_conditions.
            visibility_of_element_located((By.CSS_SELECTOR,"a[mars_sead=search_button]")))
        cl.click()
        # search.find_element_by_css_selector('a[mars_sead=search_button]').click()
        sleep(10)
        pagesoures = self.driver.page_source
        soup = BeautifulSoup(pagesoures)
        title_text = soup.title.string
        # content = self.driver.find_element_by_tag_name('head').find_element_by_tag_name('title').text
        print(title_text)

    def  test04(self):
        # id="vip-common-header"

        self.driver.find_element_by_id("vip-common-header").\
            find_element_by_class_name("main-nav").find_element_by_link_text('最后疯抢').click()
        windows=self.driver.window_handles
        print(windows)
        self.driver.switch_to_window(windows[-1])
        pagesoures = self.driver.page_source

        soup = BeautifulSoup(pagesoures)
        title_text = soup.title.string
        print(title_text)
        content=self.driver.find_element_by_id('specialContent').find_element_by_class_name('container-wrapper')\
            .find_element_by_class_name('lightart-wrap-box  ')
        contenttext=content.find_elements_by_css_selector('span.ltart-label-inner')
        for tent in contenttext:
            print(tent.text)
        # print(contenttext)
         # 鼠标事件
        """
         ActionChains类鼠标操作的常用方法
         context_click() 右击
          double_click() 双击 
           drag_and_drop() 拖动
           move_to_element() 鼠标悬停在一个元素上 
           click_and_hold() 按下鼠标左键在一个元素上

        """
    def test05(self):
            # id="vip-common-header"
            # id = "J_main_nav"
            # class="head-inner"
            # id="J_main_nav_link"
            # id="J_main_nav_category"
            # 商品分类
        category= self.driver.find_element_by_id("vip-common-header").\
            find_element_by_id("J_main_nav").find_element_by_class_name("head-inner").\
            find_element_by_id("J_main_nav_link").\
            find_element_by_id("J_main_nav_category").find_element_by_css_selector('a.main-nav-atag ')
        print(category.text)
        sleep(2)
        l=ActionChains(self.driver).move_to_element(category).perform()
        pagesoures = self.driver.page_source

        # print(pagesoures)
        # #

        #     J_main_nav_category_data
        #     id="J_main_nav_category_menu"
        #     class ="cate-menu-item J_main_nav_category_menu_item"
        content=self.driver.find_element_by_id("J_main_nav_category_data").find_element_by_id('J_main_nav_category_menu').\
            find_elements_by_css_selector('li.J_main_nav_category_menu_item')
        sleep(3)
        # print(content)
        print(self.driver.get_cookies())
        count=0
        for item in content:
            ActionChains(self.driver).move_to_element(item).perform()
            sleep(1)
            # print(item.text)
            item_text= item.text
            item_text=item_text.replace("/","_")
            # self.driver.get_screenshot_as_file("{0}.png".format(count))
            self.driver.get_screenshot_as_file("{0}{1}.png".format(count,item_text))
            sleep(1)
            count += 1
            # J_main_nav_category_pop
            # pagesoures = self.driver.page_source
            # soup = BeautifulSoup(pagesoures)
            # content=soup.find("div",id="J_main_nav_category_pop")
            # # sleep(3)
            # print("<","="*30)
            # print(content)
            # print(item.text)
            # # l=item.text



if __name__=='__mian__':
    # if len(sys.argv)>1:
    #     BROWSER=sys.argv.pop()
    #     PLATFROM=sys.argv.pop()
    unittest.main()
