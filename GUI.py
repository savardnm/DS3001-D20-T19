import tkinter as tk
import pandas as pd
import numpy as np
from PIL import Image, ImageTk
import io
import urllib.parse
import recomendation

books = pd.read_csv('raw-data/books.csv')
tags =pd.read_csv('filtered-data/final-output.csv')
tags['user_input'] = 3.0

scales = []



class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
    
    
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(text="Select Genres You Have Read")
       label.grid_forget()
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
       if(tags.iloc[i_row]['user_input']==3.0):
           tags.at[i_row, 'user_input']=3.1
           Button.configure(fg = 'black', background = 'dodgerblue')
       else:
           tags.at[i_row, 'user_input']=3.0
           Button.configure(fg = 'black', background = 'white')
       pass
   
class Page2(Page):
    elements = []
    
    def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(text="Rate the Genres You Have Read")
       label.grid_forget()
       
       label.grid(in_=self, column =0,row=0)
       pass
    def show(self):
       Page.show(self)
       for element in self.elements:
           element.destroy()
           pass
       i = 1
       for index, row in tags.iterrows():
           if (row['user_input']!=3.0):
               label=tk.Label(text=row["tag_name"])
               label.grid_forget()
               scale=tk.Scale(self, from_=1, to=5, resolution = 0.5, orient=tk.HORIZONTAL)
               scale.set(3)
               tup = (row['tag_id'], scale)
               scale.configure(command=lambda t=tup: self.update_values(tup))
               self.elements.append(scale)
               self.elements.append(label)
               label.grid(in_=self, column = 2*int(i/10), row = i%10)
               scale.grid(in_=self, column = 2*int(i/10)+1, row = i%10)
               root.grid_columnconfigure(0,weight=1)
               i+=1
               pass
           pass
       pass
   
       pass
    def hide(self):
       for element in self.elements:
           element.grid_forget()
           pass
       
    def update_values(self, tup):
        value = tup[1].get()
        tag_id = tup[0]
        
        i_row = np.where(tags['tag_id']== float(tag_id))[0][0]
        
        print('changing ', tag_id)
        print('to ', value)
        
        tags.at[i_row, 'user_input']=value
        print(tags)
       #label.pack(side="top", fill="both", expand=True)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.image1 = self.getImage(url=books.iloc[0]['image_url'])
       self.image2 = self.getImage(url=books.iloc[1]['image_url'])
       self.image3 = self.getImage(url=books.iloc[2]['image_url'])
       self.label1 = tk.Label(self, image=self.image1)
       self.label2 = tk.Label(self, image=self.image2)
       self.label3 = tk.Label(self, image=self.image3)
       self.label4 = tk.Label(self, text="book1")
       self.label5 = tk.Label(self, text="book2")
       self.label6 = tk.Label(self, text="book3")
       self.label1.grid(column=1, row=0)
       self.label2.grid(column=3, row=0)
       self.label3.grid(column=5, row=0)
       self.label4.grid(column=1, row=1)
       self.label5.grid(column=3, row=1)
       self.label6.grid(column=5, row=1)
       pass

   def getImage(self, url):
       cover = url
       raw_data = urllib.request.urlopen(cover).read()
       im = Image.open(io.BytesIO(raw_data))
       return ImageTk.PhotoImage(im)
   
   def show(self):
       Page.show(self)
       tag_tuples = [(row['tag_id'], row['user_input']) for index, row in tags.iterrows()]
       cluster = recomendation.get_cluster(tag_tuples)
       print('cluster: ', cluster)
       recommendations = []
       recommendations=recomendation.get_recommendations(cluster)
       print(recommendations[:5])
       
       print(books.loc[books['id']==recommendations[0][0]]['image_url'].iloc[0])
        
       self.image1 = self.getImage(url=books.loc[books['id']==recommendations[0][0]]['image_url'].iloc[0])
       self.image2 = self.getImage(url=books.loc[books['id']==recommendations[1][0]]['image_url'].iloc[0])
       self.image3 = self.getImage(url=books.loc[books['id']==recommendations[2][0]]['image_url'].iloc[0])
       
       self.label1.configure(image=self.image1)
       self.label2.configure(image=self.image2)
       self.label3.configure(image=self.image3)
       self.label4.configure(text=books.loc[books['id']==recommendations[0][0]]['original_title'].iloc[0], wraplength=100)
       self.label5.configure(text=books.loc[books['id']==recommendations[1][0]]['original_title'].iloc[0], wraplength=100)
       self.label6.configure(text=books.loc[books['id']==recommendations[2][0]]['original_title'].iloc[0], wraplength=100)
       
       
       
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

        next_btn.pack(in_=buttonframe, side="right")
        back_btn.pack(in_=buttonframe, side="right")

        self.p1.show()
        

    def next_page(self):
        if(self.page == 0):
            self.p2.show()
        if(self.page == 1):
            self.p2.hide()
            self.p3.show()
        self.page = min(self.page+1, 2)
    def back_page(self):
        if(self.page == 1):
            self.p1.show()
            self.p2.hide()
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