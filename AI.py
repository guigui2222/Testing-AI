import random
class Neuron:

    def __init__(self, input_nbr=None, layer=None, input_w=None, next=None):
        self.input_nbr=input_nbr
        self.layer=layer
        self.input_w=input_w
        self.next=next
        self.activation=0
        self.moyenne_v=[]

    def forward(self):
        
        if self.input_w==None:
            self.activation=sum(self.input_nbr)
        for i in self.input_nbr:

            self.activation+=i*self.input_w[self.input_nbr.index(i)]
        self.activation=self.activation/len(self.input_nbr)
        if self.next!=None:
            for i in self.next:
                i.input_nbr.append(self.activation)
            
        
            
    def run(self):
      output=[]
      while True:
          for i in self.layer:
              i.forward()
          if self.next!=None:
              self=self.next[0]
          else:
              print("________________________________________________\n________________________________________________")
              for i in self.layer:
                  print(f"{i} : {i.activation}")
                  output.append(i.activation)
              break 
      return(output)
            
          
    def clear(self):
        while True:
            
            for i in self.layer:
                i.input_nbr=[]
                i.activation=0
                i.moyenne_v=[]
            if self.next!=None:
                self=self.next[0]
            else:
                break
    def stock(self):
        
        network={self:[]}
        
        while True:
            
            for i in self.layer:
                network[i]=i.input_w
            
            if self.next!=None:
                self=self.next[0]
            else:
                break
            
            
        return network
    def arch(self):
        network=[]
        while True:
            print(self)
            network.insert(0, self.layer)
            if self.next!=None:
                self=self.next[0]
            else :
                break
        return network
def loss(w, a, y):
        
    return((w*a-y)*(w*a-y))
def loss_prime(w, a, y):
    return [2*w*a*a-2*y*a, 2*a*w*w-2*y*w]

def backpropagation(arch, y, layer1):
    for layer in arch:
        for neu in layer:
            if neu.next!=None:
            
                y[layer.index(neu)]=neu.activation-sum(neu.moyenne_v)/len(neu.moyenne_v)
                
            for w in neu.input_w:
                
                erreur=loss_prime(w, neu.input_nbr[neu.input_w.index(w)], y[layer.index(neu)])
                if layer !=layer1:
                    layer_nxt=arch[arch.index(layer)+1]
                    neu_nxt=layer_nxt[neu.input_w.index(w)]
                    neu_nxt.moyenne_v.append(0.1*erreur[0])
                print(erreur)
                neu.input_w[neu.input_w.index(w)]=w-0.1*erreur[1]
            




def change(network):
        
    for neu, w in network.items():
        neu.input_w=w




n3_2=Neuron(input_nbr=[], input_w=[random.uniform(0, 1), random.uniform(0, 1)])
n3_1=Neuron(input_nbr=[], input_w=[random.uniform(0, 1), random.uniform(0, 1)])
n2_2=Neuron(input_nbr=[], input_w=[random.uniform(0, 1), random.uniform(0, 1)], next=[n3_1, n3_2])
n2_1=Neuron(input_nbr=[], input_w=[random.uniform(0, 1), random.uniform(0, 1)], next=[n3_1, n3_2])
n1_2=Neuron(input_nbr=[1], input_w=[random.uniform(0, 1)], next=[n2_1, n2_2])
n1_1=Neuron(input_nbr=[0], input_w=[random.uniform(0, 1)], next=[n2_1, n2_2])
n1_1.layer=[n1_1, n1_2]
n2_1.layer=[n2_1, n2_2]
n3_1.layer=[n3_1, n3_2]
for i in range(1000):
    n1_1.run()
    print(loss(n3_1.input_w[0], n3_1.input_nbr[0], 1))
    a=input()
    backpropagation(n1_1.arch(), [1, 0], n1_1.layer)
    n1_1.clear()
    n1_1.input_nbr=[0]
    n1_2.input_nbr=[1]
