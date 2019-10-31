from tkinter import *

from tkinter import filedialog
 

window = Tk()
#file = filedialog.askopenfilename()
window.title("Welcome to LikeGeeks app")
 
window.geometry('1250x600')
#file = filedialog.askopenfilename()
path="C:/Users/maria/.spyder-py3/text.txt"


spin2 = Spinbox(window, from_=0, to=100, width=3)
spin2.grid(column=3,row=0)

lbl = Label(window, text="Hello")
lbl.grid(column=2, row=0)

txt = scrolledtext.ScrolledText(window,width=40,height=10)
txt.grid(column=0,row=1)


txt1 = scrolledtext.ScrolledText(window,width=40,height=10)
txt1.grid(column=1,row=1)
 

def clickspin():
	print(spin3.get())
spin3 = Spinbox(window, values=(3, 8, 11), width=5, command=clickspin)
spin3.grid(column=4, row=0)


def exit():
	print("exit")
	window.destroy()
btn = Button(window, text="Exit", command=exit)
btn.grid(column=6, row=0)


def read():
	path="C:/Users/maria/.spyder-py3/text.txt"
	readFile(path)
	#put data to widget
btn = Button(window, text="Read", command=read)
btn.grid(column=7, row=0)

def save():
	print("save")
	#file = filedialog.askopenfilename()
	files = [('Configuration file', '*.txt')] 
	#path = filedialog.asksaveasfile(filetypes = files, defaultextension = files)
	path="C:/Users/maria/.spyder-py3/text.txt"
	print(path) 
	file = open(path,'w')
	#file.write("..')
	print(spin2.get())
	file.write("\n"+spin2.get()+"\n~")
	file.write("\n"+spin3.get()+"\n~\n")
	file.write(txt.get(1.0,END)+"~\n")
	file.write(txt1.get(1.0,END)+"~")
	file.close()
	
btn = Button(window, text="Save", command=save)
btn.grid(column=8, row=0)

def readFile(path):
	print("read:")
	print(path)
	file=open(path, 'r')
	content = file.read()
	print(content)
	strings=content.split('~')
	
	#strings = string.strip("\n")
	
	print(strings)
	#put data to widget

btn = Button(window, text="Load New", command=lambda : readFile( filedialog.askopenfilename()))
btn.grid(column=9, row=0)

print(spin3.get())

window.mainloop()
	
#btn, read(radio, default, pick file), save 
# random checkbox, textbox
# https://likegeeks.com/python-gui-examples-tkinter-tutorial/
# https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
