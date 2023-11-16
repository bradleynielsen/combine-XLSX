import pandas as pd
import os
from datetime import date
from datetime import datetime

today             = str(date.today())
now               = datetime.now()
current_time      = now.strftime("%H%M%S")
todaycurrent_time = today + "_" + current_time
results_path      = ".\\results"
results_filename  = "results" + todaycurrent_time + ".xlsx"
results_filepath  = os.path.join(results_path, results_filename)

#config:
xl_path = ".\\xl"               # Path to xl files

#init:
fileslist         = os.listdir(xl_path)   # List of files

#create an empty dataframe which will have all the combined data
mergedData = pd.DataFrame()
for files in fileslist:
    #make sure you are only reading excel files
    if files.endswith('.xlsx'):
        data = pd.read_excel(files, index_col=None)
        mergedData = mergedData.append(data)
        #move the files to other folder so that it does not process multiple times
        os.rename(files, results_filepath)