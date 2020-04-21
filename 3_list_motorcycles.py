motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuzi')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
motorcycles_pop = motorcycles.pop()
print(motorcycles)
print(motorcycles_pop)

motorcycles = ['honda','yamaha','suzuki']
last_own = motorcycles.pop()
print("The last motocycle I owned was a " + last_own.title() + ".")

motorcycles = ['honda','yamaha','suzuki']
first_own = motorcycles.pop(0)
print("The first motocycle I owned was a " + first_own.title() + ".")

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('suzuki')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(("\nA " + too_expensive.title() + " is too expensive for me."))