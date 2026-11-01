import random

# --- Configuration ---
# These values are illustrative and simplified for demonstration purposes.
# In a real scenario, these would be detailed financial calculations.

# On-premise (Traditional IT Infrastructure)
# Represents the fixed monthly operational cost of owning and maintaining servers,
# storage, networking, power, cooling, and IT staff.
# This cost is incurred regardless of actual usage fluctuations.
ON_PREM_FIXED_MONTHLY_COST = 750 # Example: $750/month for a small setup

# Cloud Computing (Pay-as-you-go Model)
# Represents the variable costs charged by cloud providers based on actual resource consumption.
CLOUD_HOURLY_SERVER_RATE = 0.05 # Example: $0.05 per hour for a virtual server instance
CLOUD_GB_STORAGE_RATE = 0.02    # Example: $0.02 per GB per month for storage

# Simulation parameters
SIMULATION_MONTHS = 6 # Simulate costs over 6 months to show trends
MAX_HOURS_PER_MONTH = 720 # Approx. 30 days * 24 hours
MAX_STORAGE_GB = 500      # Max storage capacity in GB

def calculate_cloud_cost(usage_hours_monthly, storage_gb_monthly):
    """
    Calculates the total monthly cloud cost based on simulated usage.
    This demonstrates the 'pay-as-you-go' model where costs scale with demand.
    """
    server_cost = CLOUD_HOURLY_SERVER_RATE * usage_hours_monthly
    storage_cost = CLOUD_GB_STORAGE_RATE * storage_gb_monthly
    return server_cost + storage_cost

print("--- Cloud vs. On-Premise Cost Simulation ---")
print("This example illustrates how cloud computing can reduce IT infrastructure costs by offering a 'pay-as-you-go' model, contrasting it with traditional fixed on-premise expenses.")
print("\n--- Assumptions ---")
print(f"On-Premise: Fixed monthly operational cost of ${ON_PREM_FIXED_MONTHLY_COST:.2f}, regardless of usage.")
print(f"Cloud: Variable cost based on actual usage (Server: ${CLOUD_HOURLY_SERVER_RATE}/hour, Storage: ${CLOUD_GB_STORAGE_RATE}/GB/month).")
print("-" * 60)

total_on_prem_cost = 0
total_cloud_cost = 0

print(f"Fixed On-Premise Monthly Cost: ${ON_PREM_FIXED_MONTHLY_COST:.2f}")
print("-" * 60)

for month in range(1, SIMULATION_MONTHS + 1):
    # Simulate fluctuating usage for cloud resources.
    # This highlights cloud's flexibility and scalability: you only pay for what you use.
    # Usage can be low (e.g., development environment) or high (e.g., peak traffic).
    usage_hours = random.randint(100, MAX_HOURS_PER_MONTH) # Server uptime (e.g., VM running hours)
    storage_gb = random.randint(50, MAX_STORAGE_GB)       # Data stored (e.g., database, files)

    # On-premise cost remains fixed, irrespective of actual usage.
    # This demonstrates the burden of over-provisioning or under-utilization with traditional IT.
    current_on_prem_cost = ON_PREM_FIXED_MONTHLY_COST
    total_on_prem_cost += current_on_prem_cost

    # Cloud cost varies directly with the simulated usage for the month.
    current_cloud_cost = calculate_cloud_cost(usage_hours, storage_gb)
    total_cloud_cost += current_cloud_cost

    print(f"\n--- Month {month} ---")
    print(f"  Simulated Usage: {usage_hours} server hours, {storage_gb} GB storage")
    print(f"  On-Premise Cost: ${current_on_prem_cost:.2f} (fixed, regardless of usage)") # Demonstrates fixed cost
    print(f"  Cloud Cost:      ${current_cloud_cost:.2f} (variable, pay-as-you-go)")      # Demonstrates variable cost
    if current_cloud_cost < current_on_prem_cost:
        print("  -> Cloud is cheaper this month due to lower/efficient usage!")
    else:
        print("  -> On-Premise is cheaper this month (or cloud usage was high enough to exceed its flexibility benefit).")

print("\n" + "=" * 60)
print(f"Total On-Premise Cost over {SIMULATION_MONTHS} months: ${total_on_prem_cost:.2f}")
print(f"Total Cloud Cost over {SIMULATION_MONTHS} months:      ${total_cloud_cost:.2f}")
print("=" * 60)

if total_cloud_cost < total_on_prem_cost:
    print(f"\nConclusion: In this simulation, Cloud Computing resulted in savings of ${total_on_prem_cost - total_cloud_cost:.2f} over {SIMULATION_MONTHS} months.")
    print("This highlights how cloud's pay-as-you-go model can be more cost-effective, especially with fluctuating or lower usage, by eliminating large upfront capital expenditures and reducing operational overhead.")
else:
    print(f"\nConclusion: In this simulation, On-Premise was cheaper by ${total_cloud_cost - total_on_prem_cost:.2f} over {SIMULATION_MONTHS} months.")
    print("While cloud offers flexibility and no upfront CAPEX, consistently very high usage might sometimes make on-premise appear cheaper in a simplified model. However, real cloud benefits also include managed services, global reach, and reduced operational burden which are not simulated here.")
