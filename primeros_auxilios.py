
estimulos = input("responde a estímulos?: ").lower()

if estimulos == "si": 
    print("enviarlo al hospital más cercano")
else:
    print("abrir via aérea")    

respira = input("respira?: ").lower()
if respira == "si": 
    print("permitirle posición de suficiente ventilación")
else:
    print("administrar 5 ventilaciones y llamar ambulancia")  
      
    ambulancia = "no"
    while ambulancia == "no":
        signos_vida = input("signos de vida?: ").lower()

        if signos_vida == "si": 
            print("reevaluar a la espera de la ambulancia") 
        else:
            print("administrar compresiones torácicas hasta que llegue ambulancia")

        ambulancia = input("llego la ambulancia?: ")
print("programa terminado")
    



    
   
     
   




     
         

 
       
