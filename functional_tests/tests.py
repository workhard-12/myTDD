from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import WebDriverException
import unittest
import time

MAX_WAIT=10

class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self): 
        self.browser = webdriver.Firefox() 

    def tearDown(self): 
        self.browser.quit() 

    def check_for_row_in_list_table(self, row_text): 
        table = self.browser.find_element_by_id('id_list_table') 
        rows = table.find_elements_by_tag_name('tr') 
        self.assertIn(row_text, [row.text for row in rows]) 

    def wait_for_row_in_list_table(self,row_text):
        start_time=time.time()
        while True:
            try:
                table=self.browser.find_element_by_id('id_list_table')
                rows=table.find_elements_by_tag_name('tr')
                self.assertIn(row_text,[row.text for row in rows])
                return
            except(AssertionError, WebDriverException) as e:
                if time.time() - start_time>MAX_WAIT:
                    raise e
                time.sleep(0.5)

    # def test_can_start_a_list_and_retrieve_it_later(self): 
    #     # 伊迪丝听说有一个很酷的在线待办事项应用 
    #     # 她去看了这个应用的首页 
    #     self.browser.get(self.live_server_url) 
 
    #     # 她注意到网页的标题和头部都包含 “To-Do” 这个词 
    #     self.assertIn('To-Do', self.browser.title) 
    #     header_text = self.browser.find_element_by_tag_name('h1').text 
    #     self.assertIn('To-Do', header_text) 
 
    #     # 应用邀请她输入一个待办事项 
    #     inputbox = self.browser.find_element_by_id('id_new_item') 
    #     self.assertEqual( 
    #             inputbox.get_attribute('placeholder'), 
    #             'Enter a to-do item' 
    #     ) 
 
    #     # 她在一个文本框中输入了 “Buy peacock feathers”（购买孔雀羽毛） 
    #     # 伊迪丝的爱好是使用假蝇做鱼饵钓鱼 
    #     inputbox.send_keys('Buy peacock feathers') 
 
    #     # 她按回车键后， 页面更新了 
    #     # 待办事项表格中显示了 “1: Buy peacock feathers” 
    #     inputbox.send_keys(Keys.ENTER) 
    #     self.wait_for_row_in_list_table('1: Buy peacock feathers')
 
    #     # 页面中又显示了一个文本框， 可以输入其他的待办事项 
    #     # 她输入了 “Use peacock feathers to make a fly”（使用孔雀羽毛做假蝇） 
    #     # 伊迪丝做事很有条理 
    #     inputbox = self.browser.find_element_by_id('id_new_item') 
    #     inputbox.send_keys('Use peacock feathers to make a fly') 
    #     inputbox.send_keys(Keys.ENTER) 

    #     # 页面再次更新， 她的清单中显示了这两个待办事项 
    #     self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly') 
    #     self.wait_for_row_in_list_table('1: Buy peacock feathers') 
       
        
    #     table = self.browser.find_element_by_id('id_list_table') 
    #     rows = table.find_elements_by_tag_name('tr') 
    #     self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
    #     self.assertIn( 
    #         '2: Use peacock feathers to make a fly' , 
    #         [row.text for row in rows] 
    #     ) 
    #     # 页面中又显示了一个文本框， 可以输入其他的待办事项 
    #     # 她输入了 “Use peacock feathers to make a fly”（使用孔雀羽毛做假蝇） 
    #     # 伊迪丝做事很有条理 
    #     self.fail('Finish the test!') 

    def test_can_start_a_list_for_one_user(self):
        # 伊迪丝听说有一个很酷的在线待办事项应用 
        # 她去看了这个应用的首页 
        self.browser.get(self.live_server_url) 
 
        # 她注意到网页的标题和头部都包含 “To-Do” 这个词 
        self.assertIn('To-Do', self.browser.title) 
        header_text = self.browser.find_element_by_tag_name('h1').text 
        self.assertIn('To-Do', header_text) 
 
        # 应用邀请她输入一个待办事项 
        inputbox = self.browser.find_element_by_id('id_new_item') 
        self.assertEqual( 
                inputbox.get_attribute('placeholder'), 
                'Enter a to-do item' 
        ) 
 
        # 她在一个文本框中输入了 “Buy peacock feathers”（购买孔雀羽毛） 
        # 伊迪丝的爱好是使用假蝇做鱼饵钓鱼 
        inputbox.send_keys('Buy peacock feathers') 
 
        # 她按回车键后， 页面更新了 
        # 待办事项表格中显示了 “1: Buy peacock feathers” 
        inputbox.send_keys(Keys.ENTER) 
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
 
        # 页面中又显示了一个文本框， 可以输入其他的待办事项 
        # 她输入了 “Use peacock feathers to make a fly”（使用孔雀羽毛做假蝇） 
        # 伊迪丝做事很有条理 
        inputbox = self.browser.find_element_by_id('id_new_item') 
        inputbox.send_keys('Use peacock feathers to make a fly') 
        inputbox.send_keys(Keys.ENTER) 

        # The page updates again, and now shows both items on her list
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        # Satisfied, she goes back to sleep

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        # She notices that her list has a unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')  
        # Now a new user, Francis, comes along to the site.
        ## We use a new browser session to make sure that no information
        ## of Edith's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()
        # Francis visits the home page.  There is no sign of Edith's
        # list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)
        # Francis starts a new list by entering a new item. He
        # is less interesting than Edith...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)
        # Again, there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)
        # Satisfied, they both go back to sleep

    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        # She notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )
        # She starts a new list and sees the input is nicely
        # centered there too
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

        