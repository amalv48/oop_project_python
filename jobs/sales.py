import json, os, re, sys
from typing import Callable, Optional

from pyspark.sql.dataframe import DataFrame
from pyspark.sql import SparkSession


project_dir = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = f"{project_dir}\logs\job-{os.path.basename(__file__)}.log"
print(project_dir)
print(LOG_FILE)

