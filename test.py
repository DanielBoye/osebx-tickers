from selenium import webdriver
from selenium.webdriver.common.by import By

tickers = ["AEGA", "AGLX", "AIRX", "AKAST", "AKBM", "ACH", "AKH", "AOW", "AKOBO", "ARCH", "ABS", "ARGEO", "ASTRO", "AURA", "ACR", "BGBIO", "BFISH", "CAPSL", "EAM", "ECIT", "ECO", "EWIND", "EIOF", "EMGS", "EFUEL", "EXTX", "FKRFT", "GEOS", "HAVI", "HYARD", "HDLY", "HUNT", "HYPRO", "KAHOT", "KOMPL", "KOA", "KYOTO", "LYTIX", "MVW", "MSEIS", "MRCEL", "MNTR", "NOC", "NEXT", "NORDH", "NANOV", "NUMND", "NODL", "NOL", "NAS", "NOR", "NYKD", "OBSRV", "PEXIP", "PGS", "QFUEL", "SCANA", "SKAND", "TEKNA", "VGM"]

sentence = "https://finance.yahoo.com/quote/" 
end = ".OL?p=&.tsrc=fin-srch"
n = 0





for word in tickers:
    
    with webdriver.Chrome() as driver: 
        print(f"\n\nHenter {tickers[n]}\n\n")

        driver.get(sentence + tickers[n] + end)
        driver.maximize_window()
        driver.implicitly_wait(3)

        cookies = driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/div[2]/div[2]/button')
        cookies.click()
    
        driver.implicitly_wait(3)
        
        do_not_save = driver.find_element(By.XPATH, '//*[@id="myLightboxContainer"]/section/button[2]')
        do_not_save.click()

        driver.implicitly_wait(3)


        object = driver.find_element(By.XPATH, '//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[1]')
        number_value = object.text

        driver.implicitly_wait(3)
        

        with open("numberValue.txt", "a") as f:
            
            f.write(tickers[n])
            f.write(" ")
            f.write(number_value)
            f.write("\n")
            f.close
        
        print(f"\n\nAdded {tickers[n]} to the list")
        n = n + 1

driver.quit()
driver.implicitly_wait(3)
    