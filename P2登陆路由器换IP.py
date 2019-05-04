import time
from selenium import webdriver

def reconn(url):
    bs = webdriver.Firefox(executable_path = 'geckodriver.exe')
    bs.get(url)
    time.sleep(1)
    bs.find_element_by_name("Disconnect").click()
    time.sleep(1)
    al=bs.switch_to.alert
    al.accept()
    time.sleep(5)
    bs.find_element_by_name("Connect").click()
    time.sleep(2)
    bs.quit()
    return 1


if __name__ == '__main__':
    url=u'http://admin:password@192.168.1.1/RST_st_poe.htm'
    try:
        a=reconn(url)
        print(str(a))
    except Exception as err:
        print(err)

