
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pandas as pd
from selenium.webdriver.chrome.service import Service



import time
import os
import json

# GET driver
s = Service(r"C:/Users/JT/Documents/chromedriver.exe")
page = webdriver.Chrome(service=s)

expirationSelectionNumber = str(3)
monthNumber = str(2)
yearNumber = str(2022)


# ChromeDriver PATH set
def getDriver(): 
    page.get("https://dwcdataportal.fldfs.com/ProofOfCoverage.aspx")
        

def ExpirationDate():
    try:
        element = WebDriverWait(page, 10).until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_ddlSearchOptions"))
        )
    except:
        print("Wasnt able to find searchBy field ID")

    finally:
        searchBy = Select(page.find_element_by_id('ContentPlaceHolder1_ddlSearchOptions'))
        searchBy.select_by_value(expirationSelectionNumber)

        
        

def selectYear():
    try:
        element = WebDriverWait(page, 10).until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_ddlSearchOptions"))
        )
    except:
        print("Wasnt able to find Year ID")

    finally:
        selectYear = Select(page.find_element_by_id('ContentPlaceHolder1_ddYear'))
        selectYear.select_by_value(yearNumber)

# Check for Month
def selectMonth(): 
    try:
        element = WebDriverWait(page, 10).until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_ddMonth"))
        )
    except:
        print("Wasnt able to find Month ID")

    finally: 
        selectMonth = Select(page.find_element_by_id('ContentPlaceHolder1_ddMonth'))
        selectMonth.select_by_value(monthNumber)

        # 1 - JAN
        # 2 - FEB 
        # 3 - MAR 
    
# County Field 
def selectCounty():
    try:
        element = WebDriverWait(page, 10).until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_ddCounty"))
        )
    except:
        print("Wasnt able to find element")

    finally:
        selectCounty = Select(page.find_element_by_id('ContentPlaceHolder1_ddCounty'))
        selectCounty.select_by_value("056")  
        
        # Broward - 006
        # St. Lucie - 056
        
# Insurer Field
def selectInsurer():    
    try:
        element = WebDriverWait(page, 10).until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_ddInsurer"))
        )
    except:
        print("Wasnt able to find element")


    finally:
        selectInsurer = Select(page.find_element_by_id('ContentPlaceHolder1_ddInsurer'))
        selectInsurer.select_by_value("0")
        # All selection = "0"
        # "ACCIDENT FUND INSURANCE COMPANY OF AMERI" DEMO VALUE USED
        
# Clicking Search Button
def clickButton():
    try:
        element = WebDriverWait(page, 10).until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_btnSearch2"))
        )
    except:
        print("Wasnt able to find button`")

    finally:
        button = page.find_element_by_id('ContentPlaceHolder1_btnSearch2')
        button.click()
    
# Finding HTML Table and converting to CSV 

newFile = "insuranceLeads.csv"

def getTable():
    try:
        element = WebDriverWait(page, 7).until(
            EC.presence_of_element_located((By.ID, "Form1"))
        )
    except:
        print("Wasnt able to find form")
        

    finally:

        # Find form 
        
        df = pd.read_html(page.find_element_by_xpath("//*[@id='ContentPlaceHolder1_DataGrid_POC']").get_attribute('outerHTML'))[0]
        
        # Grabbing data we want from website and organizing it
        
        pulledData = {
            'Employer Address': df['Employer Address'], 
            'Policy Number': df['Policy Number'], 
            'Policy Expiration Date': df['Policy Expiration Date'],
            'Employer Name': df['Employer Name'], 
            'Named Insured': df['Named Insured'], 
            'Class Code': df['Governing Class Code'] 
            }
        
        # Columns will be inputted into DataFrame
        df_info = pd.DataFrame(data=pulledData)

        # Feedback

        print(df_info) 

        # Results to CSV
         
        df_info.to_csv('February.csv')
        
        page.quit()

        



    
        
        
def leadFinder():
    
    getDriver()
    ExpirationDate()
    selectYear()
    selectMonth()
    selectCounty()
    selectInsurer()
    clickButton()
    getTable()

leadFinder()