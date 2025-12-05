import numpy as np

def lagrange_interpolation_basique(x_nodes, y_nodes, x_eval):
    for i in range(n):
        #Calcul du L_i(x_eval)
        L_i = 1.0
        for j in range(n):
            if j != i:
                L_i *= (x_eval - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        P_x += y_nodes[i] * L_i
    return P_x

import numpy as np

def lagrange_interpolation_vectorise(x_nodes, y_nodes, x_eval):
    x_nodes = np.array(x_nodes, dtype=float)
    y_nodes = np.array(y_nodes, dtype=float)
    x_eval = np.array(x_eval, dtype=float)
    n = len(x_nodes)
  
    diff = x_eval[:, None, None] - x_nodes[None, None, :]
    numerateur = np.prod(np.where(np.eye(n, dtype=bool)[None, :, :], 1, diff), axis=2)
    denom = np.prod(np.where(np.eye(n, dtype=bool), 1, x_nodes[:, None] - x_nodes[None, :]), axis=1)
  
    L = numerateur / denom[None, :]
    P_x = np.sum(y_nodes[None, :] * L, axis=1)

    return P_x if P_x.size > 1 else P_x.item()
