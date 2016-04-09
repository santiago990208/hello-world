for i in range (0,11,5):
    print i
print "1. calculadora"
print"2. par o impar"

a = int(raw_input ("digite 1 o 2"))
while a==1 or a==2 :
 if a==1 :
    print " calculadora"
    b=float(raw_input ("digite un numero"))
    c=float(raw_input ("digite un numero"))
    d=(raw_input("escoja que operacion quiere"))
    if d=="*" or "multiplicacion":
        print b*c
    if d=="-" or "resta":
        print b-c
    if d=="+" or "suma":
        print b+c
    if d=="/" or "division":
        if c != 0:
            print b/c
        
 if a==2 :
    print "par o impar"
    e=int(raw_input("digite un numero"))
    if e%2==0:
          print "par"
    else:
          print "impar"
000000000000000000000000000000000000000000000000000000000000000000000000000000
          
    
        
                
