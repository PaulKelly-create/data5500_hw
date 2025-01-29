#create class
class Pet():
    #create species to use, and avergae lifespan
    #asked chatgpt how to get species, and their avg lifespan into the class, it helped me use a dictionary for this task
    species = {
        "Dog": 14,
        "Cat": 15,
        "Aligator": 500
    }
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
    #have different species use different human age
    def pet_human_age(self):
        if self.species == "Dog":
            return print(self.name, "age in human years is", self.age * 7)
        elif self.species == "Cat":
            return print(self.name, "age in human years is", self.age * 5)
        else:
            return print(self.name, "age in human years is", self.age)
    #return the species average lifespan
    #asked chatgpt how to get the avg lifespan from the dictionary, it helped with Pet.species.get helping me get the avg lifespan
    def average_lifespan(self):
        return print("The average lifespan for", self.name, "who is a", self.species, "is", Pet.species.get(self.species, "Unknown species"))



#make the objects
boe = Pet("Boe", 10, "Dog")
grant = Pet("Grant", 35, "Aligator")
lucy = Pet("Lucy", 1, "Cat")

#call the functions
boe.pet_human_age()
boe.average_lifespan()
grant.pet_human_age()
grant.average_lifespan()
lucy.pet_human_age()
lucy.average_lifespan()
