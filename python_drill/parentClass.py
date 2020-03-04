
# Parent class
class Organism:
    name = "unknown"
    species = "unknown"
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg


# Child class
class Human(Organism):
    name = "Pedro"
    species = "Homosapien"
    legs = 2
    arms = 2
    origin = "Earth"

    def intelligence(self):
        msg = "\nCan learn and adapt to any situation."
        return msg

            
# Child class
class Dog(Organism):
    name = "Ruppy"
    species = "Canine"
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = "Earth"

    def Bite(self):
        msg = "\nEmits a loud growl, and bites down on it's target"
        return msg





if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.intelligence())

    dog = Dog()
    print(dog.information())
    print(dog.Bite())
   
