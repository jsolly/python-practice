### Select element based on text
"""
el = driver.find_element_by_xpath("//*[text()='Exact Match']")
el = driver.find_element_by_xpath("//*[contains(text(), 'Partial Match')]")

# This one seems to work better since it looks at inner nodes
        self.driver.find_element_by_xpath(
            ".//p[text() [contains(.,'cannot be found')]]"
        )

loginButton = browser.find_element(By.XPATH, "//*[@value='Log In']")


self.assertTrue(
                "You do not have permissions"
                in self.driver.find_elements_by_tag_name("p")[1].text
            )
"""
