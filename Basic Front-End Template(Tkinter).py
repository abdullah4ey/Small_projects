from tkinter import*
import tkinter.messagebox


def disable_event():
    tkinter.messagebox.showinfo("Warning!","This action can only be perform by Admin ")
    pass
windows=Tk()
windows.geometry('375x420+500+110')
windows.resizable(width=False, height=False)
windows.resizable(0,0)
#windows.overrideredirect(1)
windows.title('Sign in system')
#windows.protocol("WM_DELETE_WINDOW", disable_event)
mainMenu=Menu(windows)
windows.configure(menu=mainMenu)
subMenu=Menu(mainMenu)
mainMenu.add_cascade(label="Extra", menu= subMenu)
subMenu.add_command(label= "Registration")#,command=register)
subMenu.add_command(label= "Access Details")#,command=access_file)
subMenu.add_command(label= "Quit")#,command=Administrator)




windows.title('Sign in system')


Tops= Frame(windows, width=500,height=15,bg='red',relief=SUNKEN)
Tops.pack(side=TOP)
photo =PhotoImage(file='London-Academy.png')
labl=Label(windows, image=photo)
labl.pack(side=TOP)
lablinfo=Label(windows,font=('Calibri (Body)',20,'bold'),text="Sign in",fg='black',bd=10)
lablinfo.pack(side=TOP)
labl1info=Label(windows,font=('Calibri (Body)',12),text="Using your employee's ID",fg='black',bd=10)
labl1info.pack(side=TOP)
f1 =Frame(windows, width =375, height= 300,relief=SUNKEN)
f1.pack(side=LEFT)
labl1=Label(f1,font=('Calibri (Body)',12),text="User Name:",fg='black',bd=10)
labl1.grid(row=0,column=0, padx=10, pady=10, sticky="w")
labl12=Label(f1,font=('Calibri (Body)',12),text="Password:",fg='black',bd=10)
labl12.grid(row=1,column=0, padx=10, pady=10, sticky="w")
labelentry1 = Entry(f1)
labelentry1.grid(row=0,column=3, padx=10, pady=10, sticky="w")
labelentry2 = Entry(f1)
labelentry2.grid(row=1,column=3, padx=10, pady=10, sticky="w")
btn =Button(f1, text="Sign in",font=('Calibri (Body)',12),fg='black',bd=10)#,command=signing_in)
btn.grid(row=3,column=3, padx=10, pady=10, sticky="w")
btn1 =Button(f1,font=('Calibri (Body)',12),text="Sign out",fg='black',bd=10)#,command=sign_out)
btn1.grid(row=3,column=6, padx=10, pady=10, sticky="w")
windows.mainloop()
