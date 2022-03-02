import json, os, re, sys
from typing import Callable, Optional

from pyspark.sql.dataframe import DataFrame
from pyspark.sql import SparkSession

class Sparkclass:

    def __init__(self, myvar):
        self.myvar = myvar

    def sparkStart(self):
        print(self.myvar)