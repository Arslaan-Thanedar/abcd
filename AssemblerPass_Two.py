import pickle
#Execute pass1 Before Executing pass2 assembler
#From python 3.6+ Dictionaries are ordered so we can index on keys to get respective Memory Address for SYMBOL_TBL and LITERAl_TBl 
file = open("pass1","rb")
data = pickle.load(file)
LITERAl_TBl = data["LITERAl_TBl"] 
POOL_TBL = data["POOL_TBL"]
SYMBOL_TBL = data["SYMBOL_TBL"]
Program = data["Program"]
Output = data["Output"]
###############################################
def Type_Helper(arg):
    if arg[0] == "L":
        return LITERAl_TBl[list(LITERAl_TBl.keys())[arg[1]]][0]
    if arg[0] == "S":
        return SYMBOL_TBL[list(SYMBOL_TBL.keys())[arg[1]]][0]
    if arg[0] == "C":
        return arg[1]
###############################################
machine_Code = ""
for statement in Output:
    line_ = ""
    if statement[0][0] == "S":
        #No need to generate machine code for label
        statement = statement[1:]
    if statement[0][0] == "IS":
        line_ += f"0{statement[0][1]} 0{statement[1][1]} {Type_Helper(statement[2])}\n"
    #Below Statements checks for the Ltorg Constant
    if statement[0] == ("AD","5"):
        line_ += f"00 00 {statement[-1][1][1:-1]}\n"
    if statement[0][0] == "AD":
        line_ += f"00 00 {statement[0][1]}\n"
    machine_Code+=line_
print(machine_Code)
file = open("pass2Output.txt","w")
file.write(machine_Code)
file.close()
