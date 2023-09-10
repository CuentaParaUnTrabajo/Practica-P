
import sqlite3

# Conectar a la base de datos o crearla si no existe
conn = sqlite3.connect('Mibasededatosdea.db')
cursor = conn.cursor()

# Modificar la tabla para incluir la columna "cantidad"
cursor.execute('''CREATE TABLE IF NOT EXISTS productos
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT NOT NULL,
                   cantidad INTEGER DEFAULT 1)''')

conn.commit()
conn.close()