import numpy as np
import matplotlib.pyplot as plt
from pysph.base.utils import get_particle_array
from pysph.solver.application import Application
from pysph.sph.scheme import SchemeChooser
from pysph.sph.heat.basic import HeatEquationWithSourceScheme

# Define Cubic Spline SPH Kernel
def cubic_spline_kernel(r, h):
    q = r / h
    sigma = 10 / (7 * np.pi * h ** 2)  # 2D normalization
    if q <= 1.0:
        return sigma * (1 - 1.5 * q ** 2 + 0.75 * q ** 3)
    elif q <= 2.0:
        return sigma * 0.25 * (2 - q) ** 3
    else:
        return 0.0

class AcoustofluidicsSPHKernelSim(Application):
    def create_particles(self):
        dx = dy = 0.001
        h = 1.2 * dx

        # Inlets
        xw, yw = np.mgrid[-0.02:0:dx, 0:0.01:dy]
        water = get_particle_array(name='water', x=xw.ravel(), y=yw.ravel(), h=h)
        water.T[:] = 298

        xi, yi = np.mgrid[-0.02:0:dx, -0.01:0:dy]
        iodix = get_particle_array(name='iodix', x=xi.ravel(), y=yi.ravel(), h=h)
        iodix.T[:] = 298

        # Microbeads
        xb = np.linspace(0.0, 0.02, 12)
        yb = np.zeros_like(xb)
        beads = get_particle_array(name='beads', x=xb, y=yb, h=h)
        beads.T[:] = 298

        return [water, iodix, beads]

    def create_scheme(self):
        return SchemeChooser(default='thermal', thermal=HeatEquationWithSourceScheme(
            fluids=['water', 'iodix'], solids=[], rho0=1000, k=0.6, cp=4180,
            alpha=1e-6, gamma=7.0, dim=2
        ))

    def configure_scheme(self):
        self.scheme.configure_solver(dt=1e-4, tf=0.5, adaptive_timestep=False)

    def apply_custom_physics(self, particles, t, dt):
        g = -9.81
        beta = 0.00021
        T_ref = 298
        A = 0.02
        k = 1000

        # Thermal buoyancy and acoustic field
        for name in ['water', 'iodix']:
            fluid = particles[name]
            for i in range(len(fluid.x)):
                # Buoyancy force
                delta_T = fluid.T[i] - T_ref
                fluid.av[i] += g * beta * delta_T

                # Local density estimation using kernel (for debug/learning)
                rho_est = 0
                for j in range(len(fluid.x)):
                    if i == j: continue
                    dx = fluid.x[i] - fluid.x[j]
                    dy = fluid.y[i] - fluid.y[j]
                    r = np.sqrt(dx**2 + dy**2)
                    rho_est += cubic_spline_kernel(r, fluid.h[i])
                fluid.rho[i] = rho_est * dx**2

        # Acoustic force on beads
        beads = particles['beads']
        for i in range(len(beads.x)):
            beads.au[i] += A * np.cos(k * beads.x[i])

    def post_step(self, solver):
        self.apply_custom_physics(self.particles, solver.t, solver.dt)

if __name__ == "__main__":
    app = AcoustofluidicsSPHKernelSim()
    app.run()

    # Plot final state
    def plot_all(particles):
        plt.figure(figsize=(10, 4))
        plt.scatter(particles['water'].x, particles['water'].y, c=particles['water'].T, cmap='coolwarm', s=3, label='Water')
        plt.scatter(particles['iodix'].x, particles['iodix'].y, c=particles['iodix'].T, cmap='coolwarm', s=3, label='Iodixanol')
        plt.scatter(particles['beads'].x, particles['beads'].y, color='red', s=12, label='Microbeads')
        plt.colorbar(label="Temperature (K)")
        plt.legend()
        plt.title("SPH Simulation with Thermal + Acoustic + Custom Kernel")
        plt.xlabel("x (m)")
        plt.ylabel("y (m)")
        plt.grid()
        plt.tight_layout()
        plt.show()

    plot_all(app.particles)
