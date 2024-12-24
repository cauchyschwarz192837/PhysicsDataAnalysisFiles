import numpy as np
from BaslerRAW import BaslerRAW 
from PIL import Image
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # Load RAW images for each filter (ON and OFF)
    red_on = BaslerRAW('redv01.raw')
    red_off = BaslerRAW('redv02.raw')
    green_on = BaslerRAW('greenv01.raw')
    green_off = BaslerRAW('greenv02.raw')
    blue_on = BaslerRAW('bluev01.raw')
    blue_off = BaslerRAW('bluev02.raw')

    # Convert to a Pillow Image object
    plt.imshow(green_off)
    plt.title("(c)")
    plt.axis('on')
    plt.show()

    # Exposure times (replace with your actual exposure times)
    exposure_time_on = 0.01  # Example exposure time in seconds
    exposure_time_off = 0.01

    # Calculate average intensities for ON and OFF images
    red_avg_on = np.sum(red_on[:, :, 0]) / (5000)
    red_avg_off = np.sum(red_off[:, :, 0]) / (5000)

    green_avg_on = np.sum(green_on[:, :, 1]) / (20000)
    green_avg_off = np.sum(green_off[:, :, 1]) / (20000)

    blue_avg_on = np.sum(blue_on[:, :, 2]) / (70000)
    blue_avg_off = np.sum(blue_off[:, :, 2]) / (70000)

    # Subtract background signal to get corrected intensities
    I_red = red_avg_on - red_avg_off
    I_green = green_avg_on - green_avg_off
    I_blue = blue_avg_on - blue_avg_off

    # Calculate intensity ratios
    R_red_green = I_red / I_green
    R_green_blue = I_green / I_blue
    R_blue_red = I_blue / I_red

    print(f"Red Intensity: {I_red}")
    print(f"Green Intensity: {I_green}")
    print(f"Blue Intensity: {I_blue}")

    print(f"Intensity Ratios:\nRed/Green: {R_red_green}, Green/Blue: {R_green_blue}, Blue/Red: {R_blue_red}")

