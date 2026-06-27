inventory={"Pen":110,"NoteBook":50}

if"NoteBook" in inventory:
    inventory["NoteBook"] -= 1
    print("BoteBook Sold")

else:
    print("BoteBook Not Found")

if"Bag" in inventory:
    inventory["Bag"] -= 1
    print("Bag Sold")
else:
    print("Bag Not Found")

print("Updated Inventory:")
print(inventory)