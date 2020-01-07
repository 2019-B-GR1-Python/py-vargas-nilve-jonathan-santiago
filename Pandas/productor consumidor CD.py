'''
Productor  Consumidor con Turno e Indicador
@author: Leo
'''

import threading
import random
from time import sleep
from _ast import Num

buffer = [];
MAX_NUM = 10;
Contador = 0;
procesos=10;
cogiendonumero = [False]*procesos;
numprocesos = [0]*procesos;

class Productor(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num=num
        
    
    def run(self):
        print("\n soy el hilo " + str(self.num)+" productor con buffer " )
        global Contador  ;
        global procesos;
        global cogiendonumero;
        #print("\n cogiendonumero " + str(cogiendonumero) )
        global numprocesos;
        #print("\n numprocesos " + str(numprocesos))
        cogiendonumero[self.num]=True;
        numprocesos[self.num]=1+max(numprocesos);
        cogiendonumero[self.num]=False;
        
        #print("\n cogiendonumero antes comparacion " + str(cogiendonumero) )
        print("\n Proceso:"+str(self.num)+" numprocesos antes comparacion" + str(numprocesos))
        
        for j in range (0,procesos):
            #print(" "+str(self.num)+"j:"+str(j))
            if(self.num==j): continue;
            while (cogiendonumero[j]):
                pass;
            if(numprocesos[j]==0):continue;
            test = (numprocesos[j]<numprocesos[self.num]) or ((numprocesos[j] == numprocesos[self.num]) and j<self.num);
            #print("\n Pid:"+str(self.num)+" j:"+str(j)+" test:"+str(test));
            while(((numprocesos[j] != 0) and (numprocesos[j]<numprocesos[self.num])) or (numprocesos[j] == numprocesos[self.num] and j<self.num)):
                pass;
        
        #Seccion Critica         
        while(Contador==MAX_NUM):
            pass;
        print("se va a agregar el dato:"+str(self.num));
        
        buffer.append(self.num);
        print("dato guardado: "+str(self.num))  ;
        #sleep(2);  
        Contador=Contador+1;
        print("Contador: "+str(Contador));
        
        #Fin seccion critica
        numprocesos[self.num]=0;
        #print("Proceso "+str(self.num)+" numprocesos despues de salir de RC:"+str(numprocesos));

        

class Consumidor(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num=num
    
    def run(self):        
        print("\n soy el hilo consumidor "+str(self.num) + " con buffer ");
        global Contador;

        global cogiendonumero;
        
        global numprocesos;
        global procesos;
        
        cogiendonumero[self.num]=True;
        numprocesos[self.num]=1+max(numprocesos);
        cogiendonumero[self.num]=False;
        
        #print("\n cogiendonumero antes comparacion " + str(cogiendonumero) )
        print("\n Proceso:"+str(self.num)+" numprocesos antes comparacion" + str(numprocesos));
        for j in range (0,procesos):
            #print(" "+str(self.num)+"j:"+str(j));
            if(self.num==j): continue;
            while (cogiendonumero[j]):
                pass;
            if(numprocesos[j]==0):continue;
            test = (numprocesos[j]<numprocesos[self.num]) or ((numprocesos[j] == numprocesos[self.num]) and j<self.num);
            #print("\n Pid:"+str(self.num)+" j:"+str(j)+" test:"+str(test));
            #while((numprocesos[j]<numprocesos[self.num]) or ((numprocesos[j] == numprocesos[self.num]) and j<self.num)):
            while(((numprocesos[j] != 0) and (numprocesos[j]<numprocesos[self.num])) or (numprocesos[j] == numprocesos[self.num] and j<self.num)):
                pass; 
               # if(self.num==6):
                    #print("Proceso"+str(self.num)+"bloqueado")
                    #print("\n Pid:"+str(self.num)+" j:"+str(j)+" test:"+str(test));
                    #print("\n"+str(numprocesos[j])+" < "+str(numprocesos[self.num]));
                    
                
                
        
        #Seccion Critica
        #print("Ingreso a Region critica proceso: "+str(self.num)+" con Contador: "+str(Contador));
        
        while(Contador==0):
            pass;

        
        
        print("Buffer: "+str(buffer));
        datoBuffer = buffer.pop(Contador-1);
        print("Dato leido: "+str(datoBuffer));
        sleep(2) #add    
        Contador=Contador-1;
        print ("Contador "+str(Contador));
               
               
        numprocesos[self.num]=0;
        print("Proceso "+str(self.num)+" numprocesos despues de salir de RC:"+str(numprocesos));
        #Fin Seccion Critica  

        

if __name__ == '__main__':
    print("Starting Test")
    
    Productores = [Productor(0), Productor(1),Productor(2), Productor(3),Productor(4)]
    
    for h in Productores:
        h.start();
        #sleep(1) #comment
    
   # sleep (2) #comment
    
    Consumidores = [Consumidor(5), Consumidor(6),Consumidor(7),Consumidor(8), Consumidor(9)]
    
    for m in Consumidores:
        m.start();
        #sleep(1) #comment

    

 
    
    
    
