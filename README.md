==================================================
#2ND UK MICROFLUIDICS SYSTEM CONFERENCE
==================================================
Title: Particle-Fluid Interactions in Acoustically Driven Convection Systems – A Study on Microbead Dynamics


==================================================
🧪 OVERVIEW
==================================================

This repository presents a high-fidelity simulation framework that couples
Smoothed Particle Hydrodynamics (SPH) with analytical and interpolated acoustic
forces to model microbead dynamics in acoustically levitated and thermally
driven environments.

The application targets advancements in:
- Droplet microfluidics
- Biological analysis
- Zero-gravity aerospace research


==================================================
📌 FEATURES
==================================================

- Gor'kov Potential-based Acoustic Force
- FEM-style pressure field interpolation
- 2D SPH simulation with PySPH
- Thermal convection modeling
- Microbead acoustic levitation and motion
- Custom SPH kernel (Cubic Spline) for visualization & density estimation


==================================================
🧬 METHODOLOGY
==================================================

Acoustic Field Modeling:
- Gor'kov potential computed analytically
- FEM-style simulated pressure field exported to CSV
- Gradient of pressure used to compute acoustic force

SPH Simulation:
- Thermal convection handled via HeatEquationWithSourceScheme

Fluids:
- Water and Iodixanol (biological medium)

Particles:
- Microbeads subject to gravity, buoyancy, and acoustic forces

Microbeads Dynamics:
- Influenced by both Gor'kov and interpolated FEM-based acoustic forces
- Coupled to local temperature field and buoyancy using Boussinesq approximation


==================================================
📂 FILE STRUCTURE
==================================================

acoustic_force_module.py        - Gor'kov and FEM acoustic force models  
acoustic_pressure_fem.csv       - Simulated FEM-like acoustic pressure field  
acoustofluidics_sph_sim.py      - Main PySPH simulation script  
plots/                          - Plots of simulation results  
README.md                       - This file


==================================================
🚀 HOW TO RUN
==================================================

1. Install Dependencies:
   pip install pysph numpy scipy matplotlib pandas

2. Run the Acoustic Force Modeling Script:
   python acoustic_force_module.py

3. Run the SPH Simulation:
   python acoustofluidics_sph_sim.py


==================================================
📊 VISUALIZATION
==================================================

At the end of the simulation, a visual plot is generated showing:
- Temperature distribution in fluids
- Microbead positions
- Field-driven convection patterns


==================================================
📖 CITATION
==================================================

If you use this code in your research, please cite:

@article{Mahapatra2025,
  title     = {Particle-Fluid Interactions in Acoustically Driven Convection Systems: A Study on Microbead Dynamics},
  author    = {Anjan Mahapatra and Muthu Shravan Sundaram},
  journal   = {2nd UK Microfluidics Conference},
  year      = {2025},
  address   = {Leeds, United Kingdom},
  note      = {Conference Paper}
 







