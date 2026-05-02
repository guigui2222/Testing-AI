def loss(a, y):
    
    return (a-y)*(a-y)
    
def loss_prime(a0, w, b, a1, y):
    
    if a1>=0:
        
        return [2*(a0-y)*w, 2*(a0-y)*a1, 2*(a0-y)]
        
    if a1<0:
        
        return [0, 0, 0]