class Character:
    def __init__(self, name, level=90):
        self.name = name
        self.level = level
        
        self.ATK = 0
        self.ATKBonus = 0
        self.ATKFlat = 0

        self.DEF = 0
        self.DEFBonus = 0
        self.DEFFlat = 0

        self.HP = 0
        self.HPBonus = 0
        self.HPFlat = 0

        self.EM = 0
        self.EMFlat = 0

        self.DMGBonus = 0
        self.CritDMG = 50
        
        self.ER = 100

        self.talent = 0

        self.DefIgnore = 0

        self.ReactionBonus = 0

        self.skillTalent = 0

        self.weapon = None
        self.artifact = None
    
    def equip_weapon(self, weapon: Weapon):
        self.weapon = weapon
        weapon.equip(self)

    def equip_artifact(self, artifact: Artifact):
        self.artifact = artifact
        artifact.equip(self)

    def nomal_attack(self):
        pass

    def get_passive(self):
        pass

    def skill(self):
        pass

    def burst(self):
        pass

    def constellations(self):
        pass

    def info(self):
        print(f"{self.__class__.__name__} 属性列表：")
        for key, value in self.__dict__.items():
            if(value != 0):
                value = round(value, 2) if isinstance(value, float) else value
                print(f"\t{key}: {value}")

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
        self.CritDMG = 0

        self.equiped = equiped
        self.character = None

    def equip(self, character: Character):
        self.character = character
        self.get_stats()

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