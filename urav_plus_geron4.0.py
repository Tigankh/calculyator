from tkinter import *
from math import sqrt
from math_func import *


# функции для  квадратное уравнение !!!
def inseter(value):
    # удаляет значение ответа из output
    output.delete('0.0', END)
    output.insert('0.0', value)


def delete_entry():
    first_entry.delete(0, END)
    two_entry.delete(0, END)
    three_entry.delete(0, END)
    a_kub_entry.delete(0, END)
    a.delete(0, END)
    b.delete(0, END)
    c.delete(0, END)
    a_par_entry.delete(0, END)
    b_par_entry.delete(0, END)
    c_par_entry.delete(0, END)


def handler():
    try:
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        inseter(solver(a_val, b_val, c_val))
    except ValueError:
        inseter('Убедитесь что ввели 3 числа')


def calculator_kv_urav():
    """все гриды калькулятора квадратных уравнений"""
    root.title('квадратное уравнение')
    lab_text1.configure(text='test 1 text 1')
    lab_text2.configure(text='test 2 text 2')
    lab_text1.grid(row=0, column=0, columnspan=8)
    lab_text2.grid(row=1, column=0, columnspan=8)
    delete_entry()
    s_lab.grid(row=2, column=0)
    a.grid(row=2, column=1)
    a_lab.grid(row=2, column=2)
    b.grid(row=2, column=3)
    b_lab.grid(row=2, column=4)
    c.grid(row=2, column=5)
    c_lab.grid(row=2, column=6)
    btn.grid(row=2, column=7)
    output.grid(row=3, column=0, columnspan=8)

    forget_geron()
    forget_kub()
    inseter('')


def forget_kv_urav():
    """удаляет все графические элементы для квадратного уравнения"""
    a.grid_forget()
    b.grid_forget()
    c.grid_forget()
    a_lab.grid_forget()
    b_lab.grid_forget()
    c_lab.grid_forget()
    btn.grid_forget()
    output.grid_forget()
    lab_text2.grid_forget()
    lab_text1.grid_forget()


# ========================================================================

# функции для герона!!!!

flag_geron_or_par = True  # если True, то герон, если False, то паралелепипед


def otvet_geron_func():
    a = float(first_entry.get())
    b = float(two_entry.get())
    c = float(three_entry.get())
    # print(a, b, c)
    if flag_geron_or_par == True:
        if proverka_geron(a, b, c) == False:
            inseter('такого треугольника не существует ')
        else:
            result = geron_func(a, b, c)
            inseter(result)
    elif flag_geron_or_par == False:
        inseter(para_calculyator(a, b, c))


def treug_func():
    """доработать, пока что только удаляет кв уравнение"""
    global flag_geron_or_par
    flag_geron_or_par = True
    root.title('герон треугольник')
    lab_text1.configure(text='Площадь треугольника по трём сторонам')
    lab_text2.configure(text='Введите значения')
    forget_kv_urav()
    forget_kub()
    forget_para()
    delete_entry()
    lab_text1.grid(row=0, column=0, columnspan=8)
    lab_text2.grid(row=1, column=0, columnspan=8)
    s_lab.grid(row=2, column=0, columnspan=1)
    first_entry.grid(row=2, column=1, columnspan=1)
    first_lab.grid(row=2, column=2, columnspan=1)
    two_entry.grid(row=2, column=3, columnspan=1)
    two_lab.grid(row=2, column=4, columnspan=1)
    three_entry.grid(row=2, column=5, columnspan=1)
    three_lab.grid(row=2, column=6, columnspan=2)
    output.grid(row=3, column=0, columnspan=8)
    btn_geron.grid(row=2, column=7)
    inseter('')


def forget_geron():
    """удаляет все графические элементы для треугольника герон"""
    s_lab.grid_forget()
    first_entry.grid_forget()
    first_lab.grid_forget()
    two_entry.grid_forget()
    two_lab.grid_forget()
    three_entry.grid_forget()
    three_lab.grid_forget()
    btn_geron.grid_forget()


# ==========================================================================


def otvet_kuba():
    kub = int(a_kub_entry.get())
    result = kub_calculyator(kub)
    return inseter(result)
    # inseter(result)


def kub_func():
    forget_geron()
    forget_kv_urav()
    forget_para()
    delete_entry()
    root.title('Калькулятор куба')
    lab_text1.configure(text='test kub 1 text 1')
    lab_text2.configure(text='test kub 2 text 2')
    lab_text1.grid(row=0, column=0, columnspan=8)
    lab_text2.grid(row=1, column=0, columnspan=8)

    a_kub_lab.grid(row=2, column=0, columnspan=3)
    a_kub_entry.grid(row=2, column=3, columnspan=3)
    btn_kub.grid(row=2, column=6, columnspan=3)
    output.grid(row=3, column=0, columnspan=8)
    inseter('')


def forget_kub():
    a_kub_lab.grid_forget()
    a_kub_entry.grid_forget()
    btn_kub.grid_forget()


# ========================================================================================================


# def otvet_para():
#     a2 = first_entry.get()
#     b2 = two_entry.get()
#     c2 = three_entry.get()
#     print('вот это в entry:', a_par_entry, b_par_entry, c_par_entry)
#     result = para_calculyator(a2, b2, c2)
#     inseter(result)


def para_funcs():
    global flag_geron_or_par
    flag_geron_or_par = False
    delete_entry()

    forget_kv_urav()
    forget_kub()
    forget_geron()
    lab_text1.configure(text='test para 1 para 1')
    lab_text2.configure(text='test para 2 para 2')
    lab_text1.grid(row=0, column=0, columnspan=8)
    lab_text2.grid(row=1, column=0, columnspan=8)
    a_par_lab.grid(row=2, column=0)
    first_entry.grid(row=2, column=1)
    b_par_lab.grid(row=2, column=2)
    two_entry.grid(row=2, column=3)
    c_par_lab.grid(row=2, column=4)
    three_entry.grid(row=2, column=5)
    btn_para_otvet.grid(row=2, column=6)
    output.grid(row=3, column=0, columnspan=14)
    inseter('')


def forget_para():
    a_par_lab.grid_forget()
    a_par_entry.grid_forget()
    b_par_lab.grid_forget()
    b_par_entry.grid_forget()
    c_par_lab.grid_forget()
    c_par_entry.grid_forget()
    btn_para_otvet.grid_forget()


# ========================================================================================================
# def choice():
#     if btn_geron == False:
#         treug_func()
#     else:
#         calculator_kv_urav()

root = Tk()
root.title('Calculyator')
root.geometry('470x300+300+300')
root.resizable(width=False, height=False)

# =========================================================================================
# Площадь треугольника по трём сторонам
lab_text1 = Label(root, text=('Площадь треугольника по трём сторонам'), font=('Arial 12'))
lab_text2 = Label(root, text='Введите значения', font='Arial 12')

s_lab = Label(root, text='S =', width=5, font='Arial 12')

first_entry = Entry(root, font='Arial 12', width=5)
first_lab = Label(root, text='x', font='Arial 12')

two_entry = Entry(root, font='Arial 12', width=5)
two_lab = Label(root, text='x', font='Arial 12')

three_entry = Entry(root, font='Arial 12', width=5)
three_lab = Label(root, text='x2', font='Arial 12')

btn_geron = Button(root, text='Otvet', command=otvet_geron_func)

# ===================================================================================================
# для калькулятора квадратных уранений все entry, label and button


a = Entry(root, width=5, font='Arial 12')
# a.pack(side=LEFT, pady=10, padx=10)

a_lab = Label(root, text='x^2 +', font='Arial 12')  # .pack(side=LEFT, pady=10)

b = Entry(root, width=5, font='Arial 12')
# b.pack(side=LEFT, pady=10)

b_lab = Label(root, text='x +', font='Arial 12')  # .pack(side=LEFT, pady=10)

c = Entry(root, width=5, font='Arial 12')
# c.pack(side=LEFT, pady=10)

c_lab = Label(root, text='= 0', font='Arial 12')  # .pack(side=LEFT, pady=10)

btn = Button(root, text='Solve', font='Arial 12', command=handler)  # .pack(side=LEFT, pady=10, padx=10)
output = Text(root, font='Arial 12', fg='white', bg='green', width=44, height=5)
# output.pack(expand=1, fill=BOTH, side=LEFT)

# ============================================================================================

# площадь куба
a_kub_lab = Label(root, text='Введите стoрону куба', font='Arial 12')

a_kub_entry = Entry(root, width=15, font='Arial 12')

btn_kub = Button(root, text='посчитать', command=otvet_kuba, font='Arial 12')

# ================================================================================================

# Объем параллелепипеда
a_par_lab = Label(root, text='V =', font='Arial 12')
a_par_entry = Entry(root, width=7, font='Arial 12')

b_par_lab = Label(root, text='*', font='Arial 15')
b_par_entry = Entry(root, width=7, font='Arial 12')

c_par_lab = Label(root, text='*', font='Arial 15')
c_par_entry = Entry(root, width=7, font='Arial 12')

btn_para_otvet = Button(root, text='Ответ', command=otvet_geron_func, font='Arial 12')

# ================================================================================================


# menu
btn_treug_menu = Button(root, text='герон (треугольник)', font='Arial 12', fg='black', bg='orange', command=treug_func)
btn_treug_menu.grid(row=10, column=2, columnspan=4)

btn_kv_urav_menu = Button(root, text='квадратное уравнение', font='Arial 12', fg='black', bg='orange',
                          command=calculator_kv_urav)
btn_kv_urav_menu.grid(row=11, column=2, columnspan=4)

btn_kub_menu = Button(root, text='Площадь куба', fg='black', bg='orange', command=kub_func, font='Arial 12')
btn_kub_menu.grid(row=12, column=2, columnspan=4)

btn_para_menu = Button(root, text='Объем параллелепипеда', command=para_funcs, fg='black', bg='orange', font='Arial 12')
btn_para_menu.grid(row=13, column=2, columnspan=4)

root.mainloop()
