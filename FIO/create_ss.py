import httplib2
import os
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'key.json' # Имя файла с закрытым ключом, этот ключ не тепять и оставлять в секурном месте

# Читаем ключи из файла и устанавливаем разрешение на использование таблиц и диска
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth) # Выбираем работу с таблицами и 4 версию API

#создание таблицы
'''spreadsheet = service.spreadsheets().create(body = {
    'properties': {'title': 'Первый тестовый документ', 'locale': 'ru_RU'},
    'sheets': [{'properties': {'sheetType': 'GRID',
                               'sheetId': 0,
                               'title': 'Лист номер один',
                               'gridProperties': {'rowCount': 100, 'columnCount': 15}}}]
}).execute()
'''
#spreadsheetId = '19yuiLWLOYVb1dOGIS_Mp8nadT4cc9SvAxpOBemo0qsU'
spreadsheetId = '1fXg3n9aszVP_CEzFKX4O6o1kJRdjiU39jwBldqzG7bE'
#spreadsheet['spreadsheetId'] # сохраняем идентификатор файла
print('https://docs.google.com/spreadsheets/d/' + spreadsheetId)

''' share access to myself
driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth) # Выбираем работу с Google Drive и 3 версию API
access = driveService.permissions().create(
    fileId = spreadsheetId,
    body = {'type': 'user', 'role': 'writer', 'emailAddress': 'aminogoule@gmail.com'},  # Открываем доступ на редактирование
    fields = 'id'
).execute()
'''
"""================================================================================================================="""
#add sheet to book
'''
results = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheetId,
    body=
    {
        "requests": [
            {
                "addSheet": {
                    "properties": {
                        "title": "Anothe One",
                        "gridProperties": {
                            "rowCount": 20,
                            "columnCount": 12
                        }
                    }
                }
            }
        ]
    }).execute()
'''
#=============================изменение данных и пакетное измененеие==================


#=====================================================================================
#по строчное чтение
ranges = ["List_of!A1:L"]  #
out_docum = '19yuiLWLOYVb1dOGIS_Mp8nadT4cc9SvAxpOBemo0qsU'
results = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId,
                                                   ranges=ranges,
                                                   valueRenderOption='FORMATTED_VALUE',
                                                   dateTimeRenderOption='FORMATTED_STRING').execute()
sheet_values = results['valueRanges'][0]['values']
#print(sheet_values)
fd=open('output.txt',"a")


for l1 in range(len(sheet_values)):
   #fill res data each iteration of for loop
    #row_data=[sheet_values[l1]]


    for l2 in range(len(sheet_values[l1])):
        fd.write(sheet_values[l1][l2]+'; ')
    fd.write('\n')
row_data=sheet_values
res = {"majorDimension": "ROWS","values": row_data}
sheet=service.spreadsheets()
sheet.values().append(spreadsheetId=out_docum,range='Лист1!A1',valueInputOption='USER_ENTERED',body=res).execute()
#---------------------------------------------
#открываем документ в который надо записать
'''
print('https://docs.google.com/spreadsheets/d/' + out_docum + '<== output here')
# make batch
in_range=["result!A1:L"]

r2 = service.spreadsheets().values().batchUpdate(spreadsheetId=out_docum,
                                                   ranges=in_range,
                                                   valueRenderOption='FORMATTED_VALUE',
                                                   dateTimeRenderOption='FORMATTED_STRING').execute()'''

#=================================================================================================================
print('may be it done =))')
# Получаем список листов, их Id и название
#Prepare to insert and update data from one sheet to another


#=================================================================================================================

spreadsheet = service.spreadsheets().get(spreadsheetId=spreadsheetId).execute()
sheetList = spreadsheet.get('sheets')
for sheet in sheetList:
    print(sheet['properties']['sheetId'], sheet['properties']['title'])

sheetId = sheetList[0]['properties']['sheetId']

print('Мы будем использовать лист с Id = ', sheetId)