import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def deltaH(i,j,S,N):
    return -2*S[i,j]*(S[i-1,j]+S[(i+1)%N,j]+S[i,(j+1)%N]+S[i,j-1])

def transition(S,N,beta):
    (i,j)=np.random.randint(N,size=2)                  # choix d'une position aléatoire dont on va modifier le spin 
    if np.random.rand()<np.exp(beta*deltaH(i,j,S,N)):
        S[i,j]*=-1 
    return S


# Definition de DeltaH et de la fonction de transition           
def deltaH_im(i,j,S,c,N,I):
    return -2*S[i,j]*(S[i-1,j]+S[(i+1)%N,j]+S[i,(j+1)%N]+S[i,j-1]+2*c*(2*I[i,j]-1)) 

def transition_im(S,N,c,beta,I):
    (i,j)=np.random.randint(N,size=2)                  # choix d'une position aléatoire dont on va modifier le spin 
    if np.random.rand()<np.exp(beta*deltaH_im(i,j,S,c,N,I)):
        S[i,j]*=-1 
    return S
