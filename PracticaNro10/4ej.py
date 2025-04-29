from multimethod import multimethod
class Ministerio:

    def __init__(self, nombre="", direccion="", nroEmpleados=4):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__nroEmpleados = nroEmpleados
        self.__empleados = [["Pedro","Rojas","Luna"],
                            ["Lucy", "Sosa", "Rios"],
                            ["Ana", "Perez", "Rojas"],
                            ["Saul", "Arce","Calle"]]
        self.__edades = [35,43,26,29]
        self.__sueldos = [2500.0,3250.0,2700.0,2500.0]

    def __str__(self):
        cad = f"Nombre: {self.__nombre}, Dirección: {self.__direccion}, nroEmpleados: {self.__nroEmpleados}\n"
        cad += "-------Empleados------- \n"
        for i in range(len(self.__empleados)):
            cad += f"Nombre: {self.__empleados[i][0]} {self.__empleados[i][1]} {self.__empleados[i][2]}, Edad: {self.__edades[i]} Sueldo: {self.__sueldos[i]}\n"
        return cad

    def eliminarPorEdad(self, x):
        i = 0
        while i < len(self.__empleados):
            if self.__edades[i] == x:
                self.__empleados.pop(i)
                self.__edades.pop(i)
                self.__sueldos.pop(i)
                self.__nroEmpleados -= 1
            else:
                i += 1

    def __add__(self, parametros):
        otro, nombre = parametros
        if isinstance(otro, Ministerio):
            for i in range(len(self.__empleados)):
                if self.__empleados[i][0] == nombre:
                    nom, pat, mat = self.__empleados[i]
                    otro.__empleados.append([nom, pat, mat])
                    otro.__edades.append(self.__edades[i])
                    otro.__sueldos.append(self.__sueldos[i])
                    self.__empleados.pop(i)
                    self.__edades.pop(i)
                    self.__sueldos.pop(i)
                    self.__nroEmpleados -= 1
                    otro.__nroEmpleados += 1
                    break
        return otro

    def menorEdad(self):
        menor = self.__edades[0]
        for edad in self.__edades:
            if edad < menor:
                menor = edad
        return menor

    def menorSueldo(self):
        menor = self.__sueldos[0]
        for sueldo in self.__sueldos:
            if sueldo < menor:
                menor = sueldo
        return menor

    @multimethod
    def mostrar(self, e: int):
        cad = "Empleados con menor edad:\n"
        for i in range(len(self.__empleados)):
            if self.__edades[i] == e:
                cad += f"Nombre: {self.__empleados[i][0]} {self.__empleados[i][1]} {self.__empleados[i][2]}, Edad: {self.__edades[i]} Sueldo: {self.__sueldos[i]}\n"
        print(cad)

    @multimethod
    def mostrar(self, s: float):
        cad = "Empleados con menor sueldo:\n"
        for i in range(len(self.__empleados)):
            if self.__sueldos[i] == s:
                cad += f"Nombre: {self.__empleados[i][0]} {self.__empleados[i][1]} {self.__empleados[i][2]}, Edad: {self.__edades[i]} Sueldo: {self.__sueldos[i]}\n"
        print(cad)

m1 = Ministerio("Ministerio de Educación", "Av. Arce #123", 4)
m2 = Ministerio("Ministerio de Salud", "Av. Camacho #456", 4)

print("-------Primer Ministerio-------")
print(m1)

print("-------Segundo Ministerio-------")
print(m2)

print("-------Eliminar por edad (26)-------")
m1.eliminarPorEdad(26)
m2.eliminarPorEdad(26)
print(m1)
print(m2)

print("-------Sobrecargar operador--------")
print(m1 + (m2, "Saul"))

print("---------Sobrecargar para menor edad---------")
menorEdad = m1.menorEdad()
m1.mostrar(menorEdad)

print("---------Sobrecargar para menor sueldo---------")
menorSueldo = m1.menorSueldo()
m1.mostrar(menorSueldo)
