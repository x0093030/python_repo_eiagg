import mysql.connector
import pdb

def connect_to_database():
    """Función para conectar a la base de datos MySQL."""
    global conexion, cursor 
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",  # Cambia por tu usuario en MySQL Workbench
            password="1qazzaq1",  # Cambia por tu contraseña en MySQL Workbench
            port=3306,  # Cambia por el puerto que uses en MySQL Workbench
            database="prueba"   # Asegúrate de que esta base de datos exista 
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            cursor = conexion.cursor() # Create a cursor to execute SQL commands
            return cursor
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")

def create_table(cursor):
    """Función para crear una tabla en la base de datos MySQL."""
    command = '''
    CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    email VARCHAR(100),
    edad INT DEFAULT 1
    )
    '''
    cursor.execute(command)

def insert_data(cursor):
    """Función para insertar datos en la tabla usuarios."""
    cursor.execute("SELECT COUNT(*) FROM usuarios")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO usuarios (nombre, email) VALUES ('Juan', 'juan@email.com')")
        cursor.execute("INSERT INTO usuarios (nombre, email) VALUES ('Ana', 'ana@email.com')")
        conexion.commit()
    else:
        print("La tabla 'usuarios' ya contiene datos, no se insertarán nuevos registros.")

def consult_data(cursor):
    """Función para consultar y mostrar datos de la tabla usuarios."""
    cursor.execute("SELECT * FROM usuarios")
    for fila in cursor.fetchall():
        print(fila)

def update_data(cursor):
    """Función para actualizar datos en la tabla usuarios."""
    command = "UPDATE usuarios SET edad = 34 WHERE nombre = 'Juan'"
    cursor.execute(command)
    # conexion.commit()

def update_after_validate_data(cursor):
    cursor.execute("SELECT * FROM usuarios")
    for file in cursor.fetchall():
        print(f"Validando datos: {file}")
        if file[1] == 'Juan':
            print("El nombre es Juan, actualizando edad a 53")
            command = "UPDATE usuarios SET edad = 53 WHERE nombre = 'Juan'"
            cursor.execute(command)
            conexion.commit()
        elif file[1] == 'Ana':
            print("El nombre es Ana, actualizando edad a 45")
            command = "UPDATE usuarios SET edad = 45 WHERE nombre = 'Ana'"
            cursor.execute(command)
            conexion.commit()
        else:
            print("No se requiere actualización para este usuario.")

def close_session(cursor):
    """Función para cerrar la conexión a la base de datos."""
    cursor.close()
    conexion.close()

if __name__ == '__main__':

    cursor = connect_to_database()
    create_table(cursor)
    insert_data(cursor)
    consult_data(cursor)
    update_data(cursor)
    consult_data(cursor)
    update_after_validate_data(cursor)
    consult_data(cursor)
    close_session(cursor)
