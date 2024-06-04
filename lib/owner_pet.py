class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type in self.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise TypeError("Pet must be available in Pet Types")
        self._owner = owner
        self.all.append(self)

    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        if not isinstance(owner, Owner):
            raise TypeError("Owner must be an instance of Class")
        else:
            self._owner = owner
        

class Owner:
    def __init__(self, name):
        self.name = name
         
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Pet must be an instance of Class")
        else:
            pet.owner = self

    def get_sorted_pets(self):
       sorted_pets = sorted(self.pets(), key=lambda x: x.name)
       return sorted_pets