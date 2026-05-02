import random
class Neuron:
    
    def __init__(self, input_nbr=None, layer=None, input_w=None, next=None, biais=None):
        self.input_nbr=input_nbr
        self.layer=layer
        self.input_w=input_w
        self.next=next
        self.activation=0
        self.z=0
        self.moyenne_v=[]
        self.biais=biais
        
        
    def reLu(self):
        
        self.activation=max(0, self.z)
        
    def forward(self):
        
        for i in self.input_nbr:

            self.z+=i*self.input_w[self.input_nbr.index(i)]
            
        self.z+=self.biais
        
        self.reLu()
        
        if self.next!=None:
            
            for i in self.next:
                
                i.input_nbr.append(self.activation)
