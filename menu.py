from tkinter import *
import validaciones

ventana = Tk()

ventana.minsize(300, 200)
ventana.eval('tk::PlaceWindow . center')
ventana.title("Validación de libros")

Label(ventana, text="Libro: ").grid(row=0, sticky="e")
libro = Entry(ventana)
libro.grid(row=0, column=1)
libro_valido = Label(ventana, text="Incorrecto")
libro_valido.grid(row=0, column=3, sticky="e")

Label(ventana, text="Autor: ").grid(row=1, sticky="e")
autor = Entry(ventana)
autor.grid(row=1, column=1)
autor_valido = Label(ventana, text="Incorrecto")
autor_valido.grid(row=1, column=3, sticky="e")


Label(ventana, text="Editorial: ").grid(row=2, sticky="e")
editorial = Entry(ventana)
editorial.grid(row=2, column=1)
editorial_valido = Label(ventana, text="Incorrecto")
editorial_valido.grid(row=2, column=3, sticky="e")

Label(ventana, text="Fecha").grid(row=3, sticky="e")
fecha = Entry(ventana)
fecha.grid(row=3, column=1)
fecha_valido = Label(ventana, text="Incorrecto")
fecha_valido.grid(row=3, column=3, sticky="e")

Label(ventana, text="Precio: ").grid(row=4, sticky="e")
precio = Entry(ventana)
precio.grid(row=4, column=1)
precio_valido = Label(ventana, text="Incorrecto")
precio_valido.grid(row=4, column=3, sticky="e")

Label(ventana, text="Cantidad: ").grid(row=5, sticky="e")
cantidad = Entry(ventana)
cantidad.grid(row=5, column=1)
cantidad_valido = Label(ventana, text="Incorrecto")
cantidad_valido.grid(row=5, column=3, sticky="e")

Label(ventana, text="ISBN: ").grid(row=6, sticky="e")
isbn = Entry(ventana)
isbn.grid(row=6, column=1)
isbn_valido = Label(ventana, text="Incorrecto")
isbn_valido.grid(row=6, column=3, sticky="e")


def actualizar():
    libro_valido.configure(text="Si") if validaciones.validar_titulo(libro.get()) else libro_valido.configure(text="No")
    autor_valido.configure(text="Si") if validaciones.validar_autor(autor.get()) else autor_valido.configure(text="No")
    editorial_valido.configure(text="Si") if validaciones.validar_titulo(editorial.get()) else editorial_valido.configure(text="No")
    fecha_valido.configure(text="Si") if validaciones.validar_fecha(fecha.get()) else fecha_valido.configure(text="No")
    precio_valido.configure(text="Si") if validaciones.validar_precio(precio.get()) else precio_valido.configure(text="No")
    cantidad_valido.configure(text="Si") if validaciones.validar_cantidad(cantidad.get()) else cantidad_valido.configure(text="No")
    isbn_valido.configure(text="Si") if validaciones.validar_isbn(isbn.get()) else isbn_valido.configure(text="No")

    ventana.after(500, actualizar)


ventana.after(500, actualizar)

ventana.mainloop()
