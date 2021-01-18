#!/usr/bin/python3
#

from modulo import *

# Cadenas usadas
in_numero = "Debe introducir un número: " # Usada cuando el usuario debía introducir un número y no lo hace

in_titulo = "Introduzca el título del libro "
in_autor = "Introduzca el nombre del autor "
in_paginas = "Introduzca la cantidad de páginas "
in_ISBN = "Introduzca el código ISBN "
in_anioEdicion = "Introduzca el año de edición "
in_editorial = "Introduzca el nombre de la editorial "
in_genero = "Introduzca el género "
in_nuevo = "Introduzca el nuevo campo "

in_indice = "\nIntroduzca el índice que numera " # Usada cuando se le pide al usuario el número que corresponde a algo a lo que se le quiera hacer alguna acción (ver las cadenas siguientes)
# Objetos
in_libro = "el libro "
in_campo = "el campo "
in_accion = "la acción "
# Común
in_desee = "que desee "
# Acciones
in_borrar = "borrar: "
in_editar = "editar: "
in_realizar = "realizar: "
in_modificar = "modificar: "

# Texto inicial de la función interactiva
acciones = ("\n\n\nPuede realizar una de las siguientes acciones sobre la biblioteca:\n\n" +
            "0. Ver la lista de libros.\n" +
            "1. Agregar un nuevo libro.\n" +
            "2. Borrar un libro.\n" +
            "3. Editar un libro.\n" +
            "4. Guardar y salir.\n" +
            "5. Consulta\n" +
            "6. Listados")


guardado_correcto = "Su biblioteca ha sido guardada correctamente. Pulse cualquier tecla para salir."



def comprueba_numero(i):
    """Comprueba si lo introducido por el usuario es un número y, si no, pide otro."""
    while haz_numero(i) == "No se puede convertir a numero": # Si no se puede convertir, pide otro hasta que se pueda
        i = input(in_numero)
    return haz_numero(i)



biblioteca = Biblioteca() # Creamos la biblioteca



def muestra_repertorio():
    """Muestra los libros que hay en la biblioteca."""
    for i, libro in enumerate(biblioteca.libros):
        print(str(i) + ". " + ", ".join(libro) + ".")



def agrega_libro():
    """Interactúa con el usuario para permitirle agregar un libro a la biblioteca."""
    # Pide al usuario los datos necesarios
    titulo = input(in_titulo)
    autor = input(in_autor)
    paginas = input(in_paginas)
    ISBN = input(in_ISBN)
    anioEdicion = input(in_anioEdicion)
    editorial = input(in_editorial)
    genero = input(in_genero)

    pos= []
    
    if biblioteca.consulta(titulo, pos) == False:     #debería consultar por ISBN
        biblioteca.agrega_libro(titulo, autor, paginas, ISBN, anioEdicion, editorial, genero)        
        print("\nLibro agregado")
    else:
        print("\nLibro ya existente")


def borra_libro():      #borra por clave ISBN
    """Interactúa con el usuario para permitirle borrar un libro de la biblioteca."""
    muestra_repertorio()
    pos = []
    #i = input(in_indice + in_libro + in_desee + in_borrar) # Pregunta qué libro borrar
    #i = comprueba_numero(i)
    ISBN = input(in_ISBN + in_desee + in_borrar)
    
    if biblioteca.consulta(ISBN, pos) == True:
        biblioteca.borra_libro(pos[0])
    else:
        print("\nLibro no existe")



def edita_libro():      #modifica por clave ISBN
    """Interactúa con el usuario para permitirle editar un libro de la biblioteca."""
    muestra_repertorio()
    pos = []
    
    #i = input(in_indice + in_libro + in_desee + in_editar) # El usuario elige qué libro quiere editar
    #i = comprueba_numero(i)
    print("\n")
    ISBN = input(in_ISBN + in_desee + in_modificar)

    if biblioteca.consulta(ISBN, pos) == True:
        i = pos[0]
    else:
        print("Libro no existe")
        
    # Muestra los campos del libro
    print("")
    for ii, campo in enumerate(biblioteca.campos): 
        print(str(ii) + ". " + campo + ": " + biblioteca.libros[i][ii] + ".")
    
    iii = input(in_indice + in_campo + in_desee + in_modificar) # El usuario elige qué campo quiere editar del libro elegido
    iii = comprueba_numero(iii)
    
    biblioteca.edita_libro(i, iii, input(in_nuevo)) # Llama al método que edita el campo

def consulta():
    pos = []
    ISBN = input(in_ISBN)
    if biblioteca.consulta(ISBN, pos) == True:
        indice = pos[0]
        titulo = biblioteca.libros[indice][0]
        print(titulo, "está presente en la BD", "pos:", pos[0])
    else:
        print(ISBN, "no se encuentra en la BD")

def listados():
    print("0. Listar todos los autores existentes.\n" +
          "1. Listar todos los libros existentes.\n" +
          "2. Listar todos los libros de un género determinado.\n" +
          "3. Listar todos los libros que posee un autor determinado.\n" +
          "4. Listar todos los libros de una editorial determinada.\n" +
          "5. Listar todos los libros de una editorial determinada en un rango de años de edición.\n" +
          "6. Listar todos los autores de una determinada editorial.\n" +
          "7. Listar todos los libros que fueron editados en un determinado año.\n" +
          "8. Listar todos los libros de los autores cuyos apellidos comienzan con una letra determinada.\n" +
          "9. Listar todos los libros cuyos títulos contengan una palabra determinada.\n"
          )
    j = input(in_indice + in_accion + in_realizar)
    j = comprueba_numero(j)
    
    if j == 0:      #1. Listar todos los autores existentes.
        biblioteca.listado_autores()
        
    elif j == 1:    #2. Listar todos los libros existentes.
        biblioteca.listado_libros()
        
    elif j == 2:    #3. Listar todos los libros de un género determinado.
        biblioteca.listado_libros_genero()

    elif j == 3:    #4. Listar todos los libros que posee un autor determinado.
        biblioteca.listado_libros_autor()

    elif j == 4:    #5. Listar todos los libros de una editorial determinada.
        biblioteca.listado_libros_editorial()

    elif j == 5:    #6. Listar todos los libros de una editorial determinada en un rango de años de edición.
        biblioteca.listado_libros_editorial_rango()

    elif j == 6:    #7. Listar todos los autores de una determinada editorial.
        biblioteca.listado_autores_editorial()

    elif j == 7:    #8. Listar todos los libros que fueron editados en un determinado año.
        biblioteca.listado_anio()

    elif j == 8:    #9. Listar todos los libros de los autores cuyos apellidos comienzan con una letra determinada.
        biblioteca.listado_apellidosLetra()

    elif j == 9:   #10. Listar todos los libros cuyos títulos contengan una palabra determinada.
        biblioteca.listado_palabra()


def interactua():
    """Interactúa con el usuario para realizar todas las acciones."""
    print(acciones) # Muestra las acciones
    i = input(in_indice + in_accion + in_desee + in_realizar) # Pregunta cuál es la que se quiere realizar
    print("\n\n\n")
    i = comprueba_numero(i)
    
    # Ejecuta la acción elegida
    if i == 0:
        muestra_repertorio()
        input("")
    elif i == 1:
        agrega_libro()
    elif i == 2:
        borra_libro()
    elif i == 3:
        edita_libro()
    elif i == 4:
        biblioteca.guarda()
        input(guardado_correcto)
        return True
    elif i == 5:
        consulta()
    elif i == 6:
        listados()


ejecuta = None
while not ejecuta: # Ejecuta el programa interactivo en bucle hasta que se escoja guardar y salir
    ejecuta = interactua()
