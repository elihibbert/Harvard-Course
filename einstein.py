#E=mc^2
#Ask the user for a mass in kilograms and output the equivelent energy

#Ask for mass
mass = int(input("What is the given mass in Kg of the object? "))

#Calculate energy (energy units m*kg m/s²)
energy = mass * 300000000 ** 2

#Display the energy, use comas for thousands
print(f"That is equivalent to {energy:,} Joules")

