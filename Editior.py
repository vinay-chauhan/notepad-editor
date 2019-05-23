from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext

root =Tk(className='|--Garibon ka Text Editor--|')
root.geometry('450x500')
textpad = scrolledtext.ScrolledText(root, width=100, height=80)

def open_command():
    file = filedialog.askopenfile(parent=root, mode='rb', title='select a file')
    if file !=None:
        contents=file.read()
        textpad.insert('1.0',contents)
        file.close()

def save_command():
    file = filedialog.asksaveasfile(mode='w')
    if file != None:
        data = textpad.get('1.0',END +'-1c')
        file.write(data)
        file.close()

def exit_command():
    if messagebox.askyesno('Do you want to Exit',
                              'if you quit you will come on road'):
        root.destroy()

def about_command():
    label = messagebox.showinfo('About','This Editor is created by vinay')

def ref():
    root.geometry('225x250')
    print('your window size smallied')

def b2n():
    root.geometry('450x500')
    print('your window is normalised')

menu = Menu(root)
root.config(menu = menu)

filemenu = Menu(menu)
menu.add_cascade(label='File',menu=filemenu)

filemenu.add_command(label='New')
filemenu.add_command(label='open',command=open_command)
filemenu.add_command(label='Save',command=save_command)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=exit_command)
filemenu.add_separator()

filemenu2 = Menu(menu)
menu.add_cascade(label='Edit',menu=filemenu2)
filemenu2.add_command(label='Copy Ctrl+c')
filemenu2.add_command(label='Paste Ctrl+v')
filemenu2.add_separator()
filemenu2.add_command(label='Undo Ctrl+z')
filemenu2.add_command(label='Select all Ctrl+a')
filemenu2.add_separator()

filemenu3 = Menu(menu)
menu.add_cascade(label='Option',menu=filemenu3)
filemenu3.add_command(label='Resize window',command = ref)
filemenu3.add_command(label='Back to Normal',command = b2n)
filemenu3.add_separator()

menu.add_cascade(label='Navigate')
menu.add_cascade(label='Code')

helpmenu = Menu(menu)
menu.add_cascade(label='help',menu=helpmenu)
helpmenu.add_command(label='About...',command=about_command)

textpad.pack()
root.mainloop()
