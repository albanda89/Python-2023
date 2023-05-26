def start_washing():
    energy = 0
    time = 0

    select_mode = input("Select Mode - eco/normal: ")

    
    if select_mode == "eco":
        fill_water(energy, time, eco_mode)        
    
    else :
        fill_water(energy, time, eco_mode)

def fill_water (energy,time,eco_mode):
    energy += 10
    time += 5
    print("Filling water (Eco mode) -> 5 minutes")
    return energy, time
    
def heat_water(energy, time, eco_mode):
    energy += 20
    time += 10
    print("Heating water (Eco mode) -> 10 minutes")
    return energy, time

def wash_clothes (energy, time, eco_mode):
    energy += 40
    time += 20
    print("Washing clothes (Eco mode) -> 20 minutes")
    return energy, time

def drain_water (energy, time, eco_mode):
    energy += 5
    time += 5
    print("Draining water -> 5 minutes")
    return energy, time

start_washing()