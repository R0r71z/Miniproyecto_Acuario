# PEZ
# set_nombre
# set_manano
# set_temperatura
# set_pais
# set_cantidad
# get_nombre
# get_agua
# get_tamano
# get_temperatura
# get_pais
# get_tipo
# get_cantidad
# ACUARIO
# registrar
# modificar_nombre
# modificar_tamano
# modificar_pais
# modificar_cantidad
# get_peces(diccionario)


class Pez():
    def __init__(self, nombre, agua, tamano, temperatura, pais, cantidad):
        self.__tipo = 'PEZ'
        self.__nombre = nombre.upper()
        self.__agua = agua.upper()
        self.__tamano = tamano
        self.__temperatura = temperatura
        self.__pais = pais.upper()

        self.__cantidad = cantidad

    def set_nombre(self, nuevoNombre):
        self.__nombre = nuevoNombre

    def set_tamano(self, nuevoTamano):
        self.__tamano = nuevoTamano

    def set_temperatura(self, nuevaTemperatura):
        self.__temperatura = nuevaTemperatura

    def set_pais(self, nuevoPais):
        self.__pais = nuevoPais

    def set_cantidad(self, nuevaCantidad):
        self.__cantidad = nuevaCantidad

    def set_tipo(self, nuevoTipo):
        self.__tipo = nuevoTipo

    def get_nombre(self):
        return self.__nombre

    def get_agua(self):
        return self.__agua

    def get_tamano(self):
        return self.__tamano

    def get_temperatura(self):
        return self.__temperatura

    def get_pais(self):
        return self.__pais

    def get_tipo(self):
        return self.__tipo

    def get_cantidad(self):
        return self.__cantidad


class Tiburon(Pez):
    def __init__(self, nombre, agua, tamano, temperatura, pais, cantidad):
        Pez.__init__(self, nombre, agua, tamano, temperatura, pais, cantidad)
        self.set_tipo("TIBURON")


class Tortuga(Pez):
    def __init__(self, nombre, agua, tamano, temperatura, pais, cantidad):
        Pez.__init__(self, nombre, agua, tamano, temperatura, pais, cantidad)
        self.set_tipo("TORTUGA")


class Acuario():
    def __init__(self):
        self.__peces = {'DULCE': {'GRANDE': {}, 'PEQUENO': {}, }, 'SALADA': {'GRANDE': {}, 'PEQUENO': {}}}


##################################################

    def registrar(self, pez):
        retornar = 'Registo Completado'
        if self.evaluardor_de_informarion(pez) == True:
            if int(pez.get_tamano() < 20) or int(pez.get_tamano()) > 80:
                if int(pez.get_tamano()) > 80 and int(pez.get_cantidad()) > 3:
                    modificar = raw_input('La cantidad de peces excede la capacidad del tanque, '
                                          '\ndesea modificar la cantidad? (SI o NO) ')
                    if modificar.upper() == 'SI':
                        self.modificar_cantidad(pez)
                        self.__peces[pez.get_agua()]['GRANDE'][pez.get_nombre()] = pez
                    else:
                        retornar = 'Registro Cancelado'
                else:
                    self.__peces[pez.get_agua()]['GRANDE'][pez.get_nombre()] = pez
            else:
                if int(pez.get_cantidad()) > 8:
                    modificar = raw_input('La cantidad de peces excede la capacidad del tanque, '
                                          '\ndesea modificar la cantidad? (SI o NO) ')
                    if modificar.upper() == 'SI':
                        self.modificar_cantidad(pez)
                        self.__peces[pez.get_agua()]['PEQUENO'][pez.get_nombre()] = pez
                    else:
                        retornar = 'Registro Cancelado'
                else:
                    self.__peces[pez.get_agua()]['PEQUENO'][pez.get_nombre()] = pez
        else:
            retornar = self.evaluardor_de_informarion(pez)
        return retornar
##############################################
    def modificar_nombre(self, pez):
        nuevo = raw_input('nuevo nombre ')
        if self.evaluador_string(nuevo) != False:
            if int(pez.get_tamano() < 20) or int(pez.get_tamano()) > 80:
                self.__peces[pez.get_agua()]['GRANDE'].pop(pez.get_nombre())
            else:
                self.__peces[pez.get_agua()]['PEQUENO'].pop(pez.get_nombre())
            pez.set_nombre(nuevo.upper())
            self.registrar(pez)

    def modificar_tamano(self, pez):
        nuevo = raw_input('nuevo tamano ')
        if self.evaluador_integer(nuevo) != False:
            if int(pez.get_tamano() < 20) or int(pez.get_tamano()) > 80:
                if int(nuevo) < 20 or int(nuevo) > 80:
                    pez.set_tamano(nuevo)
                else:
                    self.__peces[pez.get_agua()]['GRANDE'].pop(pez.get_nombre())
                    pez.set_tamano(nuevo)
                    self.__peces[pez.get_agua()]['PEQUENO'][pez.get_nombre()] = pez
            else:
                if int(nuevo) > 80:
                    self.__peces[pez.get_agua()]['PEQUENO'].pop(pez.get_nombre())
                    pez.set_tamano(nuevo)
                    self.__peces[pez.get_agua()]['GRANDE'][pez.get_nombre()] = pez
                else:
                    pez.set_tamano(nuevo)







