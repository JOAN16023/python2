#basicos
for i in range (1,11):
    print(i)

#multiplos de 5 
for q in range(5, 101, 5): #el ultinmo de este range osea el 5, es de la manera que elegimos en que va a llevar al 101, osea ira de 5 en 5
    print(q)
    
#contando al estilo dojo
for y in range(5, 101):
    if y % 10 == 0:
        print("coding dojo")
    elif y % 5 == 0:
        print("coding")
    else:
        print(y)

#whao impares
for i in range (0, 50, 3):
    print(i)
  
#cuenta regresiva
for i in range (2018, 1, -4):
    print(i)


#contador flexibles
lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)