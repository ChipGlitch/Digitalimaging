import matplotlib.pyplot as plt
import numpy as np

gs_values = np.array([5, 3, 5, 4, 4, 4, 10, 4, 5])

# Grayscale ranges
old_min, old_max = np.min(gs_values), np.max(gs_values)
new_min, new_max = 2, 40


# Mapping function
def histogram_stretching(old_value, minimum_old, maximum_old, minimum_new, maximum_new):
    slope1 = (maximum_new - minimum_new) / (maximum_old - minimum_old)
    return slope1 * (old_value - minimum_old) + minimum_new


# Histogram Stretching
stretched_values = histogram_stretching(gs_values, old_min, old_max, new_min, new_max)

# Mapping function equation
slope = (new_max - new_min) / (old_max - old_min)
intercept = new_min - slope * old_min
mapping_function_equation = f"gs_new = {slope} * (gs_old - {old_min}) + {new_min}"

# (a) Original grayscale histogram
plt.figure(figsize=(8, 5))
plt.hist(gs_values, bins=range(old_min, old_max + 2), color='gray', rwidth=0.8)
plt.title('Original Grayscale Histogram')
plt.xlabel('Grayscale Value')
plt.ylabel('Frequency')
plt.xticks(range(old_min, old_max + 1))
plt.show()

# (b) Mapping diagram
old_range = np.linspace(old_min, old_max, 100)
new_range = histogram_stretching(old_range, old_min, old_max, new_min, new_max)

plt.figure(figsize=(8, 5))
plt.plot(old_range, new_range, label='Linear Mapping Function', color='lime')
plt.scatter(gs_values, stretched_values, color='purple', label='Mapped Original Values')
plt.title('Mapping Diagram - Original to New Grayscale Value')
plt.xlabel('Original Value')
plt.ylabel('New Value')
plt.grid(axis='x', alpha=.75)
plt.show()

# (d) Histogram stretching
plt.figure(figsize=(8, 5))
plt.hist(stretched_values, bins=range(int(new_min), int(new_max) + 3), color='gray', rwidth=1)
plt.title('New Grayscale After Stretching')
plt.xlabel('Grayscale Level')
plt.ylabel('Frequency')
plt.xticks(range(int(new_min), int(new_max) + 1, 4))
plt.tight_layout()
plt.show()
