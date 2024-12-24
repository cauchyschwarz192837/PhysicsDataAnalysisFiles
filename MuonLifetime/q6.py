import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    t_TTL = 0.00001
    with open('newdata.dat', 'r') as f:
        data = f.readlines()
    num_data = [float(x) for x in data]
    adjust_num_data = [elem + t_TTL for elem in num_data]

    N_total = len(adjust_num_data)
    t_total = sum(adjust_num_data)
    mean_rate_mu = N_total / t_total

    delta_t_star = 1e-5
    edges = np.linspace(2e-7, delta_t_star, 100)
    below_data = [x for x in adjust_num_data if x < delta_t_star]
    counts, bin_edges = np.histogram(below_data, bins=edges)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    dt = bin_edges[1:] - bin_edges[:-1]

    H_model = N_total * mean_rate_mu * np.exp(-1 * mean_rate_mu * bin_centers) * dt

    extra_counts = counts - H_model

    plt.bar(bin_centers, extra_counts, width=np.diff(bin_edges), alpha=0.7, color='purple', label='Extra Counts', align='center')

    plt.xlabel('Time Interval')
    plt.ylabel('Extra Counts')
    plt.title(f'Histogram of Extra Counts')
    plt.legend()
    plt.show()
