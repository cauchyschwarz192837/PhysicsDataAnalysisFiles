import numpy as np
import matplotlib.pyplot as plt

def blackbody_spectrum(lambdas, T):
    h = 6.626e-34
    c = 3.00e8
    k_B = 1.381e-23
    I_func = ((2 * np.pi * h * c**2) / (lambdas**5)) / (np.exp((h * c) / (lambdas * k_B * T)) - 1)
    return I_func

if __name__ == "__main__":
    trans_camera_green = 8.3253431e-01
    trans_camera_red = 9.3389338e-01
    trans_camera_blue = 5.8647080e-01
    trans_video_red = 6.9452750e-01
    trans_video_green = 6.7064220e-01
    trans_video_blue = 7.1580720e-01

    temp_range = np.arange(1000, 4000, 10)

    green_spectrum = blackbody_spectrum(550e-9, temp_range) * trans_camera_green * trans_video_green
    blue_spectrum = blackbody_spectrum(450e-9, temp_range) * trans_camera_blue * trans_video_blue

    gb_ratio = green_spectrum / blue_spectrum

    experimental_gb_ratio = 3.7
    uncertainty_gb = 1.04
    upper_bound_ratio = experimental_gb_ratio + uncertainty_gb
    lower_bound_ratio = experimental_gb_ratio - uncertainty_gb
    diffs_nominal = np.abs(gb_ratio - experimental_gb_ratio)
    diffs_upper = np.abs(gb_ratio - upper_bound_ratio)
    diffs_lower = np.abs(gb_ratio - lower_bound_ratio)

    temp_nominal = temp_range[np.argmin(diffs_nominal)]
    temp_upper = temp_range[np.argmin(diffs_upper)]
    temp_lower = temp_range[np.argmin(diffs_lower)]

    plt.figure(figsize=(10, 6))
    plt.plot(temp_range, gb_ratio, label='Expected ratio', color='red')
    plt.axhline(y=experimental_gb_ratio, color='blue', linestyle='-', label="Experimental ratio")
    plt.axhline(y=upper_bound_ratio, color='blue', linestyle='--', label="Upper bound")
    plt.axhline(y=lower_bound_ratio, color='blue', linestyle='--', label="Lower bound")
    plt.fill_between(temp_range, 
                     experimental_gb_ratio - uncertainty_gb, 
                     experimental_gb_ratio + uncertainty_gb, 
                     color='blue', alpha=0.2, label="Region of uncertainty")
    plt.scatter(temp_nominal, experimental_gb_ratio, color='black', zorder=5)
    plt.annotate(f"({temp_nominal}, {experimental_gb_ratio})", 
                 (temp_nominal, experimental_gb_ratio), 
                 textcoords="offset points", xytext=(50, 10), ha='center',
                 arrowprops=dict(arrowstyle="->", color='black'))
    plt.scatter(temp_upper, upper_bound_ratio, color='black', zorder=5)
    plt.annotate(f"({temp_upper}, {upper_bound_ratio:.2f})", 
                 (temp_upper, upper_bound_ratio), 
                 textcoords="offset points", xytext=(-50, 10), ha='center',
                 arrowprops=dict(arrowstyle="->", color='black'))
    plt.scatter(temp_lower, lower_bound_ratio, color='black', zorder=5)
    plt.annotate(f"({temp_lower}, {lower_bound_ratio:.2f})", 
                 (temp_lower, lower_bound_ratio), 
                 textcoords="offset points", xytext=(-100, -20), ha='center',
                 arrowprops=dict(arrowstyle="->", color='black'))
    plt.xlabel("Temperature / K")
    plt.ylabel("R_green/blue")
    plt.legend()
    plt.show()