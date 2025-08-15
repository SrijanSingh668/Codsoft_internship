#To Do List
from tkinter import*
from tkinter import messagebox

#Function opening secondwindow
def second_window(task_listbox):
    r =Tk()
    r.title("Add Task")
    r.geometry("300x100")
    label1=Label(r,text="Enter the task",font=("Times New Roman",20))
    text_box=Text(r,height=4,width=30)
    text_box.pack()

    #function add text/task to main window
    def entry_text():
        task = text_box.get("1.0",END).strip()
        if task:
            task_listbox.insert(END, task)
            r.destroy()
        else:
            messagebox.showwarning("Empty Task", "Please enter a task!")
    
    add_button=Button(r,text="Add This task",command=entry_text)
    add_button.place(x=40,y=80)
    
#Function to remove task
def remove():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected)
    else:
        messagebox.showwarning("No selection", "Please select a task to remove.")

#Function to mark the task 
def completed_task():
    selected = task_listbox.curselection()
    if selected:
        task = task_listbox.get(selected)
        task_listbox.delete(selected)
        task_listbox.insert(END, f"[✓] {task}")
    else:
        messagebox.showwarning("No selection","Please select a task to remove.")

        
#The main window
        
window =Tk()
window.title("TO DO List")
window.geometry("500x400")

imagebg=PhotoImage(file="background image.png")
bg=Label(window,image=imagebg)
bg.place(relheight=1,relwidth=1)

label= Label(window,text="To Do List",font=("Script",35),bg="black",fg="white")
label.pack()

frame =Frame(window)
frame.pack()

scrollbar =Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

task_listbox = Listbox(frame, width=25, height=10, font=("Arial", 14), yscrollcommand=scrollbar.set)
task_listbox.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=task_listbox.yview)

button1 =Button(window,text="Add Task",command=lambda : second_window(task_listbox),bg="black",fg="yellow")
button1.place(x=405,y=80)
button2=Button(window,text="Remove Task",command=remove,bg="black",fg="yellow")
button2.place(x=405,y=180)
button3=Button(window,text="Mark Completed",command=completed_task,bg="black",fg="yellow")
button3.place(x=405,y=280)

window.mainloop()
