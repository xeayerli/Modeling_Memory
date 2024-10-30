import numpy as np
import matplotlib.pyplot as plt

# Parameters
total_steps = 100 #simualtion steps
spaced_interval = 10 #the revisiting interval for spaced learning
decay_rate = 0.1 #the rate of forgetting per step

# Initialize the retention level (as float)
spaced_fact_retention = 1.0  # Starting retention level
non_spaced_fact_retention = 1.0  # Starting retention level

# Create empty lists to track retention over time for plotting
spaced_retention_history = []
non_spaced_retention_history = []  # Correct list name here

for step in range(total_steps):
    # Apply the rate of decay
    spaced_fact_retention -= decay_rate
    non_spaced_fact_retention -= decay_rate

    # Reinforcement of the spaced fact at specific intervals
    if step % spaced_interval == 0:
        spaced_fact_retention = min(spaced_fact_retention +0.5, 1.0) # reset to max retention if revisited

    # Ensure the retention cannot be below zero
    spaced_fact_retention = max(spaced_fact_retention, 0)
    non_spaced_fact_retention = max(non_spaced_fact_retention, 0)

    # Track history
    spaced_retention_history.append(spaced_fact_retention)
    non_spaced_retention_history.append(non_spaced_fact_retention)

# Create plot
plt.plot(spaced_retention_history, label="Spaced Fact")
plt.plot(non_spaced_retention_history, label="Non-Spaced Fact")
plt.xlabel("Time Steps")
plt.ylabel("Retention Level")
plt.title("Spaced vs. Non-Spaced Fact Retention Over Time")
plt.legend()
plt.show()

    