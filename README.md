#2nd UK Microfluidics System Conference Particle-Fluid-Interactions-in-Acoustically-Driven-Convection-Systems-A-Study-on-Microbead-Dynamics

🧪 Acoustofluidics with SPH and Acoustic Force Modeling
This repository presents a high-fidelity simulation framework that couples Smoothed Particle Hydrodynamics (SPH) with analytical and interpolated acoustic forces to model microbead dynamics in acoustically levitated and thermally driven environments. The application targets advancements in droplet microfluidics, biological analysis, and zero-gravity aerospace research.

📌 Features
✅ Gor'kov Potential-based Acoustic Force

✅ FEM-style pressure field interpolation

✅ 2D SPH simulation with PySPH

✅ Thermal convection modeling

✅ Microbead acoustic levitation and motion

✅ Custom SPH kernel (Cubic Spline) for visualization & density estimation

🧬 Methodology:

Acoustic Field Modeling:
Gor'kov potential computed analytically.

FEM-style simulated pressure field exported to CSV.

Gradient of pressure used to compute acoustic force.

SPH Simulation:

Thermal convection handled via *HeatEquationWithSourceScheme*.

Fluids:
Water and Iodixanol (biological medium).

Particles: 
Microbeads subject to gravity, buoyancy, and acoustic forces.

Microbeads Dynamics:
Influenced by both Gor'kov and interpolated FEM-based acoustic forces.

Coupled to local temperature field and buoyancy using Boussinesq approximation.

📂 File Structure:
├── acoustic_force_module.py         # Gor'kov and FEM acoustic force models

├── acoustic_pressure_fem.csv        # Simulated FEM-like acoustic pressure field

├── acoustofluidics_sph_sim.py       # Main PySPH simulation script

├── plots/                           # Plots of simulation results

├── README.md                        # This file

🚀 How to Run:

1. Install Dependencies:
*pip install pysph numpy scipy matplotlib pandas*

2. Run the Acoustic Force Modeling Script:
*python acoustic_force_module.py*

3. Run the SPH Simulation:
*python acoustofluidics_sph_sim.py*

📊 Visualization:

At the end of the simulation, a visual plot is generated showing:
Temperature distribution in fluids.
Bead positions.
Field-driven convection patterns.

📖 Citation:

If you use this code in your research, please cite:





