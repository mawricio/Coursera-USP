from tkinter import *
def calculates():
    which_button = selected_operation.get()
    value_1 = float(entry_field_1.get())
    value_2 = float(entry_field_2.get())
    if which_button == 1:
        resultado = value_1 + value_2
    elif which_button == 2:
        resultado = value_1 - value_2
    elif which_button == 3:
        resultado = value_1 * value_2
    elif which_button == 4:
        resultado = value_1 / value_2
    result_field.delete(0, END)
    result_field.insert(0, resultado)


root = Tk()
root.title('calculadora rústica')
window_title = Label(root, text='calculadora rústica', font=('Helvetica', 18)).grid(row=0, column=0, columnspan=2)
label_1 = Label(root, text='Digite um número').grid(row=1, column=0)
entry_field_1 = Entry(root, text='Número 1', width=10)
entry_field_1.grid(row=1, column=1)
label_2 = Label(root, text='Digite outro número').grid(row=2, column=0)
entry_field_2 = Entry(root, text='Número 2', width=10)
entry_field_2.grid(row=2, column=1)
selected_operation = IntVar()

label_3 = Label(root, text='Escolha a operação desejada').grid(row=3, column=0, columnspan=2)

sum_button = Radiobutton(root, text='+', variable=selected_operation, value=1)
sum_button.grid(row=4, column=0)

subtraction_button = Radiobutton(root, text='-', variable=selected_operation, value=2)
subtraction_button.grid(row=4, column=1)

multiplication_button = Radiobutton(root, text='x', variable=selected_operation, value=3)
multiplication_button.grid(row=5, column=0)

division_button = Radiobutton(root, text='/', variable=selected_operation, value=4)
division_button.grid(row=5, column=1)

botao = Button(root, text='Calcular operação', command=calculates, width='30').grid(row=6, column=0, columnspan=2)

label_3 = Label(root, text='Resultado').grid(row=7, column=0)
result_field = Entry(root)
result_field.grid(row=7, column=1)
root.mainloop()