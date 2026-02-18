# This program is a litle test where I made
# a neuron which has 3 random number
# in input and an output synaps with a weight. It make than the sum of them
# and multiply it by the synaps weight: realy basic.
# I use a kinf of natural selection algorithm which repeat indefinitely.
# and returns the weight of the best neuron of the generation.
import random

# definition of a neuron

class Neuron:
    def __init__(self, input_nbr, weight):
        self.input=input_nbr
        self.output=0
        self.weight=weight
    def forward(self):
        return(sum(self.input)*self.weight)

# creation of the neuron

a=Neuron([2, 1, 4], random.uniform(0, 2))

# creation of a neuron population and testing it capacities

meilleur=a.weight

while True:
    
    a=Neurone([random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)], random.uniform(0, 2))
    
    résultats={}

    for i in range(5):
        a.weight=meilleur+random.uniform(-0.1, 0.1)
        résultats[a.weight]=a.forward()
        
# rating every neuron's synaps's weight and chosing the best
    meilleur=min(résultats, key=lambda x:(résultats[x]))
    
    print(meilleur1)

