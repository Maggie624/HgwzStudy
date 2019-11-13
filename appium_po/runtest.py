import pytest
import os

if __name__ == "__main__":
    pytest.main(['-s', '-q', '--alluredir', 'report/xml', 'testcase/'])
    os.system("/Users/maoqi/Public/tools/allure-2.7.0/bin/allure "
              "generate --clean "
              "/Users/maoqi/Projects/PycharmProjects/hgwz/appium_po/report/xml "
              "-o "
              "/Users/maoqi/Projects/PycharmProjects/hgwz/appium_po/report/html")