import tkinter as tk
import sqlite3

def guardar_producto():
    producto = entry_producto.get()
    if producto:
        conn = sqlite3.connect('Mibasededatosdea.db')
        cursor = conn.cursor()

        # Buscar si el producto ya existe en la base de datos
        cursor.execute("SELECT * FROM productos WHERE nombre=?", (producto,))
        resultado = cursor.fetchone()

        if resultado:
            # Si el producto existe, incrementar la cantidad en 1
            cantidad_actual = resultado[2]
            cantidad_nueva = cantidad_actual + 1
            cursor.execute("UPDATE productos SET cantidad=? WHERE id=?", (cantidad_nueva, resultado[0]))
        else:
            # Si el producto no existe, insertar un nuevo registro
            cursor.execute("INSERT INTO productos (nombre) VALUES (?)", (producto,))
        
        conn.commit()
        conn.close()

        # Limpiar el cuadro de entrada
        entry_producto.delete(0, tk.END)

def cargar_productos():
    # Cargar los productos desde la base de datos y mostrarlos en la lista
    conn = sqlite3.connect('Mibasededatosdea.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM productos")
    productos = cursor.fetchall()
    conn.close()
    
    for producto in productos:
        lista_productos.insert(tk.END, producto[0])

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ingreso de Productos")

# Etiqueta y cuadro de entrada para ingresar el producto
label_producto = tk.Label(ventana, text="Producto:")
label_producto.pack()

entry_producto = tk.Entry(ventana)
entry_producto.pack()

# Botón para guardar el producto en la lista y en la base de datos
boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_producto)
boton_guardar.pack()

# Lista para mostrar los productos ingresados
lista_productos = tk.Listbox(ventana)
lista_productos.pack()

# Cargar los productos desde la base de datos al iniciar la aplicación
cargar_productos()

ventana.mainloop()
