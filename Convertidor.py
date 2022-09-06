from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox

window = Tk()
window.title("Convertidor")
window.geometry("400x400")
window.resizable(False,False)
s = ttk.Style()
s.theme_use('clam')

table = ttk.Treeview(window,columns=("c1","c2"), show='headings', height=6)
table.column("# 1", anchor=CENTER)
table.heading("# 1", text="Base")
table.column("# 2", anchor=CENTER)
table.heading("# 2", text="Valor")

label1 = Label(window, text='Ingrese un número octal de 4 bits: ')
label1.pack()
entry1 = Entry(window)
entry1.pack()
label1.config(font=('helvetica', 12))


def clear_all():
   for item in table.get_children():
      table.delete(item)

def convertidor():

    clear_all()
    num = entry1.get()
    #n1 es el octal convertido a decimal
    n1 = octal_a_decimal(num)
    n2 = decimal_a_binario(n1)
    n3 = decimal_a_hexadecimal(n1)

    table.insert("", END, text="Decimal",values=("Decimal", str(n1)))
    table.insert("", END, text="Binario",values=("binario", str(n2)))
    table.insert("", END, text="Hexadecimal",values=("Hexadecimal", str(n3)))
    table.pack()

def octal_a_decimal(octal):
    decimal = 0
    posicion = 0
    # Invertir octal, porque debemos recorrerlo de derecha a izquierda
    # pero for in empieza de izquierda a derecha
    octal = octal[::-1]
    for digito in octal:
        if int(digito) == 8:
            MessageBox.showwarning("Error", "El número ingresado no es octal")
            return
        elif posicion > 3:
            MessageBox.showwarning("Error", "El número ingresado no es de 4 bits")
            return
        else:
            valor_entero = int(digito)
            numero_elevado = int(8 ** posicion)
            equivalencia = int(numero_elevado * valor_entero)
            decimal += equivalencia
        posicion += 1

    return decimal

def obtener_caracter_hexadecimal(valor):
    # Lo necesitamos como cadena
    valor = str(valor)
    equivalencias = {
        "10": "A",
        "11": "B",
        "12": "C",
        "13": "D",
        "14": "E",
        "15": "F",
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor


def decimal_a_hexadecimal(decimal):
    hexadecimal = ""
    while decimal > 0:
        residuo = decimal % 16
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        decimal = int(decimal / 16)
    return hexadecimal


def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    # Aquí almacenamos el resultado
    binario = ""
    # Mientras se pueda dividir...
    while decimal > 0:
        # Saber si es 1 o 0
        residuo = int(decimal % 2)
        # E ir dividiendo el decimal
        decimal = int(decimal / 2)
        # Ir agregando el número (1 o 0) a la izquierda del resultado
        binario = str(residuo) + binario
    return binario

button1 = Button(text='Convertir', command=convertidor, bg='brown', fg='white',font=('helvetica', 10, 'bold'))
button1.pack()


window.mainloop()