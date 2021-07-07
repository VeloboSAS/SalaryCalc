import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle


def increase():
    value = int(lbl_add["text"])
    lbl_add["text"] = f"{value + 1}"


def decrease():
    value = int(lbl_add["text"])
    lbl_add["text"] = f"{value - 1}"


def salary():
    wage = int(entry1.get())
    hours = float(entry2.get())
    night_hours = int(entry3.get())
    bonus = wage * 0.3
    price_hours = wage / hours
    price_night_hours = price_hours * night_hours * 0.2
    count_overtime = int(lbl_add["text"])
    price_overtime = count_overtime * 12 * 2 * price_hours
    my_salary = round((wage + bonus  + price_night_hours + price_overtime), 2)
    clear_salary = round((my_salary * 0.87), 2)
    label5.configure(text= my_salary)
    label6.configure(text=clear_salary)



window = tk.Tk()
window.title('Salary-Calc',)
window["bg"] = "Orange"



style = ThemedStyle(window)
style.set_theme('kroc')

f_one = tk.Frame(window, bg="Orange")
label1 = tk.Label(master=f_one, text="Enter the salary", bg="Orange", fg="Indigo",  font = ("Arial Bold",12))
entry1 = tk.Entry(master=f_one, justify=tk.CENTER, fg="Indigo", bd=5, relief=tk.RIDGE)

label2 = tk.Label(master=f_one, text="Enter the number of hours", bg="Orange", fg="Indigo", font = ("Arial Bold",12))
entry2 = tk.Entry(master=f_one, justify=tk.CENTER, fg="Indigo", bd=5, relief=tk.RIDGE)

label3 = tk.Label(master=f_one, text="Enter the number of nights", bg="Orange", fg="Indigo", font = ("Arial Bold",12))
entry3 = tk.Entry(master=f_one, justify=tk.CENTER, fg="Indigo", bd=5, relief=tk.RIDGE)
label_add = tk.Label(master=f_one, text="Overtime", bg="Orange", fg="Indigo", font = ("Arial Bold",12))

f_one.pack()
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
label3.pack()
entry3.pack()
label_add.pack()


f_two = tk.Frame(window, bg="Orange")
btn_decrease = tk.Button(master=f_two, text="-", bg="Thistle", relief=tk.RIDGE, bd=5, width=4, height=1, command=decrease)
lbl_add = tk.Label(master=f_two, text="0", fg="Indigo")
btn_increase = tk.Button(master=f_two, text="+", bg="Thistle", relief=tk.RIDGE, bd=5, width=4, height=1, command=increase)


f_two.pack()
btn_decrease.pack(side=tk.LEFT)
lbl_add.pack(side=tk.LEFT)
btn_increase.pack(side=tk.LEFT)


f_three= tk.Frame(window, bg="Orange")
but_salary = tk.Button(master=f_three, text="Calculate the salary", bg="Thistle", fg="Indigo", relief=tk.RIDGE, font= "Arial 12", bd=5, command=salary)
label5 = tk.Label(master=f_three, text="Salary", bg="Orange", fg="Indigo", font = ("Arial Bold",12))
but_salary.pack()
label5.pack()
label6 = tk.Label(master=f_three, text="Clean salary", bg="Orange", fg="Indigo", font = ("Arial Bold",12))
label6.pack()

but_quit = tk.Button(master=f_three, text="Quit", bg="Thistle", fg="Indigo", relief=tk.RIDGE, font= "Arial 12", bd=5, width=5, height=1, command=window.destroy)
but_quit.pack()

f_three.pack()
but_salary.pack()
label5.pack()
label6.pack()
but_quit.pack()

window.geometry('300x450')
# window.resizable(False, False)
window.mainloop()
