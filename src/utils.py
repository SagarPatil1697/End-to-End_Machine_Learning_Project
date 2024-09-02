import os
import sys
import dill

import numpy as np
import pandas as pd

from src.exception import CustomException
from sklearn.metrics import r2_score

def save_object(file_path, obj):
    """
    This function is responsible for saving object

    Args:
    file_path : str : file path
    obj : object : object to save
    """
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path, 'wb') as file:
            dill.dump(obj, file)
            
    except Exception as e:
        raise CustomException(f"Error in saving object : {str(e)}")

def evaluate_models(X_train,y_train,X_test,y_test,models):
    try:
        report = {}

        for i in range(len(list(models))):
            # model_name = list(models.keys())[i]
            model = list(models.values())[i]
            model.fit(X_train, y_train) # Train Model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test) # Predict Model

            # y_pred = model.predict(X_test)
            train_model_score = r2_score(y_train,y_train_pred)

            test_model_score = r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]] = test_model_score
        
        return report
    
    except Exception as e:
        raise CustomException(e,sys)
            


