# from entityFunctions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pandas as pd
import csv
from selenium.webdriver.chrome.service import Service


import time
import os


s = Service(r"C:/Users/JT/Documents/chromedriver.exe")
page = webdriver.Chrome(service=s)
URL = "http://search.sunbiz.org/Inquiry/CorporationSearch/ByName"

# start
def getDriver():
    page.get(URL)
        

# Named Insured to look for
def EntityName(name):
    global carrierName

    # Reading csv data in pandas DF
    data = pd.read_excel('FinalLeadsRevised.xlsx')
    
    try:
        element = WebDriverWait(page, 20).until(
            EC.presence_of_element_located((By.ID, "SearchTerm"))
        )
    except:
        page.refresh()
        print("Found Name")

    finally: 
        searchBy = page.find_element_by_id('SearchTerm')
        # carrierName = input("Enter Named Insured: ")

        # dynamically add bussinesses to check
          
        carrierName=(name)  
        searchBy.send_keys(carrierName)
        print("input set")

# simple click                
def clickButton(name):
    
    
    try:
        print("here1")
        element = WebDriverWait(page, 10).until(
            EC.presence_of_element_located((By.xpath, '//input[@type="submit"]'))
        )
        searchBy = page.find_element_by_id('SearchTerm')
        carrierName=(name)  
        searchBy.send_keys(carrierName)
        button = page.find_element_by_xpath('//input[@type="submit"]')
        button.click()
    except:
        
        print("Failed")

    finally:
        searchBy = page.find_element_by_id('SearchTerm')
        carrierName=(name)  
        searchBy.send_keys(carrierName)
        button = page.find_element_by_xpath('//input[@type="submit"]')
        button.click()


# Click First Element
def selectResult():
    getOption = "/html/body/div[1]/div[1]/div[2]/div/div[2]/table"
    a_tag_text = []
    
    try:
        print("here")
        time.sleep(5)
        element = WebDriverWait(page, 20).until(
            EC.presence_of_element_located((By.ID, "search-results"))
            
        )
        table_row = element.find_elements_by_tag_name("tr")
        print(table_row.length())

        for i in table_row:
            a_tag = element.find_elements_by_tag_name("a")
            print(a_tag)
            # a_tag_text.append(a_tag.text)
        
        # if(carrierName ==  ):
        #     pass 
        


        # if(element[1] == carrierName ):
        #     pass
        # selectResult = page.find_element_by_xpath(getOption)
        # selectResult.click()
        print("Found table")
        
    except:
        print("Cant find table element")
        page.refresh()
        print("refreshed")
        time.sleep(5)
        selectResult()

#Grab Company Name 
def getCompanyName():
    
    companyName = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/p[2]"
     
    try:
        element = WebDriverWait(page, 10).until(
            EC.presence_of_element_located((By.xpath, companyName))
        )
        
    except:
        page.refresh()
        print("found Company xpath")

    finally: 
        # page.get(page.current_url)
        # time.sleep(2)
        # page.refresh()
        global companyNameResult 
        companyNameResult = page.find_element_by_xpath(companyName).text # changes to text format
        print(companyNameResult)
        return companyNameResult
        
#Grab Agent Info
def getAgentInfo():
    
    title = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div[6]"
     
    try:
        element = WebDriverWait(page, 10).until(
            EC.presence_of_element_located((By.xpath, title))
        )
    except:
        print("found Agent xpath")

    finally: 
        # Loading in workers comp data frame
        addOwnerdata = pd.read_pickle('GrabWorkersComp.pkl')
        print(addOwnerdata)

        # Grab Agent info 
        global agentInfo 
        agentInfo = page.find_element_by_xpath(title).text
        print(agentInfo)
        

        # Splitting string text to grab name
        
        listSplit = agentInfo.split()
        print(listSplit)
        getName = listSplit[8:10] 
        print(getName)

        #Convert list back to string for pandas
        listToString = ' '.join(getName)

        # Add split elements into existing Dataframe
        addOwnerdata['Title Manager'] = listToString
        print(addOwnerdata)

        # Pickling collected data to excel
        addOwnerdata.to_pickle('grabOwnerInfo.pkl')

        return agentInfo

        # page quit
        page.quit()
        
#Save to notepad      
# def saveToPandas():
    # print()



    # newFile = 'OwnerInfo.txt'
    # bottomSpacer = "-------------------------"
    
    # Opens new file and appends text to file
    # with open(newFile, 'w') as f:
    #     f.write( "TITLE COMPANY"
    #             + "\n"
    #             + companyNameResult 
    #             + "\n\n" 
    #             + agentInfo 
    #             + "\n"
    #             + bottomSpacer )
        
        # print("File was successfully made")
        # os.startfile(newFile)
        
    


def entityFinder():
    # csv file name
    filename = 'DecemberLeads.csv'
    
    # # initializing the titles and rows list
    # fields = [] 
    # rows = []
    
    # reading csv file
    with open(filename, 'r') as csvfile:
        
        csvreader = csv.reader(csvfile)

        fields = next(csvreader)

        for row in csvreader:
            # print(row[5]) 
            # index 5 gives bussiness title
            # bizName = "999TCB LLC"
            bizName = row[5]
            print(bizName)
    
            getDriver()
            EntityName(bizName)
            clickButton(bizName)
            selectResult()
            # companyName = getCompanyName()
            # agentInfo = getAgentInfo()

            # print(companyNameResult)
            # print(agentInfo)

    # saveToPandas()

# entityFinder()