from us_visa.configuration.mongo_db_connection import MongoDBClient
from us_visa.constants import DATABASE_NAME
from us_visa.exception import USvisaException
import pandas as pd
import sys
from typing import Optional
import numpy as np



class USvisaData:
    """
    This class help to export entire mongo db record as pandas dataframe

    or 


    exporting data as a pandas dataframe

    """

    def __init__(self):
        """
        """
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)    #Making connection with mongodb
        except Exception as e:
            raise USvisaException(e,sys)
        

    def export_collection_as_dataframe(self,collection_name:str,database_name:Optional[str]=None)->pd.DataFrame:  #giving collection_name snd database name and it will give datafram,e
        try:
            """
            export entire collectin as dataframe:
            return pd.DataFrame of collection
            """
            if database_name is None:      #if database is none 
                collection = self.mongo_client.database[collection_name] #it will create connection 
            else:
                collection = self.mongo_client[database_name][collection_name] #else it will make connection

            df = pd.DataFrame(list(collection.find()))       #converting data to data frame using pandas
            if "_id" in df.columns.to_list():              #droping a column
                df = df.drop(columns=["_id"], axis=1)
            df.replace({"na":np.nan},inplace=True)
            return df
        except Exception as e:
            raise USvisaException(e,sys)