import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",  # Cambia por tu usuario en MySQL Workbench
    password="1qazzaq1",  # Cambia por tu contraseña en MySQL Workbench
    port=3306,  # Cambia por el puerto que uses en MySQL Workbench
    database="prueba"
)

cursor = conexion.cursor()

# Crear la tabla si no existe
tabla_usuarios = '''
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    email VARCHAR(100)
)
'''
cursor.execute(tabla_usuarios)

# Insertar datos de ejemplo si la tabla está vacía
cursor.execute("SELECT COUNT(*) FROM usuarios")
if cursor.fetchone()[0] == 0:
    cursor.execute("INSERT INTO usuarios (nombre, email) VALUES ('Juan', 'juan@email.com')")
    cursor.execute("INSERT INTO usuarios (nombre, email) VALUES ('Ana', 'ana@email.com')")
    conexion.commit()

# Consultar y mostrar los datos
cursor.execute("SELECT * FROM usuarios")
for fila in cursor.fetchall():
    print(fila)

cursor.close()
conexion.close()