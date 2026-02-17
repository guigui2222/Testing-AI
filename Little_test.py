import random

# définition du neurone

class Neurone:
    def __init__(self, Input, weight):
        self.input=Input
        self.output=0
        self.weight=weight
    def forward(self):
        return(sum(self.input)*self.weight)

# création du neurone

a=Neurone([2, 1, 4], random.uniform(0, 2))

# création d'une population et test de capacités

meilleur=a.weight

while True:
    
    a=Neurone([random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)], random.uniform(0, 2))
    
    résultats={}

    for i in range(5):
        a.weight=meilleur+random.uniform(-0.1, 0.1)
        résultats[a.weight]=a.forward()
        
# notation des résultats de chaque individu de la population
    meilleur=min(résultats, key=lambda x:(résultats[x]))
    
    print(meilleur1)

