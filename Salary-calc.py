import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

def add():
    pass


def salary():
    wage = int(entry1.get())
    hours = float(entry2.get())
    night_hours = int(entry3.get())
    bonus = wage * 0.3
    price_hours = wage / hours
    price_night_hours = price_hours * night_hours * 0.2
    my_salary = round((wage + bonus  + price_night_hours), 2)
    clear_salary = round((my_salary * 0.87), 2)
    label5.configure(text= my_salary)
    label6.configure(text=clear_salary)


window = tk.Tk()
window.title('Salary-Calc',)
window["bg"] = "Orange"



style = ThemedStyle(window)
style.set_theme('kroc')

label1 = ttk.Label(master=window, text="Enter the salary", font = ("Arial Bold",10))
entry1 = ttk.Entry(master=window)
label1.pack()
entry1.pack()

label2 = ttk.Label(master=window, text="Enter the number of hours", font = ("Arial Bold",10))
entry2 = ttk.Entry(master=window)
label2.pack()
entry2.pack()

label3 = ttk.Label(master=window, text="Enter the number of nights", font = ("Arial Bold",10))
entry3 = ttk.Entry(master=window)
label3.pack()
entry3.pack()


but_add = ttk.Button(master=window, text="Add overtime", command=add)
label_add = ttk.Label(master=window, text="Overtime")
but_add.pack()
label_add.pack()

but_salary = ttk.Button(master=window, text="Calculate the salary", command=salary)
label5 = ttk.Label(master=window, text="Salary", font = ("Arial Bold",15))
but_salary.pack()
label5.pack()
label6 = ttk.Label(master=window, text="Clean salary", font = ("Arial Bold",15))
label6.pack()

but_quit = ttk.Button(master=window, text="Quit", command=window.destroy)
but_quit.pack()

window.geometry('300x350')
# window.resizable(False, False)
window.mainloop()
