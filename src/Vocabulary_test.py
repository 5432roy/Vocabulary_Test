import requests

def get_token(path):
    try:
        file = open(path)
        token = file.readline().strip()
        database_ID = file.readline().strip()
        return token, database_ID
    except:
        raise FileNotFoundError

def read_database():

    token, database_ID = get_token("D:/Visual Studio Code/GitHub/Vocabulary_Test/src/token.txt")

    readURL = f'https://api.notion.com/v1/databases/{database_ID}/query'
    headers = {
            "Authorization": token,
            "Notion-Version": "2022-06-28"
    }
    try:
        res = requests.request("POST", readURL, headers = headers)
        data = res.json()
        return data
    except:
        print("Fetch Error")

def data_parser(data):
    vocabularies = {}
    for vocabulary in data['results']:
        cur = vocabulary['properties']
        if len(cur['Meaning']['rich_text']) > 0:
            vocabularies[cur['Vocabulary']['title'][-1]['plain_text']] = cur['Meaning']['rich_text'][-1]['plain_text']
    return vocabularies
        

data = read_database()
vocabularies = data_parser(data)
print(vocabularies)


"""
print(data['results'][1]['properties']['Vocabulary']['title'][-1]['plain_text'])
print(data['results'][1]['properties']['Meaning']['rich_text'][-1]['plain_text'])
print(data['results'][1]['properties']['Meaning 2'])
"""

