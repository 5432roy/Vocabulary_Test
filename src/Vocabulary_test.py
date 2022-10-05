import requests

token = open("D:/Visual Studio Code/GitHub/Vocabulary_Test/src/token.txt").readline()
database_ID = '5d7dfeb4ecc44661a7cc15b62966a700'

headers = {
    "Authorization": "Bearer " + token,
    "Notion-Version": "2022-06-28"
}

def read_database(database_ID, headers):
    readURL = f'https://api.notion.com/v1/databases/{database_ID}/query'
    
    try:
        res = requests.request("POST", readURL, headers = headers)
        data = res.json()
        return data
    except:
        print(res.status_code, ", Fetch Error")

def data_parser(data):
    vocabularies = {}
    for vocabulary in data['results']:
        cur = vocabulary['properties']
        if len(cur['Meaning']['rich_text']) > 0:
            vocabularies[cur['Vocabulary']['title'][-1]['plain_text']] = cur['Meaning']['rich_text'][-1]['plain_text']
    return vocabularies
        

data = read_database(database_ID, headers)
vocabularies = data_parser(data)
print(vocabularies)


"""
print(data['results'][1]['properties']['Vocabulary']['title'][-1]['plain_text'])
print(data['results'][1]['properties']['Meaning']['rich_text'][-1]['plain_text'])
print(data['results'][1]['properties']['Meaning 2'])
"""

