import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import interp1d

A = 1.0                  # Pressure amplitude (Pa)
k = 1000.0               # Wave number (1/m)
r_bead = 5e-6            # Radius of microbead (m)
rho_0 = 1000.0           # Medium density (kg/m³)
c = 1500.0               # Speed of sound (m/s)
f1 = 1.0                 # Gor'kov compressibility contrast factor
f2 = 0.5                 # Gor'kov density contrast factor

x = np.linspace(-0.01, 0.01, 1000)

def gorkov_potential(x, A=A, k=k, r=r_bead, rho=rho_0, c=c, f1=f1, f2=f2):
    p_sq = A**2 * np.cos(k * x)**2
    v_sq = (A / (rho * c))**2 * np.sin(k * x)**2
    U = 0.5 * f1 * p_sq / (rho * c**2) - 0.75 * f2 * rho * v_sq
    return U

def acoustic_force_from_gorkov(x, U=None):
    if U is None:
        U = gorkov_potential(x)
    return -np.gradient(U, x)

p_fem = A * np.cos(k * x)  # This simulates a real pressure field
pressure_data = pd.DataFrame({'x': x, 'p': p_fem})
fem_csv_path = "/mnt/data/acoustic_pressure_fem.csv"
pressure_data.to_csv(fem_csv_path, index=False)

def load_pressure_field(filepath):
    data = pd.read_csv(filepath)
    x_vals, p_vals = data['x'].values, data['p'].values
    return interp1d(x_vals, p_vals, fill_value="extrapolate", bounds_error=False)

def acoustic_force_from_fem(x_vals, interp_p_func):
    dx = x_vals[1] - x_vals[0]
    p_vals = interp_p_func(x_vals)
    dpdx = np.gradient(p_vals, dx)
    return -dpdx

U = gorkov_potential(x)
F_gorkov = acoustic_force_from_gorkov(x, U)

interp_p = load_pressure_field(fem_csv_path)
F_fem = acoustic_force_from_fem(x, interp_p)

def apply_acoustic_force_to_particles(x_particles, method='gorkov', interp_func=None):
    if method == 'gorkov':
        return acoustic_force_from_gorkov(x_particles)
    elif method == 'fem' and interp_func is not None:
        return acoustic_force_from_fem(x_particles, interp_func)
    else:
        raise ValueError("Invalid method or missing interpolation function.")

np.random.seed(42)
x_particles = np.random.uniform(-0.01, 0.01, 20)
forces_on_beads_gorkov = apply_acoustic_force_to_particles(x_particles, method='gorkov')
forces_on_beads_fem = apply_acoustic_force_to_particles(x_particles, method='fem', interp_func=interp_p)

plt.figure(figsize=(14, 6))

plt.subplot(1, 3, 1)
plt.plot(x, U, label='Gor\'kov Potential')
plt.title("Gor'kov Potential")
plt.xlabel("x (m)")
plt.ylabel("U(x) (J)")
plt.grid(True)
plt.legend()

plt.subplot(1, 3, 2)
plt.plot(x, F_gorkov, 'r', label='Force from Gor\'kov')
plt.scatter(x_particles, forces_on_beads_gorkov, color='black', s=20, label='Beads (Gor\'kov)')
plt.title("Acoustic Force (Gor'kov)")
plt.xlabel("x (m)")
plt.ylabel("Force (N)")
plt.grid(True)
plt.legend()

plt.subplot(1, 3, 3)
plt.plot(x, F_fem, 'g', label='Force from FEM Pressure')
plt.scatter(x_particles, forces_on_beads_fem, color='blue', s=20, label='Beads (FEM)')
plt.title("Acoustic Force (FEM-based)")
plt.xlabel("x (m)")
plt.ylabel("Force (N)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

fem_csv_path
