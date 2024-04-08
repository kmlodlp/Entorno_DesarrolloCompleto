# importacion del modulo
import psycopg2

#conexion a base de datos
conexion=psycopg2.connect(user='postgres',
                          password='Camilo#D11',  
                          host='localhost',
                          port='5432',
                          database='python')

# utilizar cursor
cursor=conexion.cursor()

# crear la sentencia sql
sql='SELECT * FROM personas'

# uso del metodo execute
cursor.execute(sql)

# mostrar resultado
registro=cursor.fetchall()

# mostrar en consola o el usuario
for fila in registro:
 print(fila)

# cerrar conexiones
cursor.close()
conexion.close()
