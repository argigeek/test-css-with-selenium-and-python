import unittest

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def colors_rgb_to_hex(color_str):
    """
    It converts rgb color to hexagesimal color. Example:

        Input:'rgb(1, 255, 0)'
        Output: '#01ff00'

    Returns a dictionary with both values.
    """
    new_string = color_str[4:-1]
    rgb_list = new_string.split(",")
    rgb_list = list(map(int, rgb_list))

    hex_color = "#%02x%02x%02x" % tuple(rgb_list)

    return {"hex": hex_color, "rgb": color_str}


class UsingUnitTest(unittest.TestCase):

    def setUp(self):
        """
        Add the navigator puppeter. You can find the turorial here:
        https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/

        And the codes for different browsers are here:
        https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/test_install_drivers.py#L15-L17

        Youd should install the navigator if you don't have it:
        the WebDriver is not a replacement.
        """
        self.service = FirefoxService(
            executable_path=GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=self.service)

    def test_search(self):
        """Site title is 'google' and it has a search bar."""
        driver = self.driver
        #driver.get("https://google.com.ar")
        driver.get("http://localhost:3000/")

        # if title has not 'google' substring, the test fails
        self.assertIn("google", driver.title.lower())

        search_bar = driver.find_element(By.CSS_SELECTOR, "[name='q']")
        search_bar.send_keys("hello world")
        search_bar.send_keys(Keys.ENTER)

        driver.implicitly_wait(5)
        # if not found, the test fails
        assert "No se encontró el elemento" not in driver.page_source

    def test_h1_colors_are_well(self):
        driver = self.driver
        driver.get("http://localhost:3000/")
        h1 = driver.find_element(By.TAG_NAME, 'h1')

        expected_colors = {
            "color": "#ffff00",
            "background": "#90ee90",
        }

        css_properties = {"color": "", "background": ""}
        for key in  css_properties:
            value = h1.value_of_css_property(key)
            if key in ["background", "color"]:
                new_value = colors_rgb_to_hex(value)
                css_properties[key] = new_value
            else:
                css_properties[key] = value

        #print(css_properties)
        # Output: 
        # {
        #   'color': {'hex': '#ffff00', 'rgb': 'rgb(255, 255, 0)'},
        #   'background': {'hex': '#90ee90', 'rgb': 'rgb(144, 238, 144)'}
        # }

        text_color = css_properties["color"]["hex"]
        assert expected_colors["color"] == text_color, (
            "Text color is not expected for h1"
        )

        background_color = css_properties["background"]["hex"]
        assert expected_colors["background"] == background_color, (
            "Background color is not expected for h1"
        )

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

