#----- leer operaciones
import re
number=[]
operacion=[]
#---read data
with open("activitat11/operacions.txt", encoding = 'utf-8') as f:

   for x in f.readlines() :
        res=re.split("[ \\n]",x)
        operacion.append(' '.join(res))
        match res[1]:
            case "+":
                resultat=lambda x,y: x+y
            case "-":
                resultat=lambda x,y: x-y
            case "*":
                resultat=lambda x,y: x * y
            case "/":
                resultat=lambda x,y: x/y    
            case _:
                print("I have an Error!! i can't work !")
    
        number.append(str(resultat(int(res[0]),int(res[2]))))

#---Write data
with open("activitat11/resultats.txt",'w',encoding = 'utf-8') as f:
    i = 0
    while i < len(operacion):
        f.write(str(operacion[i]))
        f.write(" = ")
        f.write(str(number[i]))
        f.write("\n")
        i += 1
   
print("Writing it's Done !")


 
   



