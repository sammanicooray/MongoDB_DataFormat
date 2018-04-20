# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 11:50:19 2018

@author: sammani.cooray
"""

#Convert Data to JASON format

#import data from excel.

from pymongo import MongoClient
import pandas

file_location = "C:\\Users\\sammani.cooray\\Google Drive\\DataFiles\\DataFiles\\crunchbase_export.xlsx"

def readDataAndFormat():

    # Read all data
    df = pandas.read_excel(file_location, sheet_name = "Funded Companies" )
    
    #print(df.shape)
    #print(df.columns)
    
    # Drop unneccessary columns
    
    df = df.drop(columns=['uuid'])
    
    #print(df.shape)
    #print(df.columns)
    
    #convert the dataframe to a list
    allData = df.values.tolist()
    columns = df.columns.tolist()
    
    jsonList = []
    
    for data in allData:
        jsonList.append(dict(zip(columns, data)))
    
    return jsonList


def writeToMongo(data):

    client = MongoClient()
    db = client.softbase
    collection = db.companydata
    dataitems = collection.dataitems
    results = dataitems.insert_many(data)
    
    # to improve 
    '''
     add try catch block and print out company name etc to pin point the place where it is failing
    '''
    
    return results
    
    
    
    
    
    
    
    

    
