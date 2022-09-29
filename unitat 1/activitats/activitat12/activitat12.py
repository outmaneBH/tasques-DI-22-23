#----- leer operaciones
import re,sys
number=[]
operacion=[]
#---read data
try:
    with open("activitat12/operacions.txt", encoding = 'utf-8') as f:
        for x in f.readlines() :
                res=re.split("[ \\n]",x)
                operacion.append(' '.join(res))
                try:
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
                except Exception as ex:
                    print("Error :",ex)
                    
    #---Write data
    with open("activitat12/resultats.txt",'w',encoding = 'utf-8') as f:
        i = 0
        while i < len(operacion):
            f.write(str(operacion[i]))
            f.write(" = ")
            f.write(str(number[i]))
            f.write("\n")
            i += 1
    
    print("Writing it's Done !")
   
except FileNotFoundError as e:
    print(e)
except Exception as ex:
    print("Error :",ex)
    pass
       



 
   



