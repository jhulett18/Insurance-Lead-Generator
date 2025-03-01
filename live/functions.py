from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pandas as pd
import csv
from openpyxl import load_workbook
import openpyxl

import time
import os

# variables
# PATH = r"C:\Users\mutua\Downloads\chromedriver.exe"
PATH = r"C:\Users\JT\Documents\chromedriver.exe"
page = webdriver.Chrome(PATH)

def getDriver():
    page.get("https://dwcdataportal.fldfs.com/ProofOfCoverage.aspx")    
# ChromeDriver PATH set


# searchBy field

def ExpirationDate():
    try:
        element = WebDriverWait(page, 10).until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_ddlSearchOptions"))
        )
    except:
        print("Wasnt able to find searchBy field ID")

    finally:
        searchBy = Select(page.find_element_by_id('ContentPlaceHolder1_ddlSearchOptions'))
        searchBy.select_by_value("3")
        
# Check for Year
def selectYear():
    try:
        element = WebDriverWait(page, 10).until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_ddlSearchOptions"))
        )
    except:
        print("Wasnt able to find Year ID")

    finally:
        selectYear = Select(page.find_element_by_id('ContentPlaceHolder1_ddYear'))
        selectYear.select_by_value("2021")

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
        selectMonth.select_by_value("11")
    
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
        selectInsurer.select_by_value("ACCIDENT FUND INSURANCE COMPANY OF AMERI")
        # All selection = "0"
        # "ACCIDENT FUND INSURANCE COMPANY OF AMERI" DEMO VALUE USED
        

def getDataframe():
    print()

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
        page.quit()

    finally:
        
        

        df = pd.read_html(page.find_element_by_id("ContentPlaceHolder1_DataGrid_POC").get_attribute('outerHTML'))[0]
        # print(df.head)
        d = {'Name': df['Employer Name']}
        df_name = pd.DataFrame(data=d)
        print(df.columns)
        print(df_name) 

        nameJSON = df_name.to_json()
        print(nameJSON)

        # Converting column to list  
        # named_list = df['Named Insured'].tolist()
        

        name_values = df['Employer Name'] 

        # Prints all values in a column

        # name_values.to_csv(newFile, index=False)




        # print("CSV was successully made ")
        # # time.sleep(2)
        
        page.quit() # Lets the program continues
        # os.startfile(newFile)
        
        # Lets python open File
        