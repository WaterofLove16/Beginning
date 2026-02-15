import sys

class SpellLibrary:
    def __init__(self):
        self.divine = {}
        self.elemental = {}

    def learn_spell(self, spell_name:str, spell_school:str)->str:
        if spell_school != "elemental" and spell_school != "divine":
            return f"{spell_school} is not a valid school of magic"
        
        elif spell_name in (self.divine or self.elemental):
            return f"{spell_school} {spell_name} is already known. Practice spell instead."
        
        else:
            if spell_school == "divine":
                self.divine[spell_name] = 1
            else:
                self.elemental[spell_name] = 1

            return f"{spell_school} {spell_name} has been learned"
        
    def practice_spell(self,spell_name:str, spell_school:str, hours:int)->str:
        if spell_school != ("elemental" and "divine"):
            return f"{spell_school} is not a valid school of magic"
        
        elif spell_name not in (self.divine or self.elemental):
            return f"{spell_school} {spell_name} is not known. Learn spell instead."
        
        else:
            if spell_school == "divine":
                self.divine[spell_name] += hours
                new_mastery = self.divine[spell_name]
            else:
                self.elemental[spell_name] += hours
                new_mastery = self.elemental[spell_name]

            return f"{spell_school} {spell_name} mastery increased to {new_mastery}"
        
    def forget_spell(self, spell_name:str, spell_school:str)->str:
        if spell_school != ("elemental" and "divine"):
            return f"{spell_school} is not a valid school of magic"
        
        elif spell_name not in (self.divine or self.elemental):
            return f"{spell_school} {spell_name} is not known."
        
        else:
            if spell_school == "divine":
                mastery_level = self.divine[spell_name]

                if mastery_level <= 0:
                    self.divine.pop(spell_name)
                    return f"{spell_school} {spell_name} has been completely forgotten."
                else: 
                    self.divine[spell_name] -= 1
                    mastery = self.divine[spell_name]
                    return f"{spell_school} {spell_name} mastery decreased to {mastery}"

            else:
                mastery_level = self.elemental[spell_name]

                if mastery_level <= 0:
                    self.elemental.pop(spell_name)
                    return f"{spell_school} {spell_name} has been completely forgotten."
                else: 
                    self.elemental[spell_name] -= 1
                    mastery = self.elemental[spell_name]
                    return f"{spell_school} {spell_name} mastery decreased to {mastery}"

    def str(self)->str:
        title = "Wizard's Grimoire"
        spell_school = []
        if len(self.elemental) != 0:
            spell_school.append("elemental")
        if len(self.divine) != 0:
            spell_school.append("divine")

        if len(self.divine) == 0 and len(self.elemental) == 0:
            return "No spells were learned."
        else:
        

if __name__ == "__main__":

    school = sys.argv[1]
    name = sys.argv[2]
    library = SpellLibrary()
    spell = library.learn_spell(name,school)
    master_spell = library.practice_spell(name,school,7)

    for i in range(9):
        done = library.forget_spell(name,school)

    print(spell)
    print(master_spell)
    print(done)
