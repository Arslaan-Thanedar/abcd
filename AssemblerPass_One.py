import pickle 
Program = """
START 100
MOVER AREG "4"
MOVEM BREG A
MOVER BREG "1"
LOOP MOVER CREG B
LTORG
ADD CREG "6"
STOP
A DS 1
B DS 1
END 
""".strip().split("\n")
Opcode_Table= {
    'STOP': ['0', 'IS', 0],
    'ADD': ['1', 'IS', 2],
    'SUB': ['2', 'IS', 2],
    'MUL': ['3', 'IS', 2],
    'MOVER': ['4', 'IS', 2],
    'MOVEM': ['5', 'IS', 2],
    'COMP': ['6', 'IS', 2],
    'BC': ['7', 'IS', 2],
    'DIV': ['8', 'IS', 2],
    'READ': ['9', 'IS', 1],
    'PRINT': ['10', 'IS', 1],
    'LTORG': ['5', 'AD', 0],
    'ORIGIN': ['3', 'AD', 1],
    'START': ['1', 'AD', 1],
    'DS': ['1', 'DL', 1],
    'DC': ['2', 'DL', 1],
    'END': ['AD', 0],
    "AREG":"1",
    "BREG":"2",
    "CREG":"3"
    }
######################
Base_Address = int(Program[0].split(" ")[1])
Current_LTORG = 0
LTORG_QUE = []
POOL_TBL =  []
SYMBOL_TBL = {}
LITERAl_TBl = {}
#######################
#Some Helper Function 
def LTORG_HELPER(adress):
    POOL_TBL.append(len(LITERAl_TBl.keys()))
    for element in LTORG_QUE:
        if element not in LITERAl_TBl:
            LITERAl_TBl[element] = [adress,len(LITERAl_TBl.keys())]
            adress += 1 ;
def TYPE_HELPER(arg):
    if arg.isnumeric():
        return ["C",arg]
    if arg[0]=="\"":
        return ["L",LITERAl_TBl[arg][1]]
    return ["S",SYMBOL_TBL[arg][1]]
#Filling Tables Here 
for statement in Program[1:]:
    statement = statement.split(" ")
    if statement[0] not in Opcode_Table.keys():
        SYMBOL_TBL[statement[0]] = [Base_Address,len(SYMBOL_TBL.keys())]
        statement = statement[1:]
    if statement[0] in ["LTORG","END"]:
        LTORG_HELPER(Base_Address)
    if statement[0] in ["MOVEM","MOVER","ADD","SUB","MUL","DIV"]:
        if statement[2][0]=="\"":
            LTORG_QUE.append(statement[2])
    Base_Address+=1
#Preparing The Output Here;
Number_of_LTORG = 0;
Output = []
Base_Address = int(Program[0].split(" ")[1])
for statement in Program[1:]:
    statement = statement.split(" ")
    line = []
    if statement[0] not in Opcode_Table.keys():
        line.append(("S",SYMBOL_TBL[statement[0]][1]))
        statement = statement[1:]
    if statement[0] in ["LTORG","END","STOP"]:
        if statement[0]=="END":
            continue
        line.append(("AD",Opcode_Table[statement[0]][0]))
        #You can Ignore the below statement if u dont care about showing the constants 
        if statement[0]=="LTORG":
            line+=[("C",list(LITERAl_TBl.keys())[i]) for i in range(POOL_TBL[Number_of_LTORG],POOL_TBL[Number_of_LTORG+1])]
    if statement[0] in  ["MOVEM","MOVER","ADD","SUB","MUL","DIV"]:
        line += [("IS",Opcode_Table[statement[0]][0]),("RG",Opcode_Table[statement[1]]),(TYPE_HELPER(statement[2])[0],TYPE_HELPER(statement[2])[1])]
    if statement[0] in ["DS","DC"]:
        line += [("DL",Opcode_Table[statement[0]][0]),(TYPE_HELPER(statement[1])[0],TYPE_HELPER(statement[1])[1])]
    Output.append(line)
print("SYMBOL_TBL=",SYMBOL_TBL)
print("LITERAl_TBl=",LITERAl_TBl)
print("Output=","\n".join(["".join([str(j) for j in i]) for i in Output]))


#Saving the output here u can ignore if u dont care about other half 
file = open("pass1","wb")
save = pickle.Pickler(file)
save.dump({
        "POOL_TBL":POOL_TBL,
        "SYMBOL_TBL":SYMBOL_TBL,
        "LITERAl_TBl":LITERAl_TBl,
        "Program":Program,
        "Output":Output
        })
file.close()
