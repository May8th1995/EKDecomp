learnsets = open('learnsets.txt', 'r')
Lines = learnsets.readlines()


#This scrpt is not perfect and directly importing leads to lots of errors but allowed for a few find and replaces to make a working learnsets file.
for lines in Lines:
    if (lines[0] == "1") or (lines[0] == "2") or (lines[0] == "3") or (lines[0] == "4") or (lines[0] == "5") or (lines[0] == "6") or (lines[0] == "7") or (lines[0] == "8") or (lines[0] == "9"):
        print("static const u16 s"+ lines.split(". ")[1].split("\n")[0] + "LevelUpLearnset[] = {") #mr mime manually needs fixing
    if lines[0] == "L":
        print("\tLEVEL_UP_MOVE("+lines.split(".")[1].split(" ")[0]+", MOVE_" +lines.split(" ",1)[1].split("\n")[0].upper().replace(" ", "_") + "),")
    if lines[0] == "\n":
        print("\tLEVEL_UP_END\n};\n")
