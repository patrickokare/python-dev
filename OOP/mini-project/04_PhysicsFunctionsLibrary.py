# ## Project IV: Physics Functions Library

# Create a comprehensive physics calculation library with functions for temperature conversion, force, energy, and work calculations.

# ### Temperature Conversion Functions

# - Fahrenheit to Celsius (`f_to_c`)
#     - Input: `f_temp` (Fahrenheit)
#     - Formula: (°F - 32) × 5/9
#     - Example: `f_to_c(100)` → 37.78°C
# - Celsius to Fahrenheit (`c_to_f`)
#     - Input: `c_temp` (Celsius)
#     - Formula: (°C × 9/5) + 32
#     - Example: `c_to_f(0)` → 32°F

# ### Force and Energy Calculations

# - Force Calculator (`get_force`)
#     - Inputs: `mass`, `acceleration`
#     - Formula: F = ma
#     - Units: Newtons (N)
# - Energy Calculator (`get_energy`)
#     - Inputs: `mass`, `c` (speed of light, default 3×10⁸)
#     - Formula: E = mc²
#     - Units: Joules (J)

# ### Work Calculation

# - Work Calculator (`get_work`)
#     - Inputs: `mass`, `acceleration`, `distance`
#     - Formula: W = F × d (where F = ma)
#     - Units: Joules (J)


# Constants
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Temperature conversion functions
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp

def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    return f_temp

# Force calculation
def get_force(mass, acceleration):
    return mass * acceleration

# Energy calculation with E = mc²
def get_energy(mass, c=3*10**8):
    return mass * c**2

# Work calculation
def get_work(mass, acceleration, distance):
    return get_force(mass, acceleration) * distance

# Example calculations
train_force = get_force(train_mass, train_acceleration)
print('The GE train supplies', train_force, 'Newtons of force.')

bomb_energy = get_energy(bomb_mass)
print('A 1kg bomb supplies', bomb_energy, 'Joules.')

train_work = get_work(train_mass, train_acceleration, train_distance)
print('The GE train does', train_work, 'Joules of work over', train_distance, 'meters.')
    