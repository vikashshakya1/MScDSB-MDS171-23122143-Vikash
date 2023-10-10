class PetStore:
    def __init__(self):
        self.pet_list = []

    def add_pet(self, pet_name, pet_type, pet_age, pet_price):
        self.pet_list.append({
            "pet_name": pet_name,
            "pet_type": pet_type,
            "pet_age": pet_age,
            "pet_price": pet_price
        })
        print(pet_name,"has been added to the store.")

    def search_pet(self, pet_name):
        for pet in self.pet_list:
            if pet["pet_name"] == pet_name:
                print("Pet found with details:")
                print("Name: ", pet["pet_name"])
                print("Type: ", pet["pet_type"])
                print("Age: ", pet["pet_age"])
                print("Price: ", pet["pet_price"])
                return
        print("Pet not found in the store.")

    def sell_pet(self, pet_name):
        for pet in self.pet_list:
            if pet["pet_name"] == pet_name:
                self.pet_list.remove(pet)
                print(pet_name, " has been sold.")
                return
        print("Pet not found in the store.")

    def list_pets(self):
        for pet in self.pet_list:
            print("Name: ", pet["pet_name"])
            print("Type: ", pet["pet_type"])
            print("Age: ", pet["pet_age"])
            print("Price: ", pet["pet_price"])
            print("------------------")

pet_store = PetStore()
while True:
    print("1. Add new pet")
    print("2. Search for a pet")
    print("3. Sell a pet")
    print("4. List all pets")
    print("5. Exit program")
    choice = int(input("Enter your choice (1-5): "))
    if choice == 1:
        pet_name = input("Enter pet name: ")
        pet_type = input("Enter pet type: ")
        pet_age = int(input("Enter pet age: "))
        pet_price = float(input("Enter pet price: "))
        pet_store.add_pet(pet_name, pet_type, pet_age, pet_price)
    elif choice == 2:
        pet_name = input("Enter pet name to search: ")
        pet_store.search_pet(pet_name)
    elif choice == 3:
        pet_name = input("Enter pet name to sell: ")
        pet_store.sell_pet(pet_name)
    elif choice == 4:
        pet_store.list_pets()
    elif choice == 5:
        break

print("Thank you for using the Pet Store program.")