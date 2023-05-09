import os, sys
import pandas as pd
import numpy as np
from Wine_ML.constant import *
from Wine_ML.logger import logging
from Wine_ML.exception import CustomException
from Wine_ML.pipeline.pipeline import Pipeline 
import os, sys

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")

if __name__=="__main__":
    main()

