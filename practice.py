# def my_function():
# print("Hello from a function")

# my_function()

# Write a function called power(base, exp) that returns an int value of base raises to the power of exp.

def power_func(base, exp):
    n = 1
    for i in range(1, base+1):
        n = exp * n
    return n


base = int(input("Enter base: "))
exp = int(input("Enter power: "))
result = power_func(base, exp)

print("The value of", base, "**", exp, " is", result)











# Method 2 -

def start_washing():
    energy_consumed = 0
    time_consumed = 0

    mode = input("Select mode (eco/normal): ")

    energy_consumed, time_consumed = fill_water(energy_consumed, time_consumed, mode)
    energy_consumed, time_consumed = heat_water(energy_consumed, time_consumed, mode)
    energy_consumed, time_consumed = wash_clothes(energy_consumed, time_consumed, mode)
    energy_consumed, time_consumed = drain_water(energy_consumed, time_consumed, mode)

    return energy_consumed, time_consumed


def fill_water(energy, time, eco_mode):
    if eco_mode == "eco":
        energy += 10
        time += 5
        print("Filling water (Eco mode) -> 5 minutes")
    else:
        energy += 15
        time += 7
        print("Filling water (Normal mode) -> 7 minutes")
    return energy, time


def heat_water(energy, time, eco_mode):
    if eco_mode == "eco":
        energy += 20
        time += 10
        print("Heating water (Eco mode) -> 10 minutes")
    else:
        energy += 30
        time += 15
        print("Heating water (Normal mode) -> 15 minutes")
    return energy, time


def wash_clothes(energy, time, eco_mode):
    if eco_mode == "eco":
        energy += 40
        time += 20
        print("Washing clothes (Eco mode) -> 20 minutes")
    else:
        energy += 50
        time += 25
        print("Washing clothes (Normal mode) -> 25 minutes")
    return energy, time


def drain_water(energy, time, eco_mode):
    energy += 5
    time += 5
    print("Draining water -> 5 minutes")
    return energy, time


total_energy, total_time = start_washing()
print("Total energy consumed:", total_energy)
print("Total time consumed:", total_time)
