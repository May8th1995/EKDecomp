learnsets = open('basestats.txt', 'r')
Lines = learnsets.readlines()

#This script does not make a perfect import and some find and replace is needed to make it work perfectly.
for lines in Lines:
    data = lines.split(",")
    print("\t[SPECIES_"+data[0].split("#")[1].replace("'","")+"] =\n\t{") #mon name
    print("\t\t.baseHP = "+ data[1]+",") #base hp
    print("\t\t.baseAttack = "+ data[2]+",") #base atk
    print("\t\t.baseDefense = "+ data[3]+",") #base def
    print("\t\t.baseSpeed = "+ data[4]+",") #base spe
    print("\t\t.baseSpAttack = "+ data[5]+",") #base spa
    print("\t\t.baseSpDefense = "+ data[6]+",") #base spdef
    
    data[7] = data[7].replace(" ","")
    if data[7] == "FIGHT":
        data[7] = "FIGHTING"
    if data[7] == "PSYCHC":
        data[7] = "PSYCHIC"
    if data[7] == "ELECTR":
        data[7] = "ELECTRIC"
    print("\t\t.type1 = TYPE_" + data[7]+",") #type 1
    data[8] = data[8].replace(" ","")
    if data[8] == "FIGHT":
        data[8] = "FIGHTING"
    if data[8] == "PSYCHC":
        data[8] = "PSYCHIC"
    if data[8] == "ELECTR":
        data[8] = "ELECTRIC"
    print("\t\t.type2 = TYPE_" + data[8]+",") #type 2

    print("\t\t.catchRate =" + data[9]+",") #catch rate
    print("\t\t.expYield =" + data[10]+",") #base exp

    print("\t\t.evYield_HP = 0,")
    print("\t\t.evYield_Attack = 0,")
    print("\t\t.evYield_Defense = 0,")
    print("\t\t.evYield_Speed = 0,")
    print("\t\t.evYield_SpAttack = 0,")
    print("\t\t.evYield_SpDefense = 0,")
    #data[11] #evs

    if data[12] == " ????????":
        data[12] = " NONE"
    print("\t\t.itemCommon = ITEM_"+data[12][1:].replace(" ","_").replace('"','') + ",") #wild held 1
    if data[13] == " ????????":
        data[13] = " NONE"
    
    print("\t\t.itemRare = ITEM_"+data[13][1:].replace(" ","_").replace('"','').replace("'","") + ",") #wild held 2
    print("\t\t.genderRatio ="+data[14]+",") #gender ratio
    print("\t\t.eggCycles ="+data[15]+",") #steps to hatch
    print("\t\t.friendship ="+data[16]+",") #base happiness
    
    expdict = {
        " 0": "GROWTH_MEDIUM_FAST",
        " 1": "GROWTH_ERRATIC",
        " 2": "GROWTH_FLUCTUATING",
        " 3": "GROWTH_MEDIUM_SLOW",
        " 4": "GROWTH_FAST",
        " 5": "GROWTH_SLOW",
    }
    print("\t\t.growthRate = "+expdict[data[17]] +",") #exp curve

    egggroupdict = {
        " 0": "EGG_GROUP_NONE",
        " 1": "EGG_GROUP_MONSTER",
        " 2": "EGG_GROUP_WATER_1",
        " 3": "EGG_GROUP_BUG",
        " 4": "EGG_GROUP_FLYING",
        " 5": "EGG_GROUP_FIELD",
        " 6": "EGG_GROUP_FAIRY",
        " 7": "EGG_GROUP_GRASS",
        " 8": "EGG_GROUP_HUMAN_LIKE",
        " 9": "EGG_GROUP_WATER_3",
        " 10": "EGG_GROUP_MINERAL",
        " 11": "EGG_GROUP_AMORPHOUS",
        " 12": "EGG_GROUP_WATER_2",
        " 13": "EGG_GROUP_DITTO",
        " 14": "EGG_GROUP_DRAGON",
        " 15": "EGG_GROUP_UNDISCOVERED",
    }
    print("\t\t.eggGroup1 = "+egggroupdict[data[18]] +",") #egg group 1
    print("\t\t.eggGroup2 = "+egggroupdict[data[19]] +",") #egg group 2
    print("\t\t.abilities = {ABILITY_"+data[20][1:].replace('"', "").replace(" ","_")+ ", "+"ABILITY_"+data[20][1:].replace('"', "").replace(" ","_")+ "}," ) #ability 1 and 2
    print("\t\t.safariZoneFleeRate ="+data[22]+",") #run rate

    colordict = {
        " 0": "BODY_COLOR_RED",
        " 1": "BODY_COLOR_BLUE",
        " 2": "BODY_COLOR_YELLOW",
        " 3": "BODY_COLOR_GREEN",
        " 4": "BODY_COLOR_BLACK",
        " 5": "BODY_COLOR_BROWN",
        " 6": "BODY_COLOR_PURPLE",
        " 7": "BODY_COLOR_GRAY",
        " 8": "BODY_COLOR_WHITE",
        " 9": "BODY_COLOR_PINK",
        " 128": "BODY_COLOR_RED",
        " 129": "BODY_COLOR_BLUE",
        " 130": "BODY_COLOR_YELLOW",
        " 131": "BODY_COLOR_GREEN",
        " 132": "BODY_COLOR_BLACK",
        " 133": "BODY_COLOR_BROWN",
        " 134": "BODY_COLOR_PURPLE",
        " 135": "BODY_COLOR_GRAY",
        " 136": "BODY_COLOR_WHITE",
        " 137": "BODY_COLOR_PINK",
    }
    print("\t\t.bodyColor = "+colordict[data[23]]+",") #body color
    print("\t\t.noFlip ="+data[24].replace("\n","")+",") #noFlip
    print("\t},")
print("};")