#################################
    def modificar_pais(self, pez):
        nuevo = raw_input('Nuevo pais ')
        if self.evaluador_string(nuevo) != False:
            pez.set_pais(nuevo)
            retornar = 'Pais Modificado'
        else:
            retornar = 'Nombre contiene caracteres no '
        return retornar


    def modificar_cantidad(self, pez):
        print 'NOTA: Recuerde que el limite de animales por especie es: \nAnimales mayor a 20CM = 8 \nAnimales mayor a 80CM = 3'
        print 'Cantidad actual ' + pez.get_cantidad()

        nuevo = raw_input('Nueva cantidad ')
        if self.evaluador_integer(nuevo) != False:
            if nuevo < pez.get_cantidad():
                pez.set_cantidad(nuevo)
                retornar = 'Cantidad Modificada'
            else:
                print 'La cantidad de peces todavia excede la '
        else:
            print 'Cantidad contiene caracteres '
            retornar = self.modificar_cantidad(pez)
        return retornar

####################





    def mostrar_por_nombre(self):
        nombre = self.buscar_nombre()
        retornar = 'Nombre Incorrecto'
        if nombre != False:
            lista = {'A': nombre.get_nombre(), 'B': nombre.get_agua(), 'C': nombre.get_tamano(),
                     'D': nombre.get_temperatura(), 'E': nombre.get_pais(), 'F': nombre.get_tipo(),
                     'G': nombre.get_cantidad(), 'H': ['Nombre: ' + nombre.get_nombre(),
                                                       'Tipo de animal: ' + nombre.get_tipo(),
                                                       'De agua: ' + nombre.get_agua(),
                                                       'Tamano aproximado de: ' + nombre.get_tamano(),
                                                       'Temperatura recomendable: '
                                                       + nombre.get_temperatura(), 'Pais nativo: ' + nombre.get_pais(),
                                                       'Cantidad en tanque: ' + nombre.get_cantidad()]}
            print 'a)Nombre\nb)Agua\nc)Tamano\nd)Temperatura\ne)Pais\nf)Tipo\ng)Cantidad\nh)TODO'
            ver = raw_input('que desea ver? (a,b,c,d,e,f,g,h) ')
            retornar = lista[ver.upper()]
        return retornar

    def mostrar_por_pais(self):
        pais = raw_input('Nombre del pais ')
        animales = []
        lista = []
        if self.evaluador_string(pais) != False:
            for agua in self.get_peces():
                for tanque in self.get_peces()[agua]:
                    for animal in self.get_peces()[agua][tanque]:
                        if pais.upper() == self.get_peces()[agua][tanque][animal].get_pais():
                            lista.append(self.get_peces()[agua][tanque][animal])
            if len(lista) > 0:
                for nombre in lista:
                    animales.append(['Nombre: ' + nombre.get_nombre(),'Tipo de animal: ' + nombre.get_tipo(),
                     'De agua: ' + nombre.get_agua(),'Tamano aproximado de: ' + nombre.get_tamano(),
                      'Temperatura recomendable: ' + nombre.get_temperatura(), 'Pais nativo: ' + nombre.get_pais(),
                      'Cantidad en tanque: ' + nombre.get_cantidad()])
            else:
                animales = 'Pais no encontrado'
        else:
            animales = 'Pais no encontrado'
        return animales




    def buscar_nombre(self):
        nombre = raw_input('Nombre del Animal a buscar ')
        animal = False
        if self.evaluador_string(nombre) != False:
            for agua in self.get_peces():
                for tanque in self.get_peces()[agua]:
                    if nombre.upper() in self.get_peces()[agua][tanque]:
                        animal = self.get_peces()[agua][tanque][nombre.upper()]
        return animal

    def eliminar(self):
        nombre = raw_input('Escriba el nombre del animal que desea eliminar del registro ')
        for agua in self.get_peces():
            for tanque in self.get_peces()[agua]:
                if nombre.upper() in self.get_peces()[agua][tanque]:
                    self.get_peces()[agua][tanque].pop(nombre.upper())
                    return 'Eliminacion Completada'
        return 'No encontrado'


    def evaluador_integer(self,integer):
        numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for element in integer:
            if element not in numeros:
                return False


    def evaluador_string(self, string):
        letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', ' ']
        for element in string.upper():
            if element not in letras:
                return False

    ###################################

    def evaluardor_de_informarion(self, pez):
        retornar = True
        evaluar = [pez.get_nombre(), pez.get_agua(), pez.get_tamano(),
                   pez.get_temperatura(), pez.get_pais(),pez.get_cantidad()]
        for elemento in evaluar:
            if self.evaluador_string(elemento) == False and self.evaluador_integer(elemento) == False:
                retornar = 'La infomarcion es incorrecta, por favor verificar ' + elemento
        return retornar

    ####################

    def get_peces(self):
        return self.__peces


peje1 = Pez('mario', 'dulce', '40', '35', 'Rep Dom', '9')
peje2 = Pez('raul', 'dulce', '40', '35', 'Rep. Dom.', '1')
tiburon = Tiburon('alma', 'salada', '85', '30', 'Rep. Dom.', '1')

acu = Acuario()
print acu.registrar(peje1)
print acu.registrar(peje2)
print acu.registrar(tiburon)
print acu.get_peces()
print '------------------------------------'
#print acu.modificar_nombre(peje1)
print acu.mostrar_por_pais()
print '------------------------------------'
print acu.get_peces()
# print peje1.get_tamano()
# acu.modificar_tamano(peje1)
# print '------------------------------------'

