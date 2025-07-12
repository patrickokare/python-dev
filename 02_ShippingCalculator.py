# ## Project II: Shipping Calculator

# Build a program to calculate and compare shipping costs between different shipping methods based on package weight.

# ### Project Requirements

# - Calculate costs for three shipping methods:
#     - Ground Shipping (flat charge + weight-based rate)
#     - Ground Premium (fixed rate)
#     - Drone Shipping (no flat charge, 3x weight rate)

# Pricing structure:

# | Weight | Ground (per lb) | Drone (per lb) |
# | --- | --- | --- |
# | ≤ 2 lb | $1.50 | $4.50 |
# | 2-6 lb | $3.00 | $9.00 |
# | 6-10 lb | $4.00 | $12.00 |
# | >10 lb | $4.75 | $14.25 |

# Ground Premium: Flat $125.00


# Constants for flat charges
GROUND_FLAT = 20.00
PREMIUM_FLAT = 125.00

def calculate_shipping(weight):
    # Calculate ground shipping
    if weight <= 2:
        ground = weight * 1.50 + GROUND_FLAT
    elif weight <= 6:
        ground = weight * 3.00 + GROUND_FLAT
    elif weight <= 10:
        ground = weight * 4.00 + GROUND_FLAT
    else:
        ground = weight * 4.75 + GROUND_FLAT
        
    # Calculate drone shipping (3x ground rates)
    if weight <= 2:
        drone = weight * 4.50
    elif weight <= 6:
        drone = weight * 9.00
    elif weight <= 10:
        drone = weight * 12.00
    else:
        drone = weight * 14.25
        
    # Find cheapest method
    costs = {
        "Ground": ground,
        "Premium": PREMIUM_FLAT,
        "Drone": drone
    }
    cheapest = min(costs, key=costs.get)
    
    return f"Best shipping method: {cheapest} (${costs[cheapest]:.2f})"

# Example usage
print(calculate_shipping(4.8))  # Returns best shipping method and costethod: Drone Shipping, Cost:', drone_cost)