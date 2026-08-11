#search engine
text=input("Enter the text: ")
word=input("Enter the word: ")

def searchEngine(x,y):
    if y in x:
        return "Word found!"
    else:
        return "Word not found!"
print(searchEngine(text,word))