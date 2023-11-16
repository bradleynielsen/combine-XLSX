import os
import pandas as pd


import importlib.util
from datetime import date
from datetime import datetime

#pd = importlib.util.spec_from_file_location("pandas", "/python-3.8.7-embed-amd64/site-packages/pandas")


#config:
xl_path = ".\\xl"               # Path to xl files

#init:
fileslist         = os.listdir(xl_path)   # List of files

today             = str(date.today())
now               = datetime.now()
current_time      = now.strftime("%H%M%S")
todaycurrent_time = today + "_" + current_time
results_path      = ".\\results"
results_filename  = "results" + todaycurrent_time + ".xlsx"
results_filepath  = os.path.join(results_path, results_filename)




#excels = [pd.ExcelFile(name) for name in fileslist]

print([pd.ExcelFile(name) for name in fileslist])