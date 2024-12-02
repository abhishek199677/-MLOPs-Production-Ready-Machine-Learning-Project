import os
from dataclasses import dataclass



@dataclass
class DataIngestionArtifact:   #this will generate train.csv and test.csv file
    trained_file_path:str 
    test_file_path:str

