# Physics-Simulation

This project implements a 2D cloth simulation in Python as part of the CAS 737 Computer Animation (Winter 2024) course. The simulation models a cloth as a grid of particles connected by springs, and includes gravity, spring forces, damping, and basic user interaction to manipulate the cloth in real-time.

---

## Features

1. **Particle-Spring System**  
   - Cloth is represented by a grid of particles connected by springs.  
   - Each spring exerts forces on the two particles it connects.

2. **Gravity (Fake Gravity for a “Flowy” Effect)**  
   - A small constant force in the negative Y-direction simulates a gentle pull.

3. **Hooke’s Law & Damping**  
   - Spring force is computed using Hooke’s Law.  
   - Damping is implemented to stabilize the simulation and prevent excessive oscillations.

4. **Euler Method**  
   - Particle positions and velocities are updated over discrete time steps using the Euler integration method.

5. **Real-Time Interaction**  
   - The user can click and drag on particles within the cloth to interact with the simulation.

---

## Implementation

**Files & Responsibilities:**
- **`ui.py`**  
  Implements the user interface and visualization of the cloth. Handles mouse interactions.
  
- **`cloth.py`**  
  Defines the Cloth class, initializing a grid of particles and springs. Iterates through each time step to apply forces and update particle positions.

- **`spring.py`**  
  Defines the Spring class. Each spring maintains references to the two particles it connects and calculates forces based on Hooke’s law.

- **`particle.py`**  
  Defines each particle (grid point) in the cloth, storing position, velocity, acceleration, and force.

---

## Usage

1. **Run the Simulation**  
   ```bash
   python ui.py
   ```
2. **Interact with the Cloth**  
   - Click and drag on any portion of the cloth to manipulate it.  
   - Observe the cloth reacting to the pull and releasing it to return to a stable configuration.

3. **Tuning Simulation Parameters**  
   - Open `cloth.py`, `spring.py`, or `particle.py` to adjust constants like gravity, spring stiffness (`k`), damping (`c`), and time step (`deltaTime`).  
   - Increasing damping or capping forces can reduce oscillations or “explosions” in the simulation.


 

