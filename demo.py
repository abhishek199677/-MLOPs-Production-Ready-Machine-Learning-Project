
# import os


# mongo_db_url = os.getenv('MONGODB_URL')    #for generating connection/collection string (mail password)
# print(mongo_db_url)


from us_visa.pipline.training_pipeline import TrainPipeline      #to run the entire training pipeline

obj = TrainPipeline()   #object
obj.run_pipeline()    #method