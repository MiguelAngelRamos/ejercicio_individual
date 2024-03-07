# Primero vamos a simular un registro básico de usuarios
usuarios_str = "Sofia,Eduardo,Catalina,Rocio,Martin,Laura,Valeria"

# Convertir un string a una lista, deseamos manejar individualmente a los usuarios
usuarios = usuarios_str.split(",")

# Imprimimos por consola la cantidad de usuarios registrados en la app
print(f"La cantidad de usuarios registrados son: {len(usuarios)}")
# print(usuarios) # ['Sofia', 'Eduardo', 'Catalina', 'Rocio', 'Martin', 'Laura', 'Valeria']
# Buscar el nombre de usuario dentro de lista

# Miguel
def iniciar_sesion(nombre_usuario):
    nombre_usuario = nombre_usuario.lower()
    usuarios_min = [usuario.lower() for usuario in usuarios] # Lista de usuarios en minúscula

    # Verificar si el nombre de usuario existe dentro de la lista
    if nombre_usuario in usuarios_min:
        print(f"Hola, {nombre_usuario.capitalize()}! Bienvenido(a) al Sistema")
    else:
        print("Usuario no encontrado. Por favor verifica tu nombre de usuario o registrate.")



iniciar_sesion("richard")  


