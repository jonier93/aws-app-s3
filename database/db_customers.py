import pymysql

db_user = 'jonier'
db_password = '12345'
db_name = 'db_users_flask'
ip_address = '35.224.188.109'

def connection_sql():
    try:
        connection = pymysql.connect(host=ip_address,
                                    user=db_user, 
                                    password=db_password,                                       
                                    db=db_name)
        print("Successful connection")
        return connection
    except pymysql.MySQLError as err:
        print(err)
        return None

def insert_record(nombre, id, age):
    connection = connection_sql()
    cursor = connection.cursor()
    try:
        instruccion = "INSERT INTO customers VALUES ('" +  nombre + "', " + str(id) + ", " + str(age) + ");"
        cursor.execute(instruccion) # se envía la instrucción a SQLite
        connection.commit() # Se utiliza para confirmar que queremos guardar los datos
        print("User registered")
        return True
    except pymysql.MySQLError as err:
        print("error: " + str(err))
        return False

def consult_record(id):
    try:
        connection = connection_sql()
        cursor = connection.cursor()
        instruction = "SELECT * FROM customers WHERE id=" + id + ";"         
        cursor.execute(instruction)
        results = cursor.fetchall()
        return results
    except pymysql as err:
        print("error: " + str(err))