import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe
from google.oauth2.service_account import Credentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
scopes = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']

credentials = Credentials.from_service_account_file('community-colleges-514717a41ebb.json', scopes=scopes)

gc = gspread.authorize(credentials)

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

# open a google sheet
gs = gc.open_by_url("https://docs.google.com/spreadsheets/d/1aWYD9Z9HlTrroQyApbkc7Lh6kR91Ivy5978nwLEIwFg/edit?usp=sharing")
# select a work sheet from its name
worksheet1 = gs.worksheet('Sheet1')

# dataframe (create or import it)
df = pd.DataFrame({'a': ['apple','airplane','alligator'], 'b': ['banana', 'ball', 'butterfly'], 'c': ['cantaloupe', 'crane', 'cat']})


# write to dataframe
worksheet1.clear()
set_with_dataframe(worksheet=worksheet1, dataframe=df, include_index=False,
include_column_header=True, resize=True)

# dataframe (create or import it)
df = pd.DataFrame({'a':['astronaut', 'ant'], 'b':['bingo', 'bee'], 'c':['candy', 'cake']})
df_values = df.values.tolist()
gs.values_append('Sheet1', {'valueInputOption': 'RAW'}, {'values': df_values})
