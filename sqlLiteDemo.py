import sqlite3

def sql_connection():
    try:
        con = sqlite3.connect('mydatabase.db')
        return con
    except Error:
        print(Error)

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE usuarios(id integer PRIMARY KEY, nombre text, email text, password text)")
    con.commit()

def sql_InsertarUsuario(con):
     cursorObj = con.cursor()
     cursorObj.execute("INSERT INTO usuarios VALUES(1, 'Allan', 'allan.monge19@gmail.com', '12345678')")
     con.commit()

#llamar a las funciones que conectan y crean la base de datos. Se comenta la linea que crea la tabla, solo se debe correr esa linea una vez
sql_connection()
#sql_table(sql_connection())
sql_InsertarUsuario(sql_connection())

