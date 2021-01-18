#!/usr/bin/python3
#

import csv

def haz_numero(i): # TODO: Controlar también que no se salga del rango positivo de la lista correspondiente y permitir cancelar funciones de alguna manera (por ejemplo introduciendo -1)
    """Comprueba si lo recibido es un número, transfórmalo si lo es y devuelve una cadena si no."""
    # Intenta convertir la cadena a número, y si se puede, devuelve el número
    try:
        i = int(i)
        return i
    #Si no se puede, nos dice que no se puede
    except ValueError:
        return "No se puede convertir a numero"





class Biblioteca: # Esta es la clase bibliotecas, cuyos métodos permiten gestionarla
    
    campos = ["Título", "Autor", "Páginas", "ISBN", "Año Ed", "Editorial", "Género"] # Campos que tendrá cada libro
    libros = []
    
    
    
    def __init__(self):
        with open('biblioteca.csv', newline='') as f:
            reader = csv.reader(f)
            self.libros = list(reader)
    
    
    
    def agrega_libro(self, *campos):
        """Añade el libro a la biblioteca."""
        self.libros.append(list(campos))
    
    
    
    def borra_libro(self, libro):
        """Borra un libro de la biblioteca"""
        self.libros.pop(libro)
    
    
    
    def edita_libro(self, libro, campo, valor):
        """Edita un campo de uno de los libros de la biblioteca"""
        self.libros[libro][campo] = valor
    
    def guarda(self):
        """Guarda la biblioteca actual en el csv."""
        with open('biblioteca.csv', 'w', newline='') as f: # Abre el archivo csv como el objeto f
            writer = csv.writer(f) # Llama al método que escribe en ese archivo
            writer.writerows(self.libros) # Escribe los libros en el CSV por filas

    def consulta(self, ISBN, pos):     #usa pos como lista porque la lista es mutable
        """Consulta si un determinado libro está en la BD"""
        Esta = False
        for i in range(0, len(self.libros)):
            if ISBN == self.libros[i][3]:
                Esta = True
                pos.append(i)
        return Esta

    def listado_autores(self): #1. Listar todos los autores existentes.
        autores = []
        for i in range(0, len(self.libros)):
            if self.libros[i][1] not in autores:
                autores.append(self.libros[i][1])
                
        print("autores:\n")
        for i in range(0, len(autores)):
            print(autores[i])

    def listado_libros(self):
        librosl = []
        for i in range(0, len(self.libros)):
            if self.libros[i][0] not in librosl:
                librosl.append(self.libros[i][0])

        print("libros:\n")
        for i in range(0, len(librosl)):
            print(librosl[i])

    def listado_libros_genero(self):
        librosg = []
        genero = input("ingrese género literario: ")
        for i in range(0, len(self.libros)):
            if ((self.libros[i][6] == genero) and (self.libros[i][0] not in librosg)):
                librosg.append(self.libros[i][0])

        print("libros del género indicado:\n")
        for i in range(0, len(librosg)):
            print(librosg[i])

    def listado_libros_autor(self):
        librosAutor = []
        autor = input("ingrese un autor: ")
        for i in range(0, len(self.libros)):
            if( (self.libros[i][1] == autor ) and (self.libros[i][0] not in librosAutor) ):
                librosAutor.append(self.libros[i][0])

        print("libros del autor indicado:\n")
        for i in range(0, len(librosAutor)):
            print(librosAutor[i])

    def listado_libros_editorial(self):
        librosEditorial = []
        editorial = input("ingrese una editorial: ")
        for i in range(0, len(self.libros)):
            if( (self.libros[i][5] == editorial ) and (self.libros[i][0] not in librosEditorial) ):
                librosEditorial.append(self.libros[i][0])

        print("libros de la editorial indicada:\n")
        for i in range(0, len(librosEditorial)):
            print(librosEditorial[i])

    def listado_libros_editorial_rango(self):
        librosRango = []
        editorial = input("ingrese una editorial: ")
        Inf = input("Ingrese rango de años, año inferior: ")
        Sup = input("Ingrese año superior: ")
        for i in range(0, len(self.libros)):
            if ( (self.libros[i][5] == editorial )
                 and (self.libros[i][0] not in librosRango)
                 and (self.libros[i][4] >= Inf)
                 and (self.libros[i][4] <= Sup)):
                
                librosRango.append(self.libros[i][0])

        print("libros de la editorial y rango de años indicados:\n")
        for i in range(0, len(librosRango)):
            print(librosRango[i])

    def listado_autores_editorial(self):
        autoresEditorial = []
        editorial = input("ingrese editorial: ")
        for i in range(0, len(self.libros)):
            if ( (self.libros[i][5] == editorial)
                 and (self.libros[i][1]) not in autoresEditorial):

                autoresEditorial.append(self.libros[i][1])

        print("Listado de autores de la editorial: ")
        for i in range(0, len(autoresEditorial)):
            print(autoresEditorial[i])

    def listado_anio(self):
        librosAnio = []
        anio = input("Ingrese año de edición: ")
        for i in range(0, len(self.libros)):
            if ( (self.libros[i][4] == anio)
                 and (self.libros[i][0] not in librosAnio)):

                librosAnio.append(self.libros[i][0])

        print("Libros editados en el año ",anio)
        for i in range(0, len(librosAnio)):
            print(librosAnio[i])    #sería bueno agregarle el isbn

    def listado_apellidosLetra(self):

        import re
        letraApellido = input("Ingrese la letra para buscar autores por apellido: ")
        titulos = []

        for i in range(0, len(self.libros)):
            cadena = self.libros[i][1]
            palabras = cadena.split()
            apellido = palabras[-1]
            if letraApellido == apellido[0]:
                titulos.append(self.libros[i][0])

        for i in range(0, len(titulos)):
            print(titulos[i])
    
    def listado_palabra(self):

        import re   #biblioteca de expresiones regulares
        librosPalabra = []
        
        palabra = input("Palabra de búsqueda: ")
        for i in range(0, len(self.libros)):
            match = re.search(palabra, self.libros[i][0])
            if match != None:
                librosPalabra.append(self.libros[i][0])
        for i in range(0, len(librosPalabra)):
            print(librosPalabra[i])
