lista2=[3,4,2,8,12,10,4,19]

lista_par=list(filter(lambda  x: x % 2  == 0 ,lista2))
lista_impar=list(filter(lambda x:x % 2 != 0,lista2))

print("Los numeros pares : \t",lista_par,'\n y Impares :\t', lista_impar )