import numpy as np
def solverouting(R):
    n = R.shape[1]
    I = np.identity(n)
    Q = np.c_[R - I, np.ones(n)]
    b = np.c_[np.zeros(n).reshape(1,n), np.ones(1)]
    Q_t = Q.transpose()
    v = np.matmul(np.matmul(b, Q_t), np.linalg.inv(np.matmul(Q, Q_t)))
    return(v)







































































