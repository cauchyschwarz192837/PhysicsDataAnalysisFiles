import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os
from scipy.ndimage import center_of_mass

# Given frequencies
freq_list = [277.8, 107.6, 128.8, 141.2, 159.1, 185.9, 209.2, 231.2, 249.8, 265.3] 

# Extract positions from images
positions = []
image_directory = 'C:/Users/Admin/Downloads/newimages'
for image_filename in os.listdir(image_directory):
    image_path = os.path.join(image_directory, image_filename)
    LaserSpotImage = Image.open(image_path)
    LaserSpotData = np.array(LaserSpotImage)
    data = LaserSpotData[:, :, 0]  # Assuming we're using only the red channel
    threshold = 100
    bit_mask = np.where(data > threshold, data, 0)
    position = center_of_mass(bit_mask)

    # Scaling factor to convert from pixels to micrometers
    position = tuple((pos * 4.8) for pos in position)
    positions.append(position)

positions = np.array(positions)
print("Positions (in micrometers):", positions)

# Scatter plot of position (y vs x)
plt.scatter(positions[:, 1], positions[:, 0])
plt.title("Test")
plt.xlabel("x-position (micrometers)")
plt.ylabel("y-position (micrometers)")
plt.show()

# Frequency vs y-position linear fit
plt.scatter(freq_list, positions[:, 0])
coeffs_y, covmat_y = np.polyfit(freq_list, positions[:, 0], 1, cov=True)
slope_y = coeffs_y[0]
intercept_y = coeffs_y[1]
uncertainty_slope_y = np.sqrt(covmat_y[0, 0])
uncertainty_intercept_y = np.sqrt(covmat_y[1, 1])

# Print slope and intercept uncertainties for y
print(f"Slope (y) = {slope_y:.4f} ± {uncertainty_slope_y:.4f}")
print(f"Intercept (y) = {intercept_y:.4f} ± {uncertainty_intercept_y:.4f}")

# Plot with fit line for y vs frequency
plt.plot(np.unique(freq_list), np.poly1d(coeffs_y)(np.unique(freq_list)), color='red')
plt.title("y against frequency")
plt.text(0.1, 0.9, f'Slope: {slope_y:.4f}', transform=plt.gca().transAxes, color='red', fontsize=12)
plt.text(0.1, 0.85, f'Intercept: {intercept_y:.4f}', transform=plt.gca().transAxes, color='red', fontsize=12)
plt.xlabel("Frequency / Hz")
plt.ylabel("y-position / micrometers")
plt.show()

# Calculate expected uncertainty in the spot position (δy)
delta_f = 0.2  # Example uncertainty in frequency (Hz)
print(slope_y)
delta_y = slope_y * delta_f
print(f"Expected uncertainty in spot position (δy): {delta_y} micrometers")

# Calculate standard deviation of data with respect to the fit (σy)
N = len(freq_list)
residuals_y = positions[:, 0] - (-0.6533 * np.array(freq_list) + 2055)
sigma_y_squared = np.sum(residuals_y ** 2) / (N - 2)
sigma_y = np.sqrt(sigma_y_squared)
print(f"Standard deviation of data with respect to the fit (σy): {sigma_y:.4f} micrometers")

# Compare δy and σy
print("\nComparison of δy and σy:")
print(f"δy (uncertainty from frequency): {delta_y:.4f} micrometers")
print(f"σy (observed standard deviation): {sigma_y:.4f} micrometers")

if delta_y > sigma_y:
    print("The uncertainty in the slope comes from other sources beyond the uncertainty in the frequency.")
else:
    print("The observed fluctuations in position can be attributed to the uncertainty in frequency.")
