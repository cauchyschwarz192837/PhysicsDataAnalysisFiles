# LAB 4
import matplotlib.pyplot as plt
import numpy as np

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

    mean_rate_mu = N_total / t_total
    print(N_total, t_total, mean_rate_mu)   #-------------------- (2)

#-------------------------------------------------------------------------------

    mybins = np.linspace(0, 1, 101)
    counts = plt.hist(adjust_num_data, bins = mybins)[0]

#-------------------------------------------------------------------------------

    tc = (mybins[1:] + mybins[:-1]) / 2
    dt = mybins[1:] - mybins[:-1]

    H_model = N_total * mean_rate_mu * np.exp(-1 * mean_rate_mu * tc) * dt

# Experimental
    plt.xlabel('Time between pulses / s')
    plt.ylabel('Frequency')
    plt.title('Detected time intervals between pulses')
    plt.hist(adjust_num_data, bins = mybins)
    plt.plot(tc, H_model)
    plt.show()


    



