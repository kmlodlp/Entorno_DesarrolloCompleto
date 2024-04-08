# importacion del modulo
import psycopg2

# conexion a base de datos
conexion = psycopg2.connect(
    user="postgres",
    password="Camilo#D11",
    host="localhost",
    port="5432",
    database="python",
)

# utilizar cursor
cursor = conexion.cursor()

# Campos  pers_nombre=%s, pers_apellido=%s, edad=%s, id_persona=%s
# crear sentencia sql
sql = "INSERT INTO personas (id_persona,pers_nombre,pers_apellido,edad) VALUES(%s,%s,%s,%s)"

# solicitud de datos al usuario
id = input("ingrese el id de la persona: ")
nombre = input("ingrese el nombre: ")
apellido = input("ingrese el apellido: ")
edad = input("ingrese la edad: ")

# recoleccion de datos
datos = (id,nombre, apellido, edad)

# hacer uso del metodo execute
cursor.execute(sql, datos)

# guardar registro
conexion.commit()

# registro insertados
registros = cursor.rowcount

# mostrar mensaje
print(f"registro insertado: {registros}")

# cerrar conexiones
cursor.close()
conexion.close()
