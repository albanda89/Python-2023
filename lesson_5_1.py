def start_washing():
    energy_consumed = 0
    time_consumed = 0

    select_mode = input("Select Mode - eco/normal: ")

    
    if select_mode == "eco":
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
    
    else :
        def fill_water (energy,time,normal_mode):    
            energy += 15
            time += 7
        print("Filling water (Normal mode) -> 7 minutes")
        return energy, time
    
        def heat_water (energy, time, normal_mode):
             energy += 30
             time += 15
        print("Heating water (Normal mode) -> 15 minutes")
        return energy, time
        
        def wash_clothes(energy, time, normal_mode):
            energy += 50
            time += 25
        print("Washing clothes (Normal mode) -> 25 minutes")
        return energy, time