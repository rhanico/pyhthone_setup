def hello():
    print("Hello World")

hello()

def pack(item1, item2, item3):
    return [item1, item2, item3]

def eat_lunch(lunchbox):
    if not lunchbox:
        print("My lunchbox is empty!")
    else:
        print("First I eat", lunchbox[0])
        for item in lunchbox[1:]:
            print("Next I eat", item)

packed_items = pack("Banana", "Apple", "Nuts")
print("Packed items:", packed_items)


eat_lunch([])

lunch_items = ["Rice", "Burger", "Fish"]
eat_lunch(lunch_items)
