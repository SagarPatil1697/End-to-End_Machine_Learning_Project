import os
import sys
import dill

import numpy as np
import pandas as pd

from src.exception import CustomException

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


