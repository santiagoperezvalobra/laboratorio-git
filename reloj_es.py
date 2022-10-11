
from datetime import datetime
hora_string={00:"las doce",1:"La una",2:"las dos",3:"las tres", 4:"las cuatro",5:"las cinco",6:"las seis",7:"las siete",8:"las ocho",
9:"las nueve",10:"las diez",11:"las once",12:"las doce", 13:"la una",14:"las dos",15:"las tres",16:"las cuatro",
17:"las cinco",18:"las seis",19:"las siete",20:"las ocho",21:"las nueve",22:"las diez",23:"las once",24:"las doce",
25:"la una"}

minuto_string={00:"en punto",5:"y cinco",10:"y diez",15:"y cuarto",20:"y veinte",25:"y veinticinco",30:"Y media",
35:"y treinta y cinco",40:"menos veinte",45:"menos cuarto",50:"menos diez",55:"menos cinco"}

hora=int(datetime.now().hour)
minuto=int(datetime.now().minute)

if minuto not in minuto_string:
    minuto=(minuto//5)*5
if minuto>=40:
    hora+=1
    
m=minuto_string.get(minuto)
h=hora_string.get(hora)
resultado = (f"Son {h} {m}")
print(resultado)