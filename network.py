from neuron import *
from function import *

class Network:
    
    def __init__(self, layers):
        
        network=[]
        
        for l in layers:
            
            lyr=[]
            
            for neu in range(l):
                
                n=Neuron(input_nbr=[])
                
                lyr.append(n)
                
            lyr[0].layer=lyr
            
            network.append(lyr)

        w=[1]
        
        for layr in network:
            
            for neu in layr:
                
                if network.index(layr)+1!=len(network):
                    
                    neu.next=network[network.index(layr)+1]
                    
                neu.input_w=w*len(network[network.index(layr)-1])
                
                neu.biais=random.uniform(-1, 1)
                
                if network.index(layr)==0:
                   
                     neu.input_w=w
        
        self.input_nbr=[]
        
        self.network=network
        
        self.output_nbr=0

    def run(self):
        
        for neu in self.network[0]:
            
            neu.input_nbr=[self.input_nbr[self.network[0].index(neu)]]
            
        for layer in self.network:
            
            for neu in layer:
                
                neu.forward()
                
        resultat=[]
         
        for neu in self.network[len(self.network)-1]:
            
            resultat.append(neu.activation)
        self.output=resultat
        
        return resultat
        
    
    def clear(self):
        
        for layer in self.network:
            for i in layer:
                i.input_nbr=[]
                i.activation=0
                i.moyenne_v=[]
                i.z=0
            
    def backpropagation(self, y):
        
        arch=[]
        
        for layer in self.network:
            
            arch.insert(0, layer)
        
        for layer in arch:
            
            for neu in layer:
                
                if neu.next!=None:
                    
                    
                    y[layer.index(neu)]=neu.activation-sum(neu.moyenne_v)/(len(neu.moyenne_v)+0.001)
                    
                for w in neu.input_w:
                    
                    erreur=loss_prime(neu.activation, w, neu.biais, neu.input_nbr[neu.input_w.index(w)], y[layer.index(neu)], )
                    
                    if layer!=self.network[0]:
                        layer_nxt=arch[arch.index(layer)+1]
                        
                        neu_nxt=layer_nxt[neu.input_w.index(w)]
                        
                        neu_nxt.moyenne_v.append(0.01*erreur[0])
                    
                    neu.input_w[neu.input_w.index(w)]=w-0.01*erreur[1]
                    
                    neu.biais-=0.01*erreur[2]
    def reward(self, reward):
        
        excepted=[]
        
        for i in self.output:
            if i==self.output_nbr:
                reward.append(self.output_nbr*reward)
            else:
                reward.append(0)
                
        self.backpropagation(excepted)