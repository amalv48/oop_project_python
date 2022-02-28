import json, os, re, sys
from typing import Callable, Optional

from pyspark.sql.dataframe import DataFrame
from pyspark.sql import SparkSession

class Sparkclass:

    def __init__(self, config:dict):
        self.config = config

    def sparkStart(self, kwargs:dict) -> SparkSession:
    
        print(self.config)