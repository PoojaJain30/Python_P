import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_sheet.json', scope)

gc = gspread.authorize(credentials)

sheet = gc.open('Practice').get_worksheet(1)
pp = pprint.PrettyPrinter()

#json_key = json.load(open('creds.json')) # json credentials you downloaded earlier
#scope = ['https://spreadsheets.google.com/feeds']

#credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope) # get email and key from creds

#file = gspread.authorize(credentials) # authenticate with Google
#sheet = file.open("Copy_of_Kharcha_US").sheet1
all_cells = sheet.get_all_records(sheet)
pp.pprint(all_cells)
