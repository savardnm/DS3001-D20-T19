import tkinter as tk
import pandas as pd
import numpy as np
from PIL import Image, ImageTk
import requests
from io import BytesIO
import io
import urllib.parse

books = pd.read_csv('raw-data/books.csv')
tags =pd.read_csv('filtered-data/final-output.csv')
tags['user_input'] = 3.01


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
    
    
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(text="Select Genres You Have Read")
       label.grid(in_=self, column=3, row=0)
       i=0
       for index, row in tags.iterrows():
           button=tk.Button(self,text=row['tag_name'], fg = 'black', background = 'white')
           button.configure(command=lambda b=button: self.toggle(b))
           button.grid(column=i%7,row=int(i/7)+1)
           root.grid_columnconfigure(0,weight=1)
           i+=1
           
   def toggle(self, Button):
       i_row = np.where(tags['tag_name']== Button['text'])[0][0]
       print(tags.iloc[i_row])
       if(tags.iloc[i_row]['user_input']==3.01):
           tags.at[i_row, 'user_input']=3.1
           Button.configure(fg = 'black', background = 'dodgerblue')
       else:
           tags.at[i_row, 'user_input']=3.01
           Button.configure(fg = 'black', background = 'white')
       pass
   
class Page2(Page):
    
           
    elements = []
    
    def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(text="Rate the Genres You Have Read")
       label.grid(in_=self, column =0,row=0)
       pass
    def show(self):
       Page.show(self)
       for element in self.elements:
           element.destroy()
           pass
       i = 1
       for index, row in tags.iterrows():
           if (row['user_input']!=3.01):
               label=tk.Label(text=row["tag_name"])
               scale=tk.Scale(self, from_=1, to=5, resolution = 0.5, orient=tk.HORIZONTAL)
               self.elements.append(scale)
               self.elements.append(label)
               label.grid(in_=self, column = 0, row = i)
               scale.grid(in_=self, column = 1, row = i)
               root.grid_columnconfigure(0,weight=1)
               i+=1
               pass
       #label.pack(side="top", fill="both", expand=True)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.image1 = self.getImage(url=books.iloc[0]['image_url'])
       self.image2 = self.getImage(url=books.iloc[1]['image_url'])
       self.image3 = self.getImage(url=books.iloc[2]['image_url'])
       label1 = tk.Label(self, image=self.image1)
       label2 = tk.Label(self, image=self.image2)
       label3 = tk.Label(self, image=self.image3)
       label4 = tk.Label(self, text="book1")
       label5 = tk.Label(self, text="book2")
       label6 = tk.Label(self, text="book3")
       label1.grid(column=1, row=0)
       label2.grid(column=3, row=0)
       label3.grid(column=5, row=0)
       label4.grid(column=1, row=1)
       label5.grid(column=3, row=1)
       label6.grid(column=5, row=1)
       pass

   def getImage(self, url):
       cover = url
       raw_data = urllib.request.urlopen(cover).read()
       im = Image.open(io.BytesIO(raw_data))
       return ImageTk.PhotoImage(im)
        
class MainView(tk.Frame):
    page = 0
    
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.p1 = Page1(self)
        self.p2 = Page2(self)
        self.p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        self.p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        next_btn = tk.Button(buttonframe, text="Next", command = self.next_page, background = "dodgerblue")
        back_btn = tk.Button(buttonframe, text="Back", command = self.back_page, background = "dodgerblue") 
        b1 = tk.Button(buttonframe, text="Page 1", command=self.p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=self.p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=self.p3.lift)

        next_btn.pack(in_=buttonframe, side="right")
        back_btn.pack(in_=buttonframe, side="right")

        self.p1.show()
        

    def next_page(self):
        if(self.page == 0):
            self.p2.show()
        if(self.page == 1):
            self.p3.show()
        self.page = min(self.page+1, 2)
    def back_page(self):
        if(self.page == 1):
            self.p1.show()
        if(self.page == 2):
            self.p2.show()
        self.page = max(self.page-1, 0)
    

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    root.state('zoomed')
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()