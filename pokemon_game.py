# taking input of pokemon's power uisng list comphrehension
pok_power = [int(x) for x in input("Enter your pokemon numbers :-").split() ]
min_p = min(pok_power)
max_p = max(pok_power)

# sorting the powers list
pok_power.sort()
i = 0 
c = 0
a = len(pok_power)-1
linear_data = []

for value in pok_power :
    linear_1 = max_p - a    
    linear = max_p - i
    linear_data.append(linear)

    if i == 0:
        print(min_p,min_p)
    
    if linear_1 == max_p:
        print(min_p,max_p)
        
    for y in linear_data:
        if y == value and c != len(pok_power)-2 :
            print(min_p,y)
            c += 1
    i+=1
    a-=1