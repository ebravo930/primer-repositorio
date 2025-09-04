#agenda
contactos = []

def agregar_contacto(nombre, telefono):
    contactos.append({"nombre": nombre, "telefono:": telefono})

def listar_contactos():
    print("\nLista de contactos : ")
    for c in contactos :
        print(f"{c['nombre']} - {c['telefono']}")

def buscar_contacto(nombre):
    for c in contactos:
        if c['nombre'].lower() == nombre.lower():
            print(f"Contacto encontrado : {c['nombre']} - {c['telefono']}")
            return
        print('Contacto NO encontrado')

listar_contactos()

#nombre = input("Ingresa el nombre : ")
#telefono = input("Ingresar el teléfono : ")
#agregar_contacto(nombre, telefono)
#print("Contacto agregado")

#uso funcion buscar
nombre_buscar = input("Nombre a buscar : ")
buscar_contacto(nombre_buscar)

