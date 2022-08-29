import numpy as np
import sys
from tabulate import tabulate

def solverouting(R):
    n = R.shape[1]
    I = np.identity(n)
    Q = np.c_[R - I, np.ones(n)]
    b = np.c_[np.zeros(n).reshape(1,n), np.ones(1)]
    Q_t = Q.transpose()
    v = np.matmul(np.matmul(b, Q_t), np.linalg.inv(np.matmul(Q, Q_t)))
    return(v)

def mmc(lam, mu, c, tol):
    # Single Server Markovian Model
    if(c == 1): 
        # Traffic intensity
        rho = lam/mu
        if(rho < 1): print("System is stable.")
        else:
            sys.exit("System is unstable.")
        # pn := steady state probability of n in the system.
        # That is, p0 is the probability of no entities in system,
        # p1 is the probability of one entity in the system, and so on.
        pn = []
        n = 0
        while(np.sum(pn) < (1-tol)):
            # Uses the geometric probability function
            pn.append((rho**n)*(1-rho))
            n += 1
        # Mean number in system
        L = rho/(1-rho)
        # Mean number in queue
        Lq = (rho**2)/(1-rho)
        # Mean time in system
        W = 1/(mu-lam)
        # Mean time in queue
        Wq = rho/(mu - lam)
        # Idle time
        I = 1-rho
        res = [["Traffic intensity", rho],
              ["Idle time", I],
              ["Mean time in system", W],
              ["Mean time in queue", Wq],
              ["Mean number in system", L],
              ["Mean number in queue", Lq]]
        print(tabulate(res, headers=["Definition", "Result"]))
        
        return(pn, rho, L, Lq, W, Wq, I)
