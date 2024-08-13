#******************************************************************************
#
# Copyright (c) 2016 Microsoft Corporation. All rights reserved.
#
# This code is licensed under the MIT License (MIT).
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# // LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
#******************************************************************************


import unittest
from appium import webdriver
from appium.options.windows import WindowsOptions
from appium.webdriver.common.appiumby import AppiumBy as By

class SimpleCalculatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # set up appium
        desired_caps = {"app": "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"}
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            options=WindowsOptions().load_capabilities(desired_caps))

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def getresults(self):
        displaytext = self.driver.find_element(By.ACCESSIBILITY_ID, "CalculatorResults").text
        displaytext = displaytext.strip()
        # Takes the last space character and deletes whole "Display is " text, more localization-compatible
        displaytext = displaytext[displaytext.rindex(' ')+1::]
        return displaytext

    def test_initialize(self):
        self.driver.find_element(By.ACCESSIBILITY_ID, "clearButton").click()
        self.driver.find_element(By.ACCESSIBILITY_ID, "num7Button").click()
        self.assertEqual(self.getresults(), "7")
        self.driver.find_element(By.ACCESSIBILITY_ID, "clearButton").click()

    def test_addition(self):
        self.driver.find_element(By.ACCESSIBILITY_ID, "num1Button").click()
        self.driver.find_element(By.ACCESSIBILITY_ID, "plusButton").click()
        self.driver.find_element(By.ACCESSIBILITY_ID, "num7Button").click()
        self.driver.find_element(By.ACCESSIBILITY_ID, "equalButton").click()
        self.assertEqual(self.getresults(), "8")

    def test_combination(self):
        self.driver.find_element(By.ACCESSIBILITY_ID, "num7Button").click()
        self.driver.find_element(By.ACCESSIBILITY_ID, "multiplyButton").click()
        self.driver.find_element(By.ACCESSIBILITY_ID, "num9Button").click()
        self.driver.find_element(By.ACCESSIBILITY_ID, "plusButton").click()
        self.driver.find_element(By.ACCESSIBILITY_ID, "num1Button").click()
        self.driver.find_element(By.ACCESSIBILITY_ID, "equalButton").click()
        self.driver.find_element(By.ACCESSIBILITY_ID, "divideButton").click()
        self.driver.find_element(By.ACCESSIBILITY_ID, "num8Button").click()
        self.driver.find_element(By.ACCESSIBILITY_ID, "equalButton").click()
        self.assertEqual(self.getresults(), "8")

    def test_division(self):
        self.driver.find_element(By.ACCESSIBILITY_ID, "num8Button").click()
        self.driver.find_element(By.ACCESSIBILITY_ID, "num8Button").click()
        self.driver.find_element(By.ACCESSIBILITY_ID, "divideButton").click()
        self.driver.find_element(By.ACCESSIBILITY_ID, "num1Button").click()
        self.driver.find_element(By.ACCESSIBILITY_ID, "num1Button").click()
        self.driver.find_element(By.ACCESSIBILITY_ID, "equalButton").click()
        self.assertEqual(self.getresults(), "8")

    def test_multiplication(self):
        self.driver.find_element(By.ACCESSIBILITY_ID, "num9Button").click()
        self.driver.find_element(By.ACCESSIBILITY_ID, "multiplyButton").click()
        self.driver.find_element(By.ACCESSIBILITY_ID, "num9Button").click()
        self.driver.find_element(By.ACCESSIBILITY_ID, "equalButton").click()
        self.assertEqual(self.getresults(), "81")

    def test_subtraction(self):
        self.driver.find_element(by=By.ACCESSIBILITY_ID, value="num9Button").click()
        self.driver.find_element(By.ACCESSIBILITY_ID,  "minusButton").click()
        self.driver.find_element(By.ACCESSIBILITY_ID,  "num1Button").click()
        self.driver.find_element(By.ACCESSIBILITY_ID, "equalButton").click()
        self.assertEqual(self.getresults(),"8")
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleCalculatorTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
