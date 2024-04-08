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

# crear sentencia sql
sql='INSERT INTO personas (pers_nombre,pers_apellido,edad) VALUES(%s,%s,%s)'

# solicitud de datos al usuario
nombre=input('ingrese el nombre: ')
apellido=input('ingrese el apellido: ')
edad=input('ingrese la edad: ')

# recoleccion de datos
datos=(nombre,apellido,edad)

# hacer uso del metodo execute
cursor.execute(sql,datos)

# guardar registro
conexion.commit()

# registro insertados
registros=cursor.rowcount

# mostrar mensaje
print(f'registro insertado: {registros}')

# cerrar conexiones
cursor.close()
conexion.close()