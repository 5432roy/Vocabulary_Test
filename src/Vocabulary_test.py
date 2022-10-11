import tkinter as tk
from tkinter import *
import requests

def read_database():
    try:
        file = open("D:/Visual Studio Code/GitHub/Vocabulary_Test/src/token.txt")
        token = file.readline().strip()
        database_ID = file.readline().strip()
    except:
        raise FileNotFoundError
    
    readURL = f'https://api.notion.com/v1/databases/{database_ID}/query'
    headers = {
            "Authorization": token,
            "Notion-Version": "2022-06-28"
    }
    data = ""
    try:
        res = requests.request("POST", readURL, headers = headers)
        data = res.json()
    except:
        print("Fetch Error")
        
    vocabularies = {}
    for vocabulary in data['results']:
        cur = vocabulary['properties']
        if len(cur['Meaning']['rich_text']) > 0:
            vocabularies[cur['Vocabulary']['title'][-1]['plain_text']] = cur['Meaning']['rich_text'][-1]['plain_text']
    return vocabularies

class GUI:
    def __init__(self, root, dictionary):
        self.root = root
        root.title("Vocabulary Test")
        root.geometry('500x100')
        self.index = 0

        self.user_input = tk.StringVar()
        # the anwer box for the user to input the vocabulary
        self.answer = Entry(root, textvariable = self.user_input)
        self.answer.pack(side = TOP)
        # bind the function get_text with this property and trigger by Hitting 'Enter'
        self.answer.bind('<Return>', self.get_text)

        self.meaning = Label(root, text = ": " + list(dictionary.values())[self.index])
        self.meaning.pack(side = TOP)

        # initail the status label of user input
        self.status = Label(root, text = "")
        self.status.pack(side = TOP)

    # function to get the text from Entry "answer"
    def get_text(self, event):
        print(list(dictionary.keys())[self.index])
        if self.user_input.get() == list(dictionary.keys())[self.index]:
            text = "Correct!"
            self.index += 1
            self.meaning.config(text = ": " + list(dictionary.values())[self.index])
        else:
            text = "Wrong"
            print(self.user_input.get())
        self.user_input.set("")

        self.status.config(text = text)

# TODO
# replace the current code that getting the value from dictionary one by one through the for loop sturcture with a generator function
# makes the selection of words become random

if __name__ == "__main__":
    dictionary = read_database()
    vocabulary_1 = list(dictionary.keys())[0]
    root = Tk()
    gui = GUI(root, dictionary)
    root.mainloop()



