#agenda
contacto = []

def agregar_contacto(nombre, telefono):
    contacto.append({"nombre": nombre, "telefono:": telefono})

nombre = input("Ingresa el nombre : ")
telefono = input("Ingresar el teléfono : ")
agregar_contacto(nombre, telefono)
print("Contacto agregado")