#agenda
contactos = []

def agregar_contacto(nombre, telefono):
    contactos.append({"nombre": nombre, "telefono:": telefono})

def listar_contactos():
    print("\nLista de contactos : ")
    for c in contactos :
        print(f"{c['nombre']} - {c['telefono']}")

listar_contactos()

nombre = input("Ingresa el nombre : ")
telefono = input("Ingresar el teléfono : ")
agregar_contacto(nombre, telefono)
print("Contacto agregado")

