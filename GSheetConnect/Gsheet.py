# Getting data from google sheet and data handling

import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

rent = []
utility = []
food = []
travel = []
general = []
car = []
merchandise = []

def get_allcategories(lists):
    global rent
    global utility
    global food
    global travel
    global general
    global car
    global merchandise 
    for i in range(len(lists)):
        if lists[i]['Category'] == 'Rent':
            rent.append(lists[i]['Price'][1:])
        elif lists[i]['Category'] == 'Utility':
            utility.append(float(lists[i]['Price'][1:]))
        elif lists[i]['Category'] == 'Food':
            food.append(float(lists[i]['Price'][1:]))
        elif lists[i]['Category'] == 'General':
            general.append(float(lists[i]['Price'][1:]))
        elif lists[i]['Category'] == 'Travel':
            travel.append(float(lists[i]['Price'][1:]))
        elif lists[i]['Category'] == 'Merchandise':
            merchandise.append(float(lists[i]['Price'][1:]))

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_sheet.json', scope)

gc = gspread.authorize(credentials)

sheet = gc.open('Copy_of_Kharcha_US').get_worksheet(2)
pp = pprint.PrettyPrinter()

#json_key = json.load(open('creds.json')) # json credentials you downloaded earlier
#scope = ['https://spreadsheets.google.com/feeds']

#credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope) # get email and key from creds

#file = gspread.authorize(credentials) # authenticate with Google
#sheet = file.open("Copy_of_Kharcha_US").sheet1
all_cells = sheet.get_all_records(sheet)
print(len(all_cells))
print(type(all_cells))
get_allcategories(all_cells) 
pp.pprint(all_cells)

print(f'Total rent is ${rent[0]}')
print(f'Total utility is ${sum(utility)}')
print(f'Total travel is ${sum(travel)}')
print(f'Total merchandise is ${sum(merchandise)}')
print(f'Total food is ${sum(food)}')
print(f'Total general is ${sum(general)}')
