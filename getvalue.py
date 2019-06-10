# craeate a ditionary of my favorite animals
fav_pets = {'dog': "terrier", 'bird': 'parrot'}

# Check the values of the key 'dog
dog = fav_pets.get("dog")

# Check the values of a non-existent key 'snake' using get
non_existent = fav_pets.get("snake")


print(fav_pets)
print(dog)  # 'terrier'
print(non_existent)  # displays None

