from Character_model import Raiden, Skirk
from Weapon_model import EngulfingLightning, Azurelight
from Artifact_model import EmblemOfSeveredFate, FinaleOfTheDeepGalleries
from Enemy import Enemy
from DamageFormula import Damage

raiden = Raiden()
el = EngulfingLightning()
esf = EmblemOfSeveredFate()
enemy = Enemy("Hilichurl")



raiden.equip_weapon(el)
raiden.equip_artifact(esf)


raiden.get_passive()
raiden.skill()
raiden.burst()
raiden.constellations()


skk = Skirk()
alt = Azurelight()
fdg = FinaleOfTheDeepGalleries()

skk.equip_weapon(alt)
skk.equip_artifact(fdg)

# alt.get_effect()
# fdg.get_effect()

skk.get_passive('a')
skk.skill()
# skk.normal_attack()
skk.burst()

# skk.info()

''' Skirk singel damege calculation'''

dmg = Damage(skk, enemy)

skk_singel = dmg.damage_calculate()

print(f'skk_singel: \t {skk_singel}')

''' take 0+0 Escoffier in to calculation '''

enemy.resist -= 55

# dmg = Damage(skk, enemy)

skk_ecf00 = dmg.damage_calculate()

print(f'skk_ecf00: \t {skk_ecf00}, \timproved {(skk_ecf00 - skk_singel)/skk_singel}')

''' take 0+1 Escoffier in to calculation '''

skk.ATKBonus += 32

skk_ecf01 = dmg.damage_calculate()

print(f'skk_ecf01 \t {skk_ecf01}, \timproved {(skk_ecf01 - skk_singel)/skk_singel}')

''' take 1+0 Escoffier in to calculation '''

skk.ATKBonus -= 32

skk.CritDMG += 60

skk_ecf10 = dmg.damage_calculate()

print(f'skk_ecf10 \t {skk_ecf10}, \timproved {(skk_ecf10 - skk_singel)/skk_singel}')

''' take 1+1 Escoffier in to calculation '''

skk.ATKBonus += 32

skk_ecf11 = dmg.damage_calculate()

print(f'skk_ecf11 \t {skk_ecf11}, \timproved {(skk_ecf11 - skk_singel)/skk_singel}')


''' take c2 Skirk into calculation '''

