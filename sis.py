print("oal ajdioajfnvaiie9")

lista=[15,"nombre",3.1415,True]

print(lista[3])


ususario=["usertnameTest1","pas123","correo@correo.cl"]

numero=[10,50,100,255.500]

#--------------------------------------------------------------

#aprend= agrega un objeto en la ultima posicion

numero.append(1000)
print(numero)


#----------------------------------------------
#extend= agrega un arreglo al final de nuestra list

extra=[75,350,990]


numero.extend(extra)
print(numero)

#----------------------------------------------------------

#insert= agregar valor en pocision especifica

numero.insert(6,5000)
print(numero)

#---------------------------------------------
#remove= entrega valor, se busca y se elimina
numero.remove(50)
print(numero)

#------------------------------------------
#reverse=inserte el orden de la lista

numero.reverse()
print(numero)
#sort=ordena los valores de menor a mayor 
#sort(reverse-true) = ordena los valores de ,ayor a ,emor
numero.sort()
print(numero)
numero.sort(reverse=True)
print(numero)
 





