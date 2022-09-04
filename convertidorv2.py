from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox

window = Tk()
window.title("Convertidor")
window.geometry("400x400")
window.resizable(False,False)

table =ttk.Treeview(window,columns=("Decimal","Binario","Hexadecimal"))

label1 = Label(window, text='Ingrese un número octal de 4 bits: ')
label1.pack()
entry1 = Entry(window)
entry1.pack()
label1.config(font=('helvetica', 12))



table.insert("",END,text="Numero octal",values=("4","2","8"))
#table.place(x=50,y=75)
table.pack()
def convertidor():

    num = entry1.get()
    #n1 es el octal convertido a decimal
    n1 = octal_a_decimal(num)
    n2 = decimal_a_binario(n1)
    n3 =decimal_a_hexadecimal(n1)

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
        else:
            valor_entero = int(digito)
            numero_elevado = int(8 ** posicion)
            equivalencia = int(numero_elevado * valor_entero)
            decimal += equivalencia
            label4 = Label(window, text=f"El número {entry1.get()} equivale a {decimal} en decimal", font=('helvetica', 10))
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
    label5 = Label(window, text=f"El número {entry1.get()} equivale a {hexadecimal} en hexadecimal", font=('helvetica', 10))
    #canvas2.create_window(200, 210, window=label5)
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
    label6 = Label(window, text=f"El número {entry1.get()} equivale a {binario} en binario", font=('helvetica', 10))
    #canvas2.create_window(200, 210, window=label6)
    return

button1 = Button(text='Convertir', command=octal_a_decimal, bg='brown', fg='white',
                    font=('helvetica', 10, 'bold'))
button1.pack()


window.mainloop()