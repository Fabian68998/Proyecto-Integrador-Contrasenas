import random
import string

# ==========================================
# CAPA DE PRESENTACIÓN (Interfaz de Usuario)
# ==========================================
print("--- GENERADOR SEGURO DE CONTRASEÑAS ---")
print("Bienvenido. Vamos a configurar tu credencial.\n")

longitud = 0

# Estructura repetitiva (while) para validar que el usuario ingrese una longitud segura
while longitud < 8:
    try:
        longitud_input = input("Ingresa la longitud de la contraseña (mínimo 8 caracteres): ")
        longitud = int(longitud_input)
        
        # Estructura condicional (if) para asegurar el estándar de seguridad
        if longitud < 8:
            print("Error: Por tu seguridad, la contraseña debe tener al menos 8 caracteres. Intenta de nuevo.\n")
    except ValueError:
        print("Error: Por favor, ingresa un número entero válido.\n")
        longitud = 0 # Reiniciamos para que el bucle continúe

# Solicitamos los parámetros adicionales
print("\nConfiguración de filtros (Escribe 's' para Sí, o 'n' para No):")
usar_mayus = input("¿Incluir letras mayúsculas?: ").lower() == 's'
usar_nums = input("¿Incluir números?: ").lower() == 's'
usar_simb = input("¿Incluir símbolos especiales?: ").lower() == 's'

# ==========================================
# CAPA DE LÓGICA DE NEGOCIO (Motor Lógico)
# ==========================================
# Por defecto, siempre incluiremos letras minúsculas
caracteres_validos = string.ascii_lowercase

# Estructuras lógicas (if) para construir el pool de caracteres según la elección del usuario
if usar_mayus:
    caracteres_validos += string.ascii_uppercase
if usar_nums:
    caracteres_validos += string.digits
if usar_simb:
    caracteres_validos += string.punctuation

# Variable para almacenar la cadena final
contrasena_generada = ""

# Estructura repetitiva (for) para compilar la cadena caracter por caracter
for i in range(longitud):
    # random.choice selecciona un caracter aleatorio del pool que construimos
    contrasena_generada += random.choice(caracteres_validos)

# ==========================================
# CAPA DE SERVICIOS Y SALIDA (Output)
# ==========================================
print("\n" + "="*40)
print(f"ÉXITO: Tu contraseña generada es: {contrasena_generada}")
print("="*40 + "\n")
