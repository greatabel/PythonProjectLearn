import imaplib, email, os
import pandas as pd

# import numpy as np
from datetime import datetime


def process_excel(target_excel):
    data = pd.read_excel(target_excel, sheet_name=0)


def loop_folder_excels():
    path = os.getcwd()
    directory = (datetime.today()).strftime("%Y-%m-%d")
    path = path + "/" + directory + "/"
    for filename in os.listdir(path):
        if filename.endswith(".xlsx") or filename.endswith(".xls"):
            print(path + filename)


if __name__ == "__main__":
    loop_folder_excels()
