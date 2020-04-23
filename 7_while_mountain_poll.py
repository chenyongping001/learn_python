responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Whick mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("\n Would you like to let another person respon?(yes/ no)")
    if repeat == 'no':
        polling_active = False

print("\n --- poll result ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
