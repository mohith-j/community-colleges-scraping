import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe
from google.oauth2.service_account import Credentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
scopes = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']

credentials = Credentials.from_service_account_file('test-gs-389813-c2ce335b243e.json', scopes=scopes)

gc = gspread.authorize(credentials)

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

# open a google sheet
gs = gc.open_by_key("1wThfRD3CjxmLsGs2yirzdK5AhPXcw-mucOapBRxt50w")
# select a work sheet from its name
worksheet1 = gs.worksheet('Sheet1')

# dataframe (create or import it)
df = pd.DataFrame({'colleges': ['chatahoochee','',''], 'majors': ['accounting', '', ''], 'courses': ['acc 101', 'acc 151', 'acc 201']})
# write to dataframe
worksheet1.clear()
set_with_dataframe(worksheet=worksheet1, dataframe=df, include_index=False,
include_column_header=True, resize=True)

# dataframe (create or import it)
df = pd.DataFrame({'colleges':['chathoochee','', ''], 'majors':['business','', ''], 'courses':['bus 101', 'bus 151', 'bus 201']})
df_values = df.values.tolist()
gs.values_append('Sheet1', {'valueInputOption': 'RAW'}, {'values': df_values})

#-------------------------------------------------

df = pd.DataFrame({'colleges':['chathoochee','', ''], 'majors':['construction','', ''], 'courses':['ctn 101', 'ctn 151', 'ctn 201']})
df_values = df.values.tolist()
gs.values_append('Sheet1', {'valueInputOption': 'RAW'}, {'values': df_values})

#-------------------------------------------------

df = pd.DataFrame({'colleges':['------','', ''], 'majors':['------','', ''], 'courses':['------', '', '']})
df_values = df.values.tolist()
gs.values_append('Sheet1', {'valueInputOption': 'RAW'}, {'values': df_values})

#-------------------------------------------------

df = pd.DataFrame({'colleges':['gwinnett','', ''], 'majors':['accounting','', ''], 'courses':['acc 101', 'acc 151', 'acc 201']})
df_values = df.values.tolist()
gs.values_append('Sheet1', {'valueInputOption': 'RAW'}, {'values': df_values})