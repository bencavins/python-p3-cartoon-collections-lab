def roll_call_dwarves(dwarves):
    num = 1
    for dwarf in dwarves:
        # print(str(num) + ".", dwarf)
        print(f"{num}. {dwarf}")
        num += 1  # num = num + 1

def summon_captain_planet(calls):
    result = []
    for call in calls:
        new_call = call.capitalize() + "!"
        result.append(new_call)
    return result

def long_planeteer_calls():
    pass

def find_the_cheese():
    pass


print(summon_captain_planet(["carrot", "cucumber", "pepper"]))