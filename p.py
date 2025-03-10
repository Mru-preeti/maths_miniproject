import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm  # For drawing a normal distribution curve

# Function to roll two dice 10 times and record sums
def roll_dice_10_times():
    sums = [random.randint(1, 6) + random.randint(1, 6) for _ in range(10)]
    return sums

# Function to perform multiple trials and count occurrences of sum > 8
def perform_trials(num_trials):
    count_list = []
    for _ in range(num_trials):
        sums = roll_dice_10_times()
        count_greater_8 = sum(1 for s in sums if s > 8)  # Count sums > 8
        count_list.append(count_greater_8)
    return count_list

# Function to plot the frequency distribution with a smooth curve
def plot_frequency_curve(data, title, xlabel, ylabel):
    plt.figure(figsize=(8, 6))
    
    # Histogram
    plt.hist(data, bins=range(min(data), max(data) + 2), edgecolor='black', alpha=0.7, density=True)
    
    # Curve
    mean, std_dev = np.mean(data), np.std(data)
    x = np.linspace(min(data), max(data), 100)
    y = norm.pdf(x, mean, std_dev)
    plt.plot(x, y, color='red', label='Normal Distribution Curve')
    
    # Display mean and standard deviation
    plt.axvline(mean, color='blue', linestyle='--', label=f'Mean: {mean:.2f}')
    plt.axvline(mean + std_dev, color='green', linestyle='--', label=f'SD: {std_dev:.2f}')
    plt.axvline(mean - std_dev, color='green', linestyle='--')
    
    # Titles and labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()

    # Print mean and standard deviation
    print(f"Mean: {mean:.2f}, Standard Deviation: {std_dev:.2f}")

# Step 1: Roll dice 10 times and analyze sums
sums_10 = roll_dice_10_times()
print(f"Sums of 10 dice rolls: {sums_10}")

# Plot frequency of sums for a single trial
plot_frequency_curve(sums_10, "Frequency of Sums in 10 Rolls", "Sum", "Frequency")

# Step 2: Perform increasing number of trials
trial_counts = [10, 20, 30, 40, 100, 200, 1000]

for trials in trial_counts:
    count_data = perform_trials(trials)
    print(f"Number of times sum > 8 in {trials} trials: {count_data}")
    plot_frequency_curve(count_data, f"Count of Sum > 8 in {trials} Trials", "Count", "Frequency")

print("\nObservation: As the number of trials increases, the distribution appears to approach a normal distribution.")
