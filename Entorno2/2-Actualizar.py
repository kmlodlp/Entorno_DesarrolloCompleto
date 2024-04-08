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
sql='UPDATE personas SET pers_nombre=%s, pers_apellido=%s, edad=%s WHERE id_persona=%s'

# consulta de datos a usuario
id_persona=input('ingrese el nuevo id de la persona a editar: ')
nombre=input('ingrese el nuevo nombre del usuario: ')
apellido=input('ingrese el nuevo apellido apellido: ')
edad=input('ingrese la edad actualizada: ')

#recoleccion de datos
datos=(nombre,apellido,edad,id_persona)

# utilizar el metodo execute
cursor.execute(sql,datos)

# guardar modificacion
conexion.commit()

#contar el numero de cambios
actualizacion=cursor.rowcount

# mostrar mensaje al usuraio
print(f'registro actualizado: {actualizacion}')

# cerrar conexiones
cursor.close()
conexion.close()

