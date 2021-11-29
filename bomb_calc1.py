"""This module's purpose is to simulate a bomber attacking a player. Tether Bomber's use Siphoning Tether followed by Sap Essence. 
Proximity Detonation is also a skilled that is precasted before the bomb but is hard to simulate because it scales with amount players hit.
It is assumed bomber is wearing the set Vicious Death."""

from random import randint
from typing import Union


def mitigation_formula(resistance, penetration) -> float:
    """Calculates the mitigation based on zergling's resistance and bomber's penetration."""
    mitigation: float = 0.0
    if penetration > resistance:
        mitigation = 1.0
    else:
        mitigation = 1 - ((resistance - penetration) / 66000)
    print(f"Zergling mitigates: {mitigation}")
    return mitigation


def crit_modifier_formula(crit_resistance, crit_multiplier) -> float:
    """Calculates the critical strike damage modifier based on the critical resistance of Zergling and bomber's critical ddamage multiplier."""
    crit_modifier: float = 0.0
    crit_resistance = crit_resistance / 6800
    crit_modifier = crit_multiplier
    return crit_modifier


def skill_tooltip_func(skill_type: str, magicka: int, spell_damage: int, ult: int) -> float:
    """Generates the skill_tooltip attributes. 450 is white noise fit."""
    strike_from_shadow: int = 300
    if skill_type == "sap essence" or skill_type == "sap":
        coefficient_a: float = 0.0776449
        coefficient_b: float = 0.813444
    if skill_type == "soul tether" or skill_type == "tether":
        coefficient_a = 0.160077
        coefficient_b = 1.68057
    skill: float = (coefficient_a * magicka) + (coefficient_b * (spell_damage + ult + strike_from_shadow))
    print(f"Skill Tooltip: {skill}")
    return skill


def vd_tooltip_func(magicka: int, spell_damage: int, ult: int) -> float:
    """Generates the skill_tooltip attributes. 450 is white noise fit."""
    strike_from_shadow: int = 300
    coefficient_a: float = 0
    coefficient_b: float = 3.32305
    skill: float = (coefficient_a * magicka) + (coefficient_b * (spell_damage + ult + strike_from_shadow)) - .939185
    print(f"Skill Tooltip: {skill}")
    return skill


class Zergling:
    """Class that stores important mitigation stats of player defending. Zergling is a name for a player who stacks in a group and is suspectible to being bombed."""
    resistance: int
    crit_resistance: float
    health: float
    healing: int

    def __init__(self, resistance: Union[int, None] = None, crit_resistance: Union[float, None] = None, health: Union[int, None] = None, healing: Union[int, None] = None):
        """Initializes attributes for Zergling class."""
        if resistance == None:
            self.resistance = input("how much resistance does the bot have? ")
            if self.resistance == "":
                self.resistance = 0
            else:
                self.resistance = int(self.resistance)
        else:
            self.resistance = resistance

        if crit_resistance == None:
            self.crit_resistance = input("how much crit resistance is the bot wearing? ")
            if self.crit_resistance == "":
                self.crit_resistance = 0.0
            else:
                self.crit_resistance = float(self.crit_resistance)
        else:
            self.crit_resistance = crit_resistance

        if health == None:
            self.health = int(input("How much health does Zergling have? "))
            if self.health == "":
                self.health = 0
            else:
                self.health = int(self.health)
        else:
            self.health = health

        if healing == None:
            self.healing = input("How much does the target heal per second?")
            if self.healing == "":
                self.healing == 0
            else:
                self.healing = int(self.healing)
        else:
            self.healing = healing


