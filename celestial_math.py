"""
CelMath 101 - Core Python Implementation

This script provides basic implementations of the core mathematical principles of Celestial Mathematics,
including recursive energy dynamics, fractal spacetime curvature, and AI-based self-evolving functions.
"""

import numpy as np
import matplotlib.pyplot as plt

# 1. Recursive Energy Dynamics
def recursive_energy(x, w):
    return w * np.log(x) + (1 - w) * (-np.log(x))

# Generate energy dynamics curve
x_values = np.linspace(0.1, 10, 400)
w_values = [0.2, 0.5, 0.8]
plt.figure(figsize=(8, 5))

for w in w_values:
    plt.plot(x_values, recursive_energy(x_values, w), label=f'w={w}')

plt.title("Recursive Energy Dynamics")
plt.xlabel("x")
plt.ylabel("E_total")
plt.legend()
plt.grid()
plt.show()


# 2. Fractal Symmetry in Space-Time
def fractal_spacetime(n, d):
    return sum(1 / ((1 + i) ** d) for i in range(n))

# Compute and display fractal spacetime behavior
n_values = np.arange(1, 50)
curvature_values = [fractal_spacetime(n, 2) for n in n_values]

plt.figure(figsize=(8, 5))
plt.plot(n_values, curvature_values, label="Fractal Curvature")
plt.xlabel("Iterations (n)")
plt.ylabel("Curvature Sum")
plt.title("Fractal Symmetry in Space-Time")
plt.legend()
plt.grid()
plt.show()


# 3. Quantum Wavefunction Expansion
def quantum_wavefunction(x, t, n_max=5):
    psi_0 = np.exp(-1j * t)
    sum_term = sum(np.sin(n * np.pi * x) for n in range(1, n_max + 1))
    return psi_0 + sum_term

# Visualization of wavefunction
x_vals = np.linspace(0, 1, 100)
t_vals = np.linspace(0, 10, 100)
wave_vals = np.real([quantum_wavefunction(x, 1) for x in x_vals])

plt.figure(figsize=(8, 5))
plt.plot(x_vals, wave_vals, label="Quantum Wavefunction")
plt.xlabel("x")
plt.ylabel("Ψ(x,t)")
plt.title("Quantum Wavefunction Expansion")
plt.legend()
plt.grid()
plt.show()


# 4. Self-Evolving AI Algorithm (Basic Recursive Learning)
def recursive_ai_learning(initial_value, iterations=10, learning_rate=0.1):
    value = initial_value
    history = [value]
    
    for _ in range(iterations):
        value += learning_rate * (np.sin(value) - value / 10)  # Recursively adjusting learning steps
        history.append(value)
    
    return history

# Simulating AI learning behavior
iterations = 50
ai_values = recursive_ai_learning(1.0, iterations)

plt.figure(figsize=(8, 5))
plt.plot(range(iterations + 1), ai_values, label="Recursive AI Learning")
plt.xlabel("Iterations")
plt.ylabel("AI Model Output")
plt.title("Fractal AI Learning Model")
plt.legend()
plt.grid()
plt.show()
