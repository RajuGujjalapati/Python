houses=["raju's house","kenny's house","kyle's house","mamatha's house","checking house"]
def deliver_house(houses):
    if len(houses)==1:
        house=houses[0]
        print("delivering food to:",house)
    else:
        mid=len(houses)//2
        fir_half=houses[:mid]
        sec_half=houses[mid:]
        deliver_house(fir_half)
        deliver_house(sec_half)
print(deliver_house(houses))
