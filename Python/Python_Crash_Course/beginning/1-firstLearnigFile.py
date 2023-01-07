    #CHAPTER 2
#Changing Case In String In Methods#
name = "tu mamaTambien"
print (name.title())  # al poner el .title hace que la primera letra de cada palabra sea mayuscula, 
#si hay una mayuscala en medio de la misma palabra, ésta se vuelve minúscula. 
print (name.upper())    # al poner .upper convierte todas las letras en mayusculas.
print (name.lower())    # al pner .lower convierte toda letra de las palabras en minusculas.

#Using Variables in Strings#
first_name = "Lidwin" # delaramos los valores de esta manera, poniendo simplemente el nombre de la variable 
#y su valor. En esto caso, un valor en formato "String"
last_name = "Gasca"
full_name = f"{first_name} {last_name}" # esta variable tiene como valor un string compuesto por por dos 
#variables que su vez tambien serán string, Ojo que por ello mismo este no es un simple string que contiene dos 
# variables dentro, se llama f-string y se usa para insertarle variables en su interior, sin importar si estas 
# mismas son de formato string o numero.
print(full_name)
print(f"Hola mundo soy {first_name} estoy aprendiendo Python, mi apellido es {last_name}. Acompañame en mi aventura")
print(f"Hello, {full_name.title()}!")
messege = f"Hello, {full_name.title()}!"  # tambien pudo ser al estilo viejito full_name = "{}{}".format(first_name, last_name)
print(messege)

#Adding Whitespace To Strings with Tabs or Newlines
print("Python")
print("\tPython")
