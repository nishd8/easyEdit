import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox as mb

import math

linenum=[]
linenum.append(1)
window = tk.Tk()
window.title("easyEdit")

'''openb=tk.Button(window,text="Open")
openb.pack(anchor="w")

saveb=tk.Button(window,text="Save")
saveb.pack()
'''
def file_open():
	editbox.delete("1.0",tk.END)
	line.config(state=tk.NORMAL)
	line.delete("1.0",tk.END)
	line.config(state=tk.DISABLED)
	filename = filedialog.askopenfilename(initialdir="C:/",
                                  title="Select File",
                                  filetypes=(("Text File", "*.txt"),("All Files","*.*")))
	window.title("easyEdit -"+filename)
	with open(filename, 'r') as f:
		lines=f.readlines()
		lines.append("\n")
		num=1.0
		for l in lines:
			editbox.insert(num,l) 
			line.config(state=tk.NORMAL)
			line.insert(float(editbox.index(tk.INSERT))-1,str(int(float(editbox.index(tk.INSERT))-1))+"\t")
			print(float(editbox.index(tk.INSERT))-1)
			line.config(state=tk.DISABLED)
			num+=1
		f.close()
    
def file_save():
    filename=window.title()
    filename=filename.replace('easyEdit -',"")	
    print(filename)
    with open(filename,'w') as f:
    	f.write(editbox.get("1.0",tk.END))
    f.close()
    mb.showinfo("Status","saved!!")

def file_saveas():
	f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
	if f is None:
		return
	text2save = str(editbox.get(1.0,tk.END)) # starts from `1.0`, not `0.0`
	f.write(text2save)
	f.close() # `()` was missing.


menubar=tk.Menu(window)
window.configure(bg="#5a5a5a",menu=menubar)
fileMenu = tk.Menu(menubar)
fileMenu.add_command(label="Open",command=file_open)
fileMenu.add_command(label="Save As",command=file_saveas)
fileMenu.add_command(label="Save",command=file_save)
menubar.add_cascade(label="File", menu=fileMenu)

line=tk.Text(window,bg="#282828",fg="grey",width=5,bd=0,pady=10,font="courier,17",padx=1)
line.pack(side=tk.LEFT,fill=tk.BOTH)
line.config(state=tk.DISABLED)

editbox = tk.Text(window,bd=0,bg="#323232",fg="white",font="courier,17",padx=10,pady=10,insertbackground="white")
editbox.pack(side=tk.LEFT, fill=tk.BOTH, expand =tk.YES)
editbox.tag_configure("current_line",background="#282828")


def multiple_yview(*args):
    line.yview(*args)
    editbox.yview(*args)
scrollbar = tk.Scrollbar(window,bg="white",activebackground="black")
scrollbar.pack( side = tk.RIGHT, fill = tk.Y )
scrollbar.config( command = multiple_yview )


linenums=[]
linenums.append(0.0)
def inclinenum(event):
	print(linenums[0])
	line.config(state=tk.NORMAL)
	if(float(editbox.index(tk.INSERT))-1>linenums[0]):
		line.insert(float(editbox.index(tk.INSERT))-1,str(int(float(editbox.index(tk.INSERT))-1))+"\t")
	else:
		line.delete(float(editbox.index(tk.INSERT))-1,tk.END)

	linenums[0]=float(editbox.index(tk.INSERT))-1
	line.config(state=tk.DISABLED)

	#getline()

def highlight_current_line(interval=100):
        '''Updates the 'current line' highlighting every "interval" milliseconds'''
        editbox.tag_remove("current_line", 1.0, "end")
        editbox.tag_add("current_line", "insert linestart", "insert lineend+1c")
        window.after(interval, highlight_current_line)

highlight_current_line()

window.bind('<Return>',inclinenum)
window.bind('<Control-S>',file_save)
window.mainloop()