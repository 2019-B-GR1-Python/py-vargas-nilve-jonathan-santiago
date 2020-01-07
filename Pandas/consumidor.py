# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 23:16:42 2019

@author: jonat
"""

''''
@author: Group5
'''
import random
from time import sleep
from _ast import Num
from threading import Semaphore, Thread

buffer = []
MAX_NUM = 5
valorA = 0
valorB = 0
valorC = 0
valorD = 0

posLibres = Semaphore(MAX_NUM) 
posOcupadas = Semaphore(0)

class Proceso1(Thread):
    def __init__(self,num):
        Thread.__init__(self)
        self.num=num
        
    def run(self):
        global valorA, valorB, valorC, valorD
        print("Soy el hilo " + str(self.num)+" del Proceso 1")

        posLibres.release()
        valorA = int(input("Ingrese El valor de A \n"))
        print("El valor de A ingresado es = ", valorA)     
        posOcupadas.acquire()
        #3sleep(2)
        posLibres.release()
        valorC = valorA + valorB
        print("El valor de C calculado es = ", valorC)
        valorB = 2 * valorD
        print("El valor de B calculado es = ", valorB)
        posOcupadas.acquire()


class Proceso2(Thread):
    def __init__(self,num):
        Thread.__init__(self)
        self.num=num
    
    def run(self):
        global valorA, valorB, valorC, valorD
        print("Soy el hilo "+str(self.num) + " del Proceso 2")

        posLibres.acquire()  
        valorC = int(input("Ingrese el valor de C \n"))
        print("El valor de C ingresado es = ", valorC)
        #posOcupadas.release()

        #posLibres.acquire()
        valorD = int(input("Ingrese el valor de D \n"))
        print("El valor de D ingresado es = ", valorD)
        posOcupadas.release()

        posLibres.acquire()    
        #sleep(2)
        valorB = valorA + valorD + valorC
        print("El valor de B luego del segundo proceso B calculado es = ", valorB)
        posOcupadas.release()
        
        

if __name__ == '__main__':
    print("Starting Test")
    Procesos = []
    Procesos.append(Proceso1(1))
    Procesos.append(Proceso2(2))

    for h in Procesos:
        h.start()
        
