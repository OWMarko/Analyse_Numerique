import numpy as np 

#élémentaire
def quadraNumTT(f,a,b): 
  return (b-a) * (f(a)+f(b))/2


#Composé non uniforme
def quadraNumTT_nnuni(f,x):
  h = np.diff(x) #x[1] - x[0]
  return sum(h * (f([x1:]+f(x[:-1]) /2 #sinon tu peux aussi mettre x[1;] - x[:-1] à la place du h

#Composé uniforme
def quadraNumTT_uni(f,a,b,M):
    h 
                    

