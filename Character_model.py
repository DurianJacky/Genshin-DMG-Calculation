

class Character:
    def __init__(self, name, level=90, constellation = 0):
        self.name = name
        self.level = level
        self.constellation = constellation
        
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
        

        self.Crit = 5
        self.CritDMG = 50
        
        self.ER = 100

        self.normal_attack_talent = 0
        self.skill_talent = 0
        self.brust_talent = 0
        self.extra_talent = 0

        self.DefIgnore = 0

        self.ReactionBonus = 0

        self.skillTalent = 0

        self.weapon = None
        self.artifact = None
    
    def equip_weapon(self, weapon):
        self.weapon = weapon
        weapon.equip(self)

    def equip_artifact(self, artifact):
        self.artifact = artifact
        artifact.equip(self)

    def normal_attack(self):
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
        

class Raiden(Character):
    def __init__(self, name = "Raiden", level=90, constellation = 2):
        super().__init__(name, level, constellation)
        self.ATK = 337
        self.HP = 12907
        self.DEF = 789
        self.ER = 100 + 32
        self.constellations()
        

    def get_passive(self):
        # Enlightened One: Each 1% above 100% Energy Recharge:
        # 0.4% Electro DMG Bonus.
        ER = self.ER
        self.DMGBonus += 0.4 * (ER - 100)

    def skill(self):
        # Transcendence: Baleful Omen
        # Increases the entire party's Elemental Burst DMG by 20% for 8s.
        DMGBonus = 0.3 * 90
        self.DMGBonus += DMGBonus

    def burst(self, stacks = 60):
        # Secret Art: Musou Shinsetsu
        # Chakra Desiderata: The maximum number of Resolve stacks is 60.
        ResolveBonus = 7 * stacks # 7% ATK per stack
        talentInitial = 721 # 721% ATK
        self.brust_talent = talentInitial + ResolveBonus

    def constellations(self):
        # C2: Raiden Shogun's attacks ignore 60% of opponents' DEF
        if(self.constellation >= 2):
            self.DefIgnore = 60


class Skirk(Character):
    def __init__(self, name = "Skirk", level=90, constellation = 0):
        super().__init__(name, level, constellation)
        self.ATK = 359
        self.DMGBonus += 38.4
        self.na_DMGbonus = 0
        self.stack = 0
        self.stack_limit = 100
        self.stack_used = 0
        self.stack_used_limit = 12

        self.constellations()
        

    def get_passive(self, action: str = 'a'):
        '''
        Action: 'a' or 'q'
        '''
        self.stack += 8 * 3
        if action == 'a':
            self.skillTalent = 1.7
        else:
            self.skillTalent = 1.6
    
    def normal_attack(self):
        na_talent = [281.1, 253.5, 160.3*2, 170.4*2, 416.1]
        self.normal_attack_talent += sum(na_talent) + self.extra_talent
        self.DMGBonus += 20.0 + self.na_DMGbonus

    def skill(self):
        self.stack += 45
    
    def burst(self):
        self.stack = self.stack_limit if self.stack > self.stack_limit else self.stack
        self.stack_used = (self.stack - 50) if (self.stack - 50) <= self.stack_used_limit else self.stack_used_limit
        self.brust_talent_bonus = 29.93 * self.stack_used
        self.brust_talent += 248.6 * 5 + 414.4 + self.extra_talent + self.brust_talent_bonus
    
    def constellations(self):
        if self.constellation >= 1:
            self.extra_talent += 500

        if self.constellation >=2:
            self.stack += 12
            self.stack_used_limit += 12
            self.na_DMGbonus = 60.0




    