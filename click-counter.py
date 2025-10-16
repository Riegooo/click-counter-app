from tkinter import *
from tkinter import messagebox

count = 0

def click():
    global count
    count += 1
    count_label.config(text=f"Click count: {count}")

def resetClick():  
    global count
    confirm = messagebox.askyesno("Reset Confirmation", "Are you sure you want to reset the count?")
    if confirm:
        count = 0
        count_label.config(text=f"Click count: {count}")

def exitApp():
    confirm = messagebox.askyesno("Exit App", "Do you really want to close the app?")
    if confirm:
        window.destroy()

window = Tk()
window.title("Click Counter App 🖱️")
window.geometry('400x450')
window.configure(bg="#222")


title_label = Label(window, 
                    text="🖱️ Click Counter", 
                    font=('Comic Sans MS', 20, 'bold'),
                    fg="white", 
                    bg="#222")
title_label.pack(pady=15)

count_label = Label(window, 
                    text=f"Click count: {count}", 
                    font=('Comic Sans MS', 18),
                    fg="yellow", 
                    bg="#222")
count_label.pack(pady=10)

button = Button(window,
                text='Click Me!',
                command=click,
                width=20,
                height=2,
                fg='white',
                bg='green',
                font=('Comic Sans MS', 14, 'bold'),
                relief=RAISED,
                bd=8,
                activeforeground='yellow',
                activebackground='#006400')
button.pack(pady=10)

click_reset = Button(window,
                    text='Reset Count',
                    command=resetClick,
                    width=20,
                    height=2,
                    fg='white',
                    bg='red',
                    font=('Comic Sans MS', 14, 'bold'),
                    relief=RAISED,
                    bd=8,
                    activeforeground='yellow',
                    activebackground='#8B0000')
click_reset.pack(pady=10)

exit_button = Button(window,
                    text='Exit App',
                    command=exitApp,
                    width=20,
                    height=2,
                    fg='white',
                    bg='gray',
                    font=('Comic Sans MS', 14, 'bold'),
                    relief=RAISED,
                    bd=8,
                    activeforeground='black',
                    activebackground='silver')
exit_button.pack(pady=10)

window.mainloop()