class Bomber:
    """Class that stores important offensive stats of bomber. Bomber is a player who is built to kill massive amounts of stacked players in approximately 3 seconds."""
    magicka: int
    spell_damage: int
    crit_percent: int
    light_armor: float 
    medium_armor: float
    divines: float
    ult: int
    mundus: str
    race: str
    weapon: str
    weapon_trait: str

    def __init__(self, magicka: Union[int, None] = None, spell_damage: Union[int, None] = None, crit_percent: Union[float, None] = None, light_armor: Union[float, None] = None, medium_armor: Union[float, None] = None, divines: Union[float, None] = None, ult: Union[int, None] = None, mundus: Union[str, None] = None, race: Union[str, None] = None, weapon: Union[str, None] = None, weapon_trait: Union[None, str] = None):
        """Initializes attributes for Bomber class."""
        if magicka == None:
            self.magicka = input("what is the max mag? ")
            if self.magicka == "":
                self.magicka = 0
            else:
                self.magicka = int(self.magicka)
        else:
            self.magicka = magicka
        if spell_damage == None:
            self.spell_damage = input("what is the spell damage? ")
            if self.spell_damage == "":
                self.spell_damage = 0
            else:
                self.spell_damage = int(self.spell_damage)
        else:
            self.spell_damage = spell_damage
        if crit_percent == None:
            self.crit_percent = input("what is the chance of doing critical damage? ")
            if self.crit_percent == "":
                self.crit_percent = 0.0
            else:
                self.crit_percent = float(self.crit_percent)
        else:
            self.crit_percent = crit_percent
        if light_armor == None:
            self.light_armor = input("how many light pieces you wearing boss? no judgement. ")
            if self.light_armor == "":
                self.light_armor = 0.0
            else:
                self.light_armor = float(self.light_armor)
        else:
            self.light_armor = light_armor
        if medium_armor == None:
            self.medium_armor = input("how many medium pieces you wearing boss? no judgement. ")
            if self.medium_armor == "":
                self.medium_armor = 0.0
            else:
                self.medium_armor = float(self.medium_armor)
        self.medium_armor = medium_armor
        if divines == None:
            self.divines = input("how many divines you wearing boss? no judgement. ")
            if self.divines == "":
                self.divines = 0.0
            else:
                self.divines = float(self.divines)
        else:
            self.divines = divines
        if ult == None:            
            self.ult = input('How much Ultimate are you packing? ')
            if self.ult == "":
                self.ult = 0.0
            else:
                self.ult = int(self.ult)
        else:
            self.ult = ult
        if mundus == None:
            self.mundus = input("What mundus is used? (only shadow matters) ")
        else:
            self.mundus = mundus
        if race == None:
            self.race = input("what race are you? ")
        else:
            self.race = race
        if weapon == None:
            self.weapon = input("what type of weapon?(only axe and mace matter) ")
        else:
            self.weapon = weapon
        if weapon_trait == None:
            self.weapon_trait = input("what trait is on the weapon? (Only sharpened matters) ")
        else:
            self.weapon_trait = weapon_trait
     

    def penetration_formula(self) -> int:
        """Calculate how much armor a bomber and shred with it's penetration. Generate by it's own attributes."""
        penetration: int = 0
        balorgh: int = self.ult * 23
        light_armor_buff: int = self.light_armor * 939
        nightblade_flanking: int = 2974
        cp: int = 700
        if self.weapon_trait == "sharpened":
            sharpened_trait: int = 3276
        else:
            sharpened_trait: int = 0
        if self.weapon == "mace" or self.weapon == "maul":
            mace_buff: int = 3300
        else:
            mace_buff: int = 0
        set_bonus: int = 1487
        penetration = balorgh + light_armor_buff + nightblade_flanking + cp + sharpened_trait + set_bonus + mace_buff
        print(f"Bomber's pentration: {penetration}")
        return penetration

    def crit_multiplier_func(self) -> float:
        """Calculate the critical strike damage multiplier from within the objects attributes."""
        crit_multiplier: float = 0.0
        # base shadow mundus is .11 then add the divines pieces.
        if self.mundus == "shadow":
            shadow: float = .11 * (1 +(self.divines * .091))
        else:
            shadow: float = 0
        medium_armor_buff: float = .02 * self.medium_armor
        if self.race == 'khajit' or self.race == 'Khajit':
            khajit_buff: float = .12
        else:
            khajit_buff: float = 0
        base_crit: float = .5
        if self.weapon_trait == "axe":
            axe_buff: float = .12
        else:
            axe_buff: float = 0.0
        minor_force: float = .1
        fighting_finese: float = .1
        back_stabber: float = .15
        class_passive: float = .1
        crit_multiplier = 1 + base_crit + minor_force + axe_buff + class_passive + medium_armor_buff + shadow + fighting_finese + back_stabber + khajit_buff
        print(f"Bomber's crit multiplier: {crit_multiplier}")
        return crit_multiplier

    def crit_chance_func(self) -> bool:
        """Simulate if critical damage will be dealt."""
        random_chance: int = randint(1, 100)
        result: bool = self.crit_percent > random_chance
        return result

    def vicious_death_proc(self, defending: list[Zergling], vd_counter: int) -> list[Zergling]:
        """Vicious death damage when proc'd (when procedural condition is met). Proc condition is a defending player being dealt a killer blow."""
        living_zerglings: list[Zergling] = []
        for zergling in defending:
            i: int = 0
            while i < vd_counter:
                mitigation: float = mitigation_formula(zergling.resistance, self.penetration_formula())
                base_damage: float = mitigation * vd_tooltip_func(self.magicka, self.spell_damage, self.ult)
                if self.crit_chance_func():
                    crit_modifier: float = crit_modifier_formula(zergling.crit_resistance, self.crit_multiplier_func())
                    damage: float = base_damage * crit_modifier
                else:
                    damage: float = base_damage
                zergling.health = zergling.health - damage
                if zergling. health <= 0:
                    print("vd has killed zergling.")
                    i += vd_counter
                    vd_counter += 1
                else:
                    zergling.health += zergling.healing
            if zergling.health > 0:
                living_zerglings.append(zergling)
        return living_zerglings

    def first_attack(self, defending: Union[Zergling, list[Zergling]]) -> Union[list, Zergling]:
        """Simulates first attack from stealth. This should always crit based on nightblade passive skill."""
        skill_type: str = input("What skill are we performance? ")
        alive: list = []
        if isinstance(defending, Zergling):
            mitigation: float = mitigation_formula(defending.resistance, self.penetration_formula())
            base_damage: float = mitigation * skill_tooltip_func(skill_type, self.magicka, self.spell_damage, self.ult)
            crit_modifier: float = crit_modifier_formula(defending.crit_resistance, self.crit_multiplier_func())
            damage: float = base_damage * crit_modifier
            print(f"Damage that was dealt = {damage}")
            defending.health = defending.health - damage
            if defending.health <= 0:
                print(f"Zergling has been defeated. Health: {defending.health}")
            if defending.health > 0:
                print(f"Try harder, Zergling health: {defending.health} and healed for {defending.healing}")
                defending.health += defending.healing
            return defending
        if isinstance(defending, list):
            vd_counter: int = 0
            for i in range(len(defending)):
                mitigation: float = mitigation_formula(defending[i].resistance, self.penetration_formula())
                base_damage: float = mitigation * skill_tooltip_func(skill_type, self.magicka, self.spell_damage, self.ult)
                crit_modifier: float = crit_modifier_formula(defending[i].crit_resistance, self.crit_multiplier_func())
                damage: float = base_damage * crit_modifier
                print(f"Damage that was dealt = {damage}")
                defending[i].health = defending[i].health - damage
                if defending[i].health <= 0:
                    print(f"{i} has been defeated. Health: {defending[i].health}")
                    vd_counter += 1
                if defending[i].health > 0:
                    print(f"Try harder, {i} health: {defending[i].health} and healed for {defending[i].healing}")
                    defending[i].health += defending[i].healing
                    alive.append(defending[i])

            print(f"There are {len(alive)} Zerglings left before Vicious Death.")
            alive = self.vicious_death_proc(alive, vd_counter)
            print(f"There are {len(alive)} left after attack")
            return alive       

    def subsequent_attack(self, defending: Union[Zergling, list[Zergling]]) -> Union[list, Zergling]:
        """Anything that follows the first attack will rely on crit chance to use critical modifier."""
        skill_type: str = input("What skill are we performance? ")
        if isinstance(defending, Zergling):
            mitigation: float = mitigation_formula(defending.resistance, self.penetration_formula())
            base_damage: float = mitigation * skill_tooltip_func(skill_type, self.magicka, self.spell_damage, self.ult)
            if self.crit_chance_func():
                crit_modifier: float = crit_modifier_formula(defending.crit_resistance, self.crit_multiplier_func())
                damage: float = base_damage * crit_modifier
            else:
                damage: float = base_damage
            print(f"Damage that was dealt = {damage}")
            defending.health = defending.health - damage
            if defending.health <= 0:
                print(f"Zergling has been defeated. Health: {defending.health}")
            if defending.health > 0:
                print(f"Try harder, Zergling health: {defending.health} and healed for {defending.healing}")
                defending.health += defending.healing
            return Zergling
        if isinstance(defending, list):
            vd_counter: int = 0
            alive: list = []
            for i in range(len(defending)):
                mitigation: float = mitigation_formula(defending[i].resistance, self.penetration_formula())
                base_damage: float = mitigation * skill_tooltip_func(skill_type, self.magicka, self.spell_damage, self.ult)
                if self.crit_chance_func():
                    crit_modifier: float = crit_modifier_formula(defending[i].crit_resistance, self.crit_multiplier_func())
                    damage: float = base_damage * crit_modifier
                else:
                    damage: float = base_damage
                print(f"Damage that was dealt = {damage}")
                defending[i].health = defending[i].health - damage
                if defending[i].health <= 0:
                    print(f"defending[i] has been defeated. Health: {defending[i].health}")
                    vd_counter += 1
                if defending[i].health > 0:
                    print(f"Try harder, defending[i] health: {defending[i].health} and healed for {defending[i].healing}")
                    defending[i].health += defending[i].healing
                    alive.append(defending[i])
            print(f"There are {len(defending)} Zerglings left before Vicious Death.")
            defending = self.vicious_death_proc(defending, vd_counter)
            print(f"There are {len(defending)} left after attack")
            return alive

def main() -> None:
    """Starting place."""
    Tremaine: Bomber = Bomber(37000, 4500, 55, 5, 2, 7, 500, 'thief', 'elf', 'dagger', 'nirn')
    Sinned: Zergling = Zergling(25000, 1500, 26000, 5000)
    a_zergling: Zergling = Zergling(30000, 3000, 35000, 5000)
    b_zergling: Zergling = Zergling(25000, 2700, 28000, 5000)
    c_zergling: Zergling = Zergling(25000, 2700, 28000, 5000)
    d_zergling: Zergling = Zergling(25000, 2700, 28000, 5000)
    myList: list[Zergling] = [a_zergling, Sinned, b_zergling, c_zergling, d_zergling]
    myList = Tremaine.first_attack(myList)
    if len(myList) > 0:
        myList = Tremaine.subsequent_attack(myList)

if __name__ == '__main__':
    main()
