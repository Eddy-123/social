from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online blog app.
        # She goes to check out its homepage
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mentions blog
        self.assertIn("blog", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("My blog", header_text)

        # She clicks on the first article to view it's details
        first_h2 = self.browser.find_element(By.TAG_NAME, "h2")
        link = first_h2.find_element(By.TAG_NAME, "a")
        time.sleep(2)
        link.click()
        time.sleep(2)

        # She is invited to comment the first item
        # She enters her name
        name_box = self.browser.find_element(By.ID, "id_name")
        self.assertEqual(name_box.get_attribute("name"), "name")
        self.browser.execute_script("arguments[0].scrollIntoView();", name_box)
        name_box.send_keys("Edith")
        time.sleep(2)

        # She enters her email
        email_box = self.browser.find_element(By.ID, "id_email")
        self.assertEqual(email_box.get_attribute("name"), "email")
        self.browser.execute_script("arguments[0].scrollIntoView();", email_box)
        email_box.send_keys("edith@gmail.com")
        time.sleep(2)

        # She enters her comment
        body_box = self.browser.find_element(By.ID, "id_body")
        self.assertEqual(body_box.get_attribute("name"), "body")
        self.browser.execute_script("arguments[0].scrollIntoView();", body_box)
        body_box.send_keys("Alright !")
        time.sleep(2)

        # She submits her comment
        submit_button = self.browser.find_element(By.XPATH, "//input[@type='submit']")
        submit_button.click()
        time.sleep(2)

        # She goes back to the post
        link = self.browser.find_element(By.TAG_NAME, "a")
        link.click()
        time.sleep(2)

        # Edith checks that her comment appears on the post
        paragraphs = self.browser.find_elements(By.TAG_NAME, "p")
        self.assertTrue(any(paragraph.text == "Alright !" for paragraph in paragraphs))

        self.fail("Finish the test !")
        # She types "Buy peacock feathers" into a text box

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a post list

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly"

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list.
        # Then she sees that the site has generated a unique URL for her --
        # There is some explanatory text to that effect.

        # She visits that URL - her post list is still there.

        # Satisfied, she goes back to sleep


if __name__ == "__main__":
    unittest.main(warnings="ignore")
