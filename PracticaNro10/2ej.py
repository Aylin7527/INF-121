from multimethod import multimethod

class LineaTeleferico:
    
    def __init__(self, color="", tramo="", nroCabinas=0, nroEmpleados=4): 
        self.__color = color
        self.__tramo = tramo
        self.__nroCabinas = nroCabinas
        self.__nroEmpleados = nroEmpleados
        self.__empleados = [["Pedro","Rojas","Luna"],
                            ["Lucy", "Sosa", "Rios"],
                            ["Ana", "Perez", "Rojas"],
                            ["Saul", "Arce","Calle"]]
        self.__edades = [35,43,26,29]
        self.__sueldos = [2500.0,3250.0,2700.0,2500.0]
    
    def __str__(self):
        cad = f"Color: {self.__color}, Tramo: {self.__tramo}, nroCabinas: {self.__nroCabinas}, nroEmpleados: {self.__nroEmpleados}\n"
        cad = cad+ "-------Empleados------- \n"
        for i in range(len(self.__empleados)):
            cad = cad+f"Nombre: {(self.__empleados[i])[0]} {(self.__empleados[i])[1]} {(self.__empleados[i])[2]}, Edad: {self.__edades[i]} Sueldo: {self.__sueldos[i]}\n"
        return cad
    
    def eliminarPorApellido(self, x):
        i = 0
        while i < len(self.__empleados):
            if self.__empleados[i][1] == x or self.__empleados[i][2] == x:
                self.__empleados.pop(i)
                self.__edades.pop(i)
                self.__sueldos.pop(i)
                self.__nroEmpleados -= 1
            # No incrementamos i porque la lista se redujo
            else:
                i += 1

    
    def __add__(self,parametros):
        otro, x = parametros
        if (isinstance(otro, LineaTeleferico)):
            for i in range(len(self.__empleados)):
                if((self.__empleados[i])[0] == x):
                    nombre = (self.__empleados[i])[0]
                    paterno = (self.__empleados[i])[1]
                    materno = (self.__empleados[i])[2]
                    otro.__empleados.append([nombre, paterno, materno])
                    otro.__edades.append(self.__edades[i])
                    otro.__sueldos.append(self.__sueldos[i])
                    self.__empleados.pop(i)
                    self.__edades.pop(i)
                    self.__sueldos.pop(i)
                    self.__nroEmpleados -=1
                    otro.__nroEmpleados +=1
                    break
        return otro

    def mayorEdad(self): 
        mayor = 0
        for i in range(len(self.__empleados)):
            if(self.__edades[i]>mayor):
                mayor = self.__edades[i]
        return mayor
    
    def mayorSueldo(self): 
        mayor = 0.0
        for i in range(len(self.__empleados)):
            if(self.__sueldos[i]>mayor):
                mayor = self.__sueldos[i]
        return mayor
    
    @multimethod
    def mostrar(self,e:int):
        cad = "Empelados con mayor edad: \n"
        for i in range(len(self.__empleados)):
            if(self.__edades[i] == e):
                cad = cad+f"Nombre: {(self.__empleados[i])[0]} {(self.__empleados[i])[1]} {(self.__empleados[i])[2]}, Edad: {self.__edades[i]} Sueldo: {self.__sueldos[i]}\n"
        print(cad)
    
    @multimethod
    def mostrar(self, s:float):
        cad = "Empleados con mayor sueldo: \n"
        for i in range(len(self.__empleados)):
            if(self.__sueldos[i] == s):
                cad = cad+f"Nombre: {(self.__empleados[i])[0]} {(self.__empleados[i])[1]} {(self.__empleados[i])[2]}, Edad: {self.__edades[i]} Sueldo: {self.__sueldos[i]}\n"
        print(cad)
        
    
t01 = LineaTeleferico("Rojo", "Estacion Central - Estacion Cementerio - Estacion 16 de Julio", 20, 4)
t02 = LineaTeleferico("Morado", "Estacion San José - Estacion Faro Murillo - Estacion 6 de Marzo", 40, 4)
print("-------Primer Teleferico-------")
print(t01)
print("-------Segundo Teleferico-------")
print(t02)
    
print("-------Eliminar por apellido(Rojas)-------")
t01.eliminarPorApellido("Rojas")
t02.eliminarPorApellido("Rojas")
print(t01)
print(t02)
    
print("-------Sobrecargar operador--------")
print(t01+(t02,"Saul")) 
    
print("---------Sobrecargar para mayor edad---------")
mayEdad=t01.mayorEdad()
t01.mostrar(mayEdad)

print("---------Sobrecargar para mayor sueldo---------")
maySueldo = t01.mayorSueldo()
t01.mostrar(maySueldo)