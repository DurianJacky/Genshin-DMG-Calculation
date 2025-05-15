from Character_model import Character
from Enemy import Enemy


class Damage:
    def __init__(self, character: Character, enemy: Enemy, attack_type: str = 'brust'):
        '''attack = 'brust' or 'na' or 'skill' '''
        self.character = character
        self.enemy = enemy
        self.attack_type = attack_type
        self.ATK = 0
        self.DEF = 0
        self.HP = 0
        self.EM = 0
        self.B = 0
        self.C = 0
        self.D = 0
        self.R = 0
        self.R_amp = 0
        
    def atk(self):
        ATKBase = self.character.ATK
        ATKBonus = self.character.ATKBonus
        ATKFlat = self.character.ATKFlat
        ATK = (ATKBase * (1 + ATKBonus / 100) + ATKFlat)
        return ATK
        
    def defence(self):
        DEFBase = (self.character.DEF)
        DEFBonus = self.character.DEFBonus
        DEFFlat = self.character.DEFFlat
        DEF = (DEFBase * (1 + DEFBonus / 100) + DEFFlat)
        return DEF
    
    def hp(self):
        HPBase = (self.character.HP)
        HPBonus = self.character.HPBonus
        HPFlat = self.character.HPFlat
        HP = (HPBase * (1 + HPBonus / 100) + HPFlat)
        return HP
    
    def em(self):
        EMBase = (self.character.EM)
        EMFlat = self.character.EMFlat
        EM = (EMBase + EMFlat)
        return EM
    
    def damage_bonus(self):
        # “造成的伤害提升/增加值”为基础倍率区，“造成的伤害提高”为增伤区，注意“值”
        DMGBonusMult = 1 + self.character.DMGBonus / 100
        return DMGBonusMult

    def crit(self):
        return self.character.Crit / 100

    def critical_damage(self):
        # Critical Hits
        CritDMG = self.character.CritDMG
        CRIT = 1 + CritDMG / 100
        return CRIT
    
    def enemy_defense(self):
        # Enemy defense multiplier
        DefReduction = self.enemy.DefReduction / 100
        DefIgnore = self.character.DefIgnore / 100
        level_character = self.character.level
        level_enemy = self.enemy.level
        EnemyDefMult = ((level_character + 100) / ((level_character + 100) 
               + (level_enemy + 100) * (1 - DefReduction) * (1 - DefIgnore)))
        return EnemyDefMult
    
    def resistance(self):
        # Enemy resistance multiplier
        resistance = self.enemy.resist / 100
        
        if(resistance < 0):
            EnemyResMult = (1 - resistance/2)
        elif(resistance < 0.75):
            EnemyResMult = (1 - resistance)
        else:
            EnemyResMult = (1 / (4 * resistance + 1))
        
        return EnemyResMult
    
    def base_DMG_multiplier(self):
        # Base Damage Multiplier
        BaseDMGMultiplier = 1
        if(self.character.skillTalent != 0):
            BaseDMGMultiplier = self.character.skillTalent
        
        return BaseDMGMultiplier

    def amplifying_reaction(self, trigger):
        # trigger = 2 for triggering inverse amplifying reaction, 
        # trigger = 1.5 for triggering amplifying reaction,
        # trigger = 1 for not triggering reaction
        
        EM = self.em()
        
        if(trigger == 2):
            reaction_multiplier = 2
        else:
            reaction_multiplier = 1.5

        if(trigger == 1):
            AmplifyingReaction = 1
        else:
            AmplifyingReaction = reaction_multiplier * (1 
                                       + 2.78 * EM / (1400 + EM)
                                       + self.character.ReactionBonus / 100)
        
        return AmplifyingReaction
    
    def transformative_reaction(self, trigger):
        trigger = 1
        TransformativeReaction = trigger
        return TransformativeReaction
    
    def additive_base_DMG_bonus(self):
        AdditiveBaseDMGBonus = 0
        return AdditiveBaseDMGBonus
    
    def DMG_reduction_target(self):
        DMGReductionTarget = 0
        return DMGReductionTarget

    def info(self):
        print(f"{self.__class__.__name__} 属性列表：")
        for key, value in self.__dict__.items():
            if(value != 0):
                value = round(value, 2) if isinstance(value, float) else value
                print(f"\t{key}: {value}")

    def damage_calculate(self, type: str = "ATK", trigger = 1, expect: bool = False):
        # type = "ATK" for calculating damage based on ATK,
        # type = "HP" for calculating damage based on HP,
        # type = "DEF" for calculating damage based on DEF,
        # type = "EM" for calculating damage based on EM,
        # type = "ATK+DEF" for calculating damage based on ATK and DEF,
        # type = "ATK+HP" for calculating damage based on ATK and HP,
        # type = "ATK+EM" for calculating damage based on ATK and EM.
        if self.attack_type == 'na':
            talent = self.character.normal_attack_talent
        elif self.attack_type == 'brust':
            talent = self.character.brust_talent
        else:
            talent = self.character.skill_talent

        self.talent = talent

        ATK = round(self.atk())
        HP = round(self.hp())
        DEF = round(self.defence())
        EM = round(self.em())
        Crit_expect = self.crit()

        if(type == "ATK"):
            BaseDMG = talent/100 * ATK
        elif(type == "HP"):
            BaseDMG = talent/100 * HP
        elif(type == "DEF"):
            BaseDMG = talent/100 * DEF
        elif(type == "EM"):
            BaseDMG = talent/100 * EM
        elif(type == "ATK+DEF"):
            BaseDMG = talent[0]/100 * ATK + talent[1]/100 * DEF
        elif(type == "ATK+HP"):
            BaseDMG = talent[0]/100 * ATK + talent[1]/100 * HP
        elif(type == "ATK+EM"):
            BaseDMG = talent[0]/100 * ATK + talent[1]/100 * EM


        AdditiveBaseDMGBonus = self.additive_base_DMG_bonus()
        DMGBonusMult = self.damage_bonus()
        DMGReductionTarget = self.DMG_reduction_target()
        CRIT = self.critical_damage()
        EnemyDefMult = self.enemy_defense()
        EnemyResMult = self.resistance()
        BaseDMGMultiplier = self.base_DMG_multiplier()
        AmplifyingReaction = self.amplifying_reaction(trigger)

        self.BaseDMG = BaseDMG
        self.AdditiveBaseDMGBonus = AdditiveBaseDMGBonus
        self.DMGBonusMult = DMGBonusMult
        self.DMGReductionTarget = DMGReductionTarget
        self.CRIT = CRIT
        self.EnemyDefMult = EnemyDefMult
        self.EnemyResMult = EnemyResMult
        self.BaseDMGMultiplier = BaseDMGMultiplier
        self.AmplifyingReaction = AmplifyingReaction

        
        DMG = round(((BaseDMG * BaseDMGMultiplier) + AdditiveBaseDMGBonus)
             *(DMGBonusMult - DMGReductionTarget) * CRIT
             * EnemyDefMult * EnemyResMult * AmplifyingReaction)
        
        self.DMG = DMG
        self.DMG_expect = DMG * Crit_expect
        
        if expect:
            return self.DMG_expect
        
        return self.DMG

        




