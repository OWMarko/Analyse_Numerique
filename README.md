# Resources for Numerical Analysis

> **Personal Sandbox & Knowledge Base**
> **Language:** Python (NumPy, SciPy, Matplotlib)

This repository serves as a collection of **reference implementations**, snippets, and educational scripts related to Numerical Analysis. It acts as a digital notebook where I test algorithms, visualize numerical schemes, and verify theoretical concepts before applying them in more complex C++/HPC projects.

### Repository Content

The scripts and notebooks cover various standard topics in applied mathematics:

#### ODE Solvers & Schemes
Implementation and stability testing of time-stepping methods:
* **Basic Schemes :** Forward/Backward Euler, Crank-Nicolson
* **Runge-Kutta :** RK4 implementations
* **Stability Analysis :** Scripts to plot stability regions

#### Numerical Integration (Quadrature)
* Trapezoidal rule & Simpson's method
* Gaussian quadrature implementations
* Error estimation analysis

#### Root Finding & Optimization
* Newton-Raphson method (convergence tests)
* Bisection and Secant methods
* Gradient Descent basic implementation

--

### Usage
Most files are standalone scripts or Jupyter Notebooks meant for educational exploration.

```bash
# Clone the repository
git clone [https://github.com/OWMarko/Resources_for_Numerical_Analysis.git](https://github.com/OWMarko/Resources_for_Numerical_Analysis.git)

# Run a specific script
python script_name.py
```

These codes are written for educational purposes to illustrate mathematical concepts. They prioritize readability and theoretical clarity over performance optimization.
