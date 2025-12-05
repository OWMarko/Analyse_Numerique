import numpy as np
from scipy.optimize import fsolve

def Euler_Explicite(t0, tf, f, y0, N):
    h = (tf - t0) / N
    t = np.linspace(t0, tf, N+1) 
    y0 = np.atleast_1d(y0) 
    m = y0.size 
    y = np.zeros((m, N+1)) 
    y[:, 0] = y0 
    for n in range(N):
        y[:, n+1] = y[:, n] + h * f(t[n], y[:, n])
    return t, y 


def Euler_Implicite_Newton(t0,tf,f,y0,N):
    h = T / (N - 1) 
    t = np.linspace(0, T, N) 
    x = np.zeros(N) 
    x[0] = x0 
    for k in range(1, N): 
        xk = x[k-1] 
        tk = t[k] 
        g = lambda y: y - xk - dt * f(tk, y) 
        dg = lambda y: 1 - dt * df(tk, y) 
        x[k] = Newton(xk, g, 10, 1e-10, 1e-10, tk, dt, xk) 
    return t, x

"""
Il existe plusieurs schéma d'Euler Implicite, certains utilisent l'algo de Newton, d'autres non. Dans le cours nous nous limitons à l'Euler Implicite générale, sans cas particulier comme dans l'exercice 1.2 du TP5. 
Pour ce faire, nous appliquons le même raisonnemment qu'à l'Euler Explicite le seul détail qui change est la boucle, on résoud explicitement notre équation en y[n+1]. 
"""

def Euler_Implicite(t0,tf,f,y0,N):
    h = (tf-t0)/N
    t = np.linspace(t0, tf, N+1) 
    y0 = np.atleast_1d(y0) 
    m = y0.size
    y = np.zeros((m, len(y0)) 
    y[:, 0] = y0
    for n in range(N):
        g = lambda y_suiv: y_suiv - y[n] - h * f(t[n+1], y_suiv)
        y[n+1] = fsolve(g, y[n])
    return t, y

def Point_Milieu(t0,tf,f,y0,N): 
    h = (tf-t0)/ (N-1)
    t = np.linspace(t0, tf, N)
    y0 = np.atleast_1d(y0)
    m = y0.size
    y = np.zeros((m,N) 
    y[:, 0] = y0
    for k in range(1, N):
        tk_mid = t[k-1] + h/2.
        y_mid = y[:, k-1] + (h/ 2.) * f(t[k-1], y[:, k-1])
        y[:, k] = y[:, k-1] + h* f(tk_mid, y_mid)    
    if m == 1:
        return t, x[0, :]
    return t, x

def Point_Milieu(t0,tf,f,y0,N): 
    h = (tf-t0)/ (N-1)
    t = np.linspace(t0, tf, N)
    y0 = np.atleast_1d(y0)
    m = y0.size
    y = np.zeros((m,N) 
    y[:, 0] = y0
    for k in range(N):
        t_k = t[k]
        y_k = y[k]
        t_mid = t_k + h/2.
        y_mid = y_k + (h/ 2.0) * f(t_k, y_k)
        y[k+1] = y_k + h* f(t_mid, y_mid)    
    return t, x

def Cranck_Nicolson(t0,tf,f,y0,N,tol=1e-8,maxit=50):
    h = (tf - t0) / (N - 1)
    t = np.linspace(t0, tf, N)
    y0 = np.atleast_1d(y0)
    m = y0.size
    y = np.zeros((m, N))
    y[:, 0] = y0
    for k in range(1, N):
        y_suiv = y[:,k-1].copy()
        for _ in range(maxit):
            y_nouv = y[:, k-1] + (h / 2.) * ( f(t[k-1], y[:, k-1]) + f(t[k], y_suiv))
            if np.linalg.norm(y_nouv - y_suiv) < tol:
                y_suiv = y_nouv
                break
            y_suiv = y_nouv.copy()
        y[:, k] = y_suiv
    if m == 1:
        return t, y[0, :]
    return t, y

def CrankNicolsonEx3(T,N,Y0):
    A=np.zeros((2,2))
    A[0,0]=0
    A[0,1]=1
    A[1,0]=-k/m
    A[1,1]=0
    h = T/N
    t=np.linspace(0,T,num=N+1)  
    l=np.size(Y0)
    y=np.zeros((l,N+1))
    y[:,0]=Y0[:]
    for n in range(0,N):
      y[:,n+1] = np.linalg.solve(np.eye(l)-1./2.*h*A,y[:,n]+1./2.*h*np.dot(A,y[:,n]))
    return t,y

def Runge_Kutta(t0, tf, f, y0, N):
    h = (tf - t0) / (N - 1)
    t = np.linspace(t0, tf, N)
    y0 = np.atleast_1d(y0)
    m = y0.size
    y = np.zeros((m, N))
    y[:, 0] = y0
    for k in range(1, N):
        tk = t[k-1]
        k1 = f(tk, y[:, k-1])
        k2 = f(tk + h/2, y[:, k-1] + (h/2) * k1)
        k3 = f(tk + h/2, y[:, k-1] + (h/2) * k2)
        k4 = f(tk + h, y[:, k-1] + h * k3)
        y[:, k] = y[:, k-1] + (h/6.) * (k1 + 2*k2 + 2*k3 + k4)
    if m == 1:
        return t, y[0, :]
    return t, y

