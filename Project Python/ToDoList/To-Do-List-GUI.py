import tkinter
from tkinter import*

root=Tk()
#judul
root.title("Your To-Do List")
#ukuran gui
root.geometry("400x595+400+100")
#mengizinkan resize ukuran gui (lebar, tinggi)
root.resizable(False,False)

task_list= []

#input data
def openTaskFile():
    try: 
        global task_list
        with open("listtugas.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file=open('listtugas.txt', 'w')
        file.close()

#menambahkan data yg diinput ke task_list
def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("listtugas.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)

#menghapus list tugas
def deletetask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("listtugas.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task+'\n')

        listbox.delete(ANCHOR)


#icon
image_icon = PhotoImage(file="Image\gask.png")
root.iconphoto(False, image_icon)

#top bar
top_image = PhotoImage(file="Image\gbar2.png")
Label(root,image=top_image).pack()

heading = Label(root, text="ALL TASK", font="arial 24 bold", fg="white", bg="#FF0075")
heading.place(x=115, y=17)

#main
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=100)
 #input bar
task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

#button add
button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#fc4698", fg="#fff", bd=0, command=addTask)
button.place(x=300, y=0)

#listbox task
frame1 = Frame(root, bd=3, width=700, height=280, bg="#FF0075")
frame1.pack(pady=(98,0))

listbox = Listbox(frame1, font=("arial, 13"), width=40, height=16, bg="#FF0075", fg="white", cursor="hand2", selectbackground="#ea70a7")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

#scroll bar
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

#delete
delete_icon = PhotoImage(file="Image\delete1.png")
Button(root, image=delete_icon, bd=0, command=deletetask).pack(side=BOTTOM, pady=20)


openTaskFile()

#menjalankan apk
root.mainloop()
