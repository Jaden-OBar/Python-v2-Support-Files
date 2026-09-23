#Items acquired
v_1 = "Rock"
v_2 = "Pogo Stick"
v_3 = "Wand"
#What level items are acquired
v_4 = "level 1"
v_5 = "level 2"
v_6 = "level 3"

print(f"You can get a {v_1} at {v_4}")
print(f"You can get a {v_2} at {v_4}")
print(f"You can get a {v_3} at {v_5}")
print(f"You can get a {v_2} at {v_5}")
print(f"You can get a {v_3} at {v_6}")
print(f"You can get a {v_1} at {v_6}")
print(f"You can get a {v_2} at {v_6}")

#What the video shows to do

items = ['Wand', 'Rock', 'Pogo Stick']
levels = [1, 2, 3]
for level in levels:
    for item in items:
        if level == 2 and item == 'Rock':
            continue
        else:
            print(f"You can get a {item} at level {level}.")