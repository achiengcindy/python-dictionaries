# craeate a ditionary of my favorite animals
fav_pets = {'dog': "terrier", 'bird': 'parrot'}
print(fav_pets)

# Check the values of the key 'dog
dog = fav_pets["dog"]
print(dog)  # 'terrier'

# Check the values of the key 'bird'
bird = fav_pets["bird"]
print(bird)  # 'parrot'

# Check the values of a non-existent key 'dog
non_existent = fav_pets["snake"]
print(non_existent)  # KeyError: 'snake'
