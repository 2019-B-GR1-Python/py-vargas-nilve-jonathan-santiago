"""
Created on Thu Nov 28 17:17:11 2019

@author: jonat
"""

from threading import Thread
from random import randint
from time import sleep


class Producer (Thread):
    def __init__(self,t,q,a,b,p):
        print("empieza el constructor")
        Thread.__init__(self, name = t)
        self.queue = q
        self.begin = a
        self.end = b
        self.pace = p


    def run(self):
        print(f"{self.getName()} starts ...")
        
        for i in range(self.begin, self.end + 1):
            rnd = randint(1,self.pace)
            print(f"{self.getName()} sleeps %d seconds % {rnd}")
            sleep(rnd)
            
            print(f"appending %d to queue % {i}")
            self.queue.append(i)
            
        print("Production terminated")
        
    def main():
        que = []
        prd = Producer('producer',que,3,9,10)
        prd.start()
        prd.join()
        
    if __name__== "__main__":
        main()
        
        
class Consumer(Thread):
    
    def __init__(self,t,q,n,p):
        
        Thread.__init__(self,name = t)
        self.queue = q
        self.amount = n
        self.pace = p
        
        
    def run(self):
        print ("consumption starts ...")
        
        for i in range (0,self.amount):
            rnd = randint(1,self.pace)
            print(f"{self.getName()} sleeps %d seconds % {rnd}")
            sleep(rnd)
            while True:
                try:
                    i = self.queue.pop(0)
                    print("popped %d from queue % {i}")
                    break
                except IndexError:
                    print ("wait a second ...")
                    sleep(1)
                    
        print("consumption terminated")
        
    def main():
        que = range(5)
        cns = Consumer('consumer', que, 5 , 10)
        cns.start()
        cns.join() 

    if __name__== "__main__":
        main()
    
    

import Producer
    
    
    