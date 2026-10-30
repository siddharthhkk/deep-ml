import math
import numpy as np
PI = 3.14159

def power_grid_forecast(x):
	# 1) Subtract the daily fluctuation (10 * sin(2π * i / 10)) from each data point.
	# 2) Perform linear regression on the detrended data.
	# 3) Predict day 15's base consumption.
	# 4) Add the day 15 fluctuation back.
	# 5) Round, then add a 5% safety margin (rounded up).
	# 6) Return the final integer.
    x = np.array(x, dtype=float)
    n = len(x)
    days = np.arange(1, n + 1)
    fluctuations = 10 * np.sin(2 * PI * days / 10)
    de_x = x - fluctuations
    X = np.column_stack((np.ones(n), days))
    theta = np.linalg.inv(X.T @ X) @ X.T @ de_x
    b, w = theta[0], theta[1]
    day_15 = w * 15 + b
    f15 = day_15 + (10 * math.sin(2 * PI * 15 / 10))
    ans = math.ceil(round(f15) * 1.05)
    return int(ans)