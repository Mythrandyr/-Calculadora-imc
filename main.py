# la funcion es para dar la bienvenida al programa
def start():
    print ('Hola bienvenido a la calculadora de IMC')

# la funcion es para definir una longitud de string e identificar si es nulo
def validationString(mensaje, mensaje_while, longitud):
  dato = input(mensaje).strip()
  while dato == "" or len(dato) < longitud:
    dato = input(mensaje_while).strip()
  return dato

#  la funcion es para definir datos float validos y mayores a 0
def isFLoat(number):
  try:
    isValid=float(number)
    if isValid<0:
      return False
    return True
  except ValueError:
    return False
    
    # esta funcion es para definir que el dato float no sea 0
def validationFloat(mensaje, mensaje_while):
  numero = input(mensaje).strip()
  while isFLoat(numero) == False or numero =='0':
    numero = input(mensaje_while).strip()
  return float(numero)

# esta funcion es  para calcular el imc
def formulaImc(peso,altura):
  return peso/(altura*2)

# esta funcion es para arrojar los datos relativos al calculo de tu imc
def indicesImc(imc): 
  if imc <= 18.49:
    return 'bajo metele proteina'
  elif imc <= 24.99:
    return 'peso normal felicidades'
  elif imc <= 29.99:
    return 'sobrepeso deja la coca cola'
  elif imc <= 34.99:
    return 'obesidad leve la bascula lloro'
  elif imc <= 39.99:
    return 'obesidad media aiudaaaa'
  elif imc >= 40.0:
    return 'obesidad morbida come mas lechuga'

 # esta funcion es para correr el programa 
def run():
  start()
  enable = True
  while enable:
    nombre = validationString('Ingresa un nombre de al menos 4 letras: ', 'Información no válida, intenta de nuevo: ', 4)
    apellidoPaterno = validationString('Ingresa tu apellido paterno de al menos 4 letras: ', 'Información no válida, intenta de nuevo: ', 4)
    apellidoMaterno = validationString('Ingresa tu apellido materno de al menos 4 letras: ', 'Información no válida, intenta de nuevo: ', 4)
    peso = validationFloat('Por favor ingresa tu peso: ', 'Informacion no valida, intenta de nuevo: ' )
    altura = validationFloat('por favor ingresa tu altura: ' , 'Informacion no valida, intenta de nuevo: ')
    imc = formulaImc(peso,altura)

    print(f"Hola estos son tus datos: este es tu nombre {nombre} {apellidoPaterno} {apellidoMaterno} Tu peso es {peso}kgs Tu altura es {altura}mts Tu imc es {imc} {indicesImc(imc)} ")
    enable = input('presiona x para salir').lower()!='x'

run()