cart = ["apples","bananas","cherries"]
print(cart)
cart.append("donuts")
cart.append("milk")
cart.append("eggs")
print(cart)

cart.remove("cherries")
cart.pop(1)
print(cart)
cart.pop()
print(cart)
cart.append("bananas")
cart.append("bananas")
print(cart)
cart.sort()
print(cart)

fruit=cart[0:3]
print(fruit)

count=cart.count("bananas")
print(count)

squares=[]
for i in range(1,10):
    squares.append(i*i)
print(squares)

b_items = [item for item in cart if item.startswith("b")]
print(b_items)

inventory=[0]*10
inventory[4]=100
print(inventory)

book_genres={"romance"}
book_genres.add("science fiction")
book_genres.add("mystery")
print(book_genres)
aset=set()

lst=[1,1,2,2,3,3,4,4,5,5]
unique=set(lst)
print(unique)

fav_snacks={"Kathleen":"pizza", "Steve":"chips","Patrick":"nutella"}

steve=fav_snacks["Steve"]
print(steve)

for key in fav_snacks:
    print(fav_snacks[key])

for key, value in fav_snacks.items():
    print(key,value)

if "Jack" in fav_snacks:
    print(fav_snacks["Jack"])
else:
    fav_snacks["Jack"] = "ice cream"

print("hello world")
    