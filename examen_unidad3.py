import json
from crudmysql import MySQL

variables = {}
variables["host"] = "localhost"
variables["user"] = "root"
variables["pws"] = ""
variables["db"] = "itj_estudiantes"

def examenU3(ctrl):
    obj_MySQL = MySQL(variables)
    print(" == Examen unidad 3 ==")
    #ctrl = input("Numero de control: ")
    sql_materias ="SELECT E.nombre, K.materia, K.calificacion " \
                  "FROM estudiantes E, kardex K " \
                  f"WHERE E.control = K.control and E.control='{ctrl}';"
    resp = obj_MySQL.consulta_sql(sql_materias)
    if resp:
        lista_materias = []
        #print("Estudiante: ", resp[0][0])
        lista_materias.append({"Estudiante: ": f"{resp[0][0]}"})
        for mat in resp:
                lista_materias.append({"Materia: ": f"{mat[1]}", " Calificación: ": f"{mat[2]}"})
        return json.dumps(lista_materias)
            #print("Materia: ",mat[1], " Calificación: ", mat[2])
    else:
        print(f"El estudiante con Número de control: {ctrl} NO existe")

print(examenU3(ctrl = input("Numero de control: ")))


#examenU3()

