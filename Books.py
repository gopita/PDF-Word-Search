#Importing libraries
import PyPDF2 as pdf
import glob
from tkinter import * 

root = Tk() #GUI interface

e = Entry(root, width=50) #Creates search bar
e.pack()


def getWord():
    file_list = glob.glob("C:/Users/User/Documents/BooksPDF/*.pdf") #Location of PDF files

    counter_2 = 0

    word = e.get() #gets word or sentence from user

    #for loop to open pdf files one by one
    for pdfs in file_list:
        pd = pdf.PdfFileReader(pdfs)

        num_pages = pd.getNumPages() 

        total = int(num_pages)

        lista = []

        counter = 0

        name = file_list[counter_2]

        #append all the pages from the book in a list 
        while total > 0:
            novo = total - total + counter
            lista.append(novo)
            counter += 1
            total = total - 1

        #for every page in the list search for the word or sentence the user has typed
        for page in lista:
            x = pd.getPage(page)
            texto = x.extractText()
            if word == "":
                break
            if word.lower() in texto.lower():
                y = page + 1
                myLabel = Label(root, text="pg." + str(y) + " - " + name) #Display book name and page number that contains the word or sentence the user has typed
                myLabel.pack()
        counter_2 += 1



myButton = Button(root, text="Search", command=getWord) #Creates search button
myButton.pack()

root.mainloop()