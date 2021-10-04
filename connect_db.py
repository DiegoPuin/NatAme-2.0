import cx_Oracle


class connect():

    def __init__(self):
        host = "localhost"
        user = "natame"
        passw = "1234"
        tsname = "xe"

        lib_dir = r"C:\Users\USER\Downloads\Instaladores\instantclient_19_10"

        try:
            cx_Oracle.init_oracle_client(lib_dir=lib_dir)
        except Exception as err:
            print("Error connecting: cx_Oracle.init_oracle_client()")
            print(err)

        try:
            self.conexion = cx_Oracle.connect(user, passw, host+"/"+tsname)
        except Exception as error:
            print("No se pudo conectar a la base de datos. Error: ")

    def sentenciaCompuesta(self, sentencia):
        cursor = self.conexion.cursor()
        cursor.execute(sentencia)
        datos = cursor.fetchall()
        cursor.close()
        return datos

    def close(self):
        if self.conexion:
            self.conexion.close()

    def commint(self):
        self.conexion.commit()
        
    def sentenciaSimple(self, sentencia):
        cursor = self.conexion.cursor()
        cursor.execute(sentencia)
        cursor.close()

    def sentenciaPreparada(self, sentencia, datos):
        cursor = self.conexion.cursor()
        cursor.execute(sentencia,(datos,))
        salida = cursor.fetchall()
        cursor.close()
        return salida