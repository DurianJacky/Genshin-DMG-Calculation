from Character_model import Character

class Artifact:
    def __init__(self, name, equiped = 4):
        self.name = name

        self.ER = 0
        self.ATKBonus = 0
        self.ATKFlat = 311
        self.HPBonus = 0
        self.HPFlat = 4780
        self.DEFBonus = 0
        self.DEFFlat = 0
        self.EMFlat = 0
        self.DMGBonus = 0
        self.Crit = 0
        self.CritDMG = 0

        self.equiped = equiped
        self.character = None

    def equip(self, character: Character):
        self.character = character
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


class EmblemOfSeveredFate(Artifact):
    def __init__(self, name = "Emblem of Severed Fate", equiped = 4):
        super().__init__(name, equiped)
        self.ATKBonus += 46.6 + 15.2
        self.ER += 51.8 + 17.5
        self.ATKFlat += 31 + 14
        self.CritDMG += 66.8

    def get_stats(self):
        self.character.ATKBonus += self.ATKBonus
        self.character.ATKFlat += self.ATKFlat
        self.character.CritDMG += self.CritDMG
        self.character.ER += self.ER
        # 2-Piece Set Bonus: Energy Recharge +20%
        if(self.equiped >= 2):
            self.ER += 20
            self.character.ER += 20

    def get_effect(self):
        # 4-Piece Set Bonus: Increases Elemental Burst DMG by 25% of Energy Recharge. 
        # A maximum of 75% bonus DMG can be obtained in this way.
        if(self.equiped >= 4):
            ER = self.character.ER
            DMGBonus = 0.25 * ER
            if DMGBonus >= 75:
                DMGBonus = 75
            self.DMGBonus += DMGBonus
            self.character.DMGBonus += DMGBonus
        

class FinaleOfTheDeepGalleries(Artifact):
    def __init__(self, name = 'Finale Of The Deep Galleries', equiped=4):
        super().__init__(name, equiped)
        self.ATKBonus += 4.7 + 11.7 + 46.6 + 46.6
        self.ATKFlat += 33
        self.Crit += 6.2 + 3.1 + 3.5 + 10.1 + 8.6
        self.CritDMG += 13.2 + 24.9 +  22.5 + 62.2 + 20.2
        self.DMGBonus += 0

    def get_stats(self):
        self.character.ATKBonus += self.ATKBonus
        self.character.ATKFlat += self. ATKFlat
        self.character.Crit += self.Crit
        self.character.CritDMG += self.CritDMG
        self.character.DMGBonus += self.DMGBonus

    def get_effect(self):
        self.character.DMGBonus += 60 + 15
