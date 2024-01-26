name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 # lbs
eye = 'Blue'
teeth = 'White'
hair = 'Brown'
height_cm = 74 * 2.54
weight_kg = round(180 * 0.453592)

print(f"Let's talk about {name}. ")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eye} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")


print(f"He's {height_cm} cm tall.")
print(f"He's {weight_kg} kg heavy.")

a = 52 / 6
print(a)
