from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def myPrint(txt):
    print(txt + '\n')

def addScanToMFP(hostMFP, folderName, displayName):
    res = "" # Возвращаемое значение
    driver = webdriver.Chrome('..\\chromedriver.exe')  # driver = webdriver.Firefox()
    driver.get("http://" + hostMFP + ".targin.ru")
    myPrint(driver.title)
    #assert "HP LaserJet 400 MFP M425dn" in driver.title


    def insert_data(html_id, data):
        try:
            the_element = driver.find_element_by_id(html_id)
            the_element.clear()
            the_element.send_keys(data)
        except Exception as Exc:
            myPrint(Exc.args)


    def select_data(html_id, data):
        try:
            sel = Select(driver.find_element_by_id(html_id))
            sel.select_by_value(data)
        except Exception as Exc:
            myPrint(Exc.args)


    try:
        driver.find_element_by_partial_link_text("Сканирование").click()
        driver.find_element_by_id("newButton").click()

        insert_data("displayName", displayName)
        insert_data("networkFolderPath", folderName)
        insert_data("UserName", "targin\\mfu_cheb64")
        insert_data("PassWord", "mfuA12345#")
        select_data("ScanQualitySelection", "DPI_300")
        insert_data("filePrefix", "scan")
        SaveButton = driver.find_element_by_name("SaveTest_button")
        SaveButton.click()


        # driver.implicitly_wait(3)
        # locator = driver.find_element_by_id("testing")
        # myPrint(locator)
        # try:

        # result = WebDriverWait(driver, 30).until_not(EC.text_to_be_present_in_element( (By.ID, "testing"), "connectingboxImage") )
        id_name = 'testing'
        #class_name = 'connectedboxImage'
        connecting_class_name = 'connectingboxImage'

        # Waiting for appearance  the  div id='testing'
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, id_name)))
        myPrint("Появился " + id_name)

        # Waiting for ending of testing
        WebDriverWait(driver, 20).until_not(EC.presence_of_element_located((By.CLASS_NAME, connecting_class_name)))

        result = driver.find_element_by_id(id_name)
        mess = "Add record for scan - " + displayName + " to folder:" + folderName + " on MFP:" + hostMFP
        res += mess +'\n'
        myPrint(mess)
        mess = "Результат = " + result.text
        myPrint("Результат = " + result.text)
        res += mess +'\n'

    except Exception as Exc:
        myPrint("Ошибка")
        myPrint( Exc.args)

    finally:
        # pass
        # except Exception as Exc:
        #    myPrint(Exc.args)
        # driver.close()
        # finally:

        #time.sleep(10)
        myPrint("Закрытие окна.")
        driver.close()
        myPrint("END программы")
        return res

if __name__ == "__main__":
    #host = "02-chb-025"
    #display_name = "Эдуард Аскадуллин test"
    print(" *** ТЕСТОВЫЙ ВЫЗОВ ***")
    comp = "02-araskadullin"
    folder = '\\\\' + comp + '\\scan'
    addScanToMFP(hostMFP = "02-chb-025", folderName = folder, displayName = "TEST Эдуард Аскадуллин" )
