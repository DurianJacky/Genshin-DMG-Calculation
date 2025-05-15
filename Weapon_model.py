from Character_model import Character

class Weapon:
    def __init__(self, name, ATK=0, REFINEMENTS = 1):
        self.name = name
        self.ATK = ATK

        self.ER = 0
        self.ATKBonus = 0
        self.ATKFlat = 0
        self.HPBonus = 0
        self.HPFlat = 0
        self.DEFBonus = 0
        self.DEFFlat = 0
        self.EMFlat = 0
        self.DMGBonus = 0
        self.Crit = 0
        self.CritDMG = 0

        self.REFINEMENTS = REFINEMENTS
        self.character = None

    def equip(self, character: Character):
        self.character = character
        self.character.ATK += self.ATK
        self.get_stats()
        self.get_effect()
        
    
    def get_stats(self):
        pass

    def get_effect(self):
        pass

    def info(self):
        print(f"{self.__class__.__name__} 属性列表：")
        for key, value in self.__dict__.items():
            if (value):
                value = round(value, 2) if isinstance(value, float) else value
                print(f"\t{key}: {value}")



class EngulfingLightning(Weapon):
    def __init__(self, name = "Engulfing Lightning", ATK = 608):
        super().__init__(name, ATK)
        self.ER = 55.1
    
    def get_stats(self):
        # ATK increased by 28%/35%/42%/49%/56% of Energy Recharge over the base 100%.  
        ER_increase = [30, 35, 40, 45, 50]
        self.ER += ER_increase[self.REFINEMENTS - 1]
        self.character.ER += self.ER

    def get_effect(self):
        # You can gain a maximum bonus of 80%/90%/100%/110%/120% ATK. 
        # Gain 30%/35%/40%/45%/50% Energy Recharge for 12s after using an Elemental Burst.

        ATK_increase = [0.28, 0.35, 0.42, 0.49, 0.56]
        ATK_increase_max = [80, 90, 100, 110, 120]

        ATK_increase_real = ATK_increase[self.REFINEMENTS - 1] * (self.character.ER - 100)
        if ATK_increase_real > ATK_increase_max[self.REFINEMENTS - 1]:
            ATK_increase_real = ATK_increase_max[self.REFINEMENTS - 1]

        self.ATKBonus += ATK_increase_real

        self.character.ATKBonus += ATK_increase_real


class Azurelight(Weapon):
    def __init__(self, name = 'Azurelight', ATK=674, REFINEMENTS=1):
        super().__init__(name, ATK, REFINEMENTS)
        self.Crit = 22.1

    def get_stats(self):
        self.character.Crit += self.Crit


    def get_effect(self):
        self.character.ATKBonus += 24 + 24
        self.character.CritDMG += 40