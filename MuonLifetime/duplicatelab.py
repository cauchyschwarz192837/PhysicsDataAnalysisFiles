# LAB 4
import matplotlib.pyplot as plt
import numpy as np
import math

if __name__ == "__main__":
    t_TTL = 1e-7 # test

    with open('newdata.dat', 'r') as f:
        data = f.readlines()
        num_data = []
        for x in range(len(data)):
            num_data.append(float(data[x]))

    adjust_num_data = [elem + t_TTL for elem in num_data]  #-------------------- (1)

#-------------------------------------------------------------------------------

    N_total = len(adjust_num_data)

    t_total = 0.0
    for elem in adjust_num_data:
        t_total += elem

    mean_rate_mu = N_total / t_total  #-------------------- (2)

#-------------------------------------------------------------------------------

    logedges = np.linspace(-7.0, 0.0, 71)
    edges = 10 ** logedges
    counts = plt.hist(adjust_num_data, bins = edges)[0]

    tc = (edges[1:] + edges[:-1]) / 2  # bin centers
    dt = edges[1:] - edges[:-1]  # bin widths

# Experimental

    plt.hist(adjust_num_data, bins = edges)  #-------------------- (2)
    plt.show()

#-------------------------------------------------------------------------------

    N_meas_dicrepancy = 0 
    for i in adjust_num_data:
        if i < math.pow(10, -5):
            N_meas_dicrepancy += 1

    print(N_meas_dicrepancy)

#-------------------------------------------------------------------------------

    H_model = N_total * mean_rate_mu * np.exp(-1 * mean_rate_mu * tc) * dt

    N_exp_dicrepancy = 0 
    for i in range(len(tc)):
        if tc[i] < math.pow(10, -5):
            N_exp_dicrepancy += H_model[i]

    print(N_exp_dicrepancy)

    plt.plot(tc, H_model)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
