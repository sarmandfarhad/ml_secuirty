import os
import sys
import json
from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

print(MONGO_DB_URL)

import certifi
ca=certifi.where()
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.execption import NetworkSecurityException
from networksecurity.logging.logger import logging
class networkDataExtractor():
  def __init__(self):
    try:
      pass
    except Exception as e:
      raise NetworkSecurityException(e, sys)
  def cv_to_json(self, file_path):
    try:
      df = pd.read_csv(file_path)
      df.reset_index(drop=True, inplace=True)
      records=list(json.loads(df.T.to_json()).values())  #convert dataframe to the list of json format
      return records
    except Exception as e:
      raise NetworkSecurityException(e, sys)
  def insert_data_to_mongodb(self, records,database, collection):
    try:
      self.database=database
      self.collection=collection
      self.records=records
      self.client=pymongo.MongoClient(MONGO_DB_URL,tlsCAFile=ca)
      self.database=self.client[self.database]
      self.collection=self.database[self.collection]
      self.collection.insert_many(self.records)
      return "Data inserted successfully"+str(len(self.records))
    except Exception as e:
      raise NetworkSecurityException(e, sys)

if __name__ == "__main__":
    FIle_path='Network_Data\phisingData.csv'
    database='sarmandai'
    collection='network_data'
    networkobj=networkDataExtractor()
    records=networkobj.cv_to_json(FIle_path)
    print(records[0])
    no_of_records=networkobj.insert_data_to_mongodb(records, database, collection)
    print(no_of_records)