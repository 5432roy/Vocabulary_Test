import tkinter as tk
from tkinter import *
import requests
import random 

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
            vocabularies[cur['Vocabulary']['title'][-1]['plain_text'].lower().strip()] = cur['Meaning']['rich_text'][-1]['plain_text']
    return vocabularies

class GUI:
    def __init__(self, root, dictionary):
        
        self.root = root
        root.title("Vocabulary Test")
        root.geometry('1000x500')
        root.configure(bg = "gray")
        self.words = self.generator()
        self.current_word = next(self.words)

        self.user_input = tk.StringVar()

        # the anwer box for the user to input the vocabulary
        self.answer = Entry(root, textvariable = self.user_input, bg = "gray", font=('calibre',20,'normal'))
        self.answer.pack(side = TOP, anchor = NW)
        # bind the function get_text with this property and trigger by Hitting 'Enter'
        self.answer.bind('<Return>', self.get_text)

        self.meaning = Label(root, text = ": " + dictionary[self.current_word], font=("Helvetica", 20),
                            bg = "gray", wraplengt = 1000)
        self.meaning.pack(side = TOP, anchor = NW)

        # initail the status label of user input
        self.status = Label(root, text = "", bg = "gray")
        self.status.pack(side = TOP, anchor = NW)

    # using gernerator to iterarte through the list of vocabulary
    def generator(self):
        words = list(dictionary.keys())
        random.shuffle(words)
        for word in words:
            print(word)
            yield word

    # function to get the text from Entry "answer"
    def get_text(self, event):
        if self.user_input.get().lower() == self.current_word:
            text = "Correct!"
            self.current_word = next(self.words)
            self.meaning.config(text = ": " + dictionary[self.current_word])
        else:
            text = "Wrong"
            print("Wrong answer: " + self.user_input.get())
        
        self.user_input.set("")
        self.status.config(text = text)



if __name__ == "__main__":
    dictionary = read_database()
    vocabulary_1 = list(dictionary.keys())[0]
    root = Tk()
    gui = GUI(root, dictionary)
    root.mainloop()



