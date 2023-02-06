import numpy as np
import numpy.random as rd

if __name__ == '__main__':
    avgs = rd.rand(10)*10 - 5
    k = 10
    Q = np.zeros(10)
    N = np.zeros(10)
    R_total = 0
    epsilon = 1 / 10
    for i in range(1000):
        A = Q.argmax()
        if rd.rand() < epsilon:
            A = rd.randint(0, k - 1)
            pass
        R = rd.normal(avgs[A], 1, 1)
        N[A] = N[A] + 1
        Q[A] = Q[A] + (1 / N[A]) * (R - Q[A])
        R_total += R
        pass
    print(Q, "\n", avgs, "\n", N, "\n", R_total)
    pass