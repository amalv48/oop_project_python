#from cmath import log
import logging
import json, os, re, sys
from typing import Callable, Optional

from pyspark.sql.dataframe import DataFrame
from pyspark.sql import SparkSession


project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # set the project directoy -> "d:/oop_project/"
LOG_FILE = f"{project_dir}/logs/job-{os.path.basename(__file__)}.log"
LOG_FORMAT = f"%(asctime)s - LINE:%(lineno)d - %(name)s - %(levelname)s - %(funcName)s - %(message)s"
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format=LOG_FORMAT)
logger = logging.getLogger('py4j')

sys.path.insert(1, project_dir) # pointing to the right directory where classes reside
from classes import class_pyspark

def main():
    class_pyspark.Sparkclass("hello myvar").sparkStart() 

if __name__ == '__main__':
    main()