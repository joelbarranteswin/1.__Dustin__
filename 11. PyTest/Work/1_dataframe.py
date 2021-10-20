from dataclasses import dataclass
from typing import Type, Union 
import pytest
import pandas
import openpyxl
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory


def test_get_dataframe(name):
    dataframe = pandas.read_excel(f'{cwd}\{name}')
    if dataframe.empty:
        print("el dataframe esta vacio")
        print(dataframe)

test_get_dataframe('dataframe.xlsx')