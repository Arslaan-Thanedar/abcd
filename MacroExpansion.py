import re
program = """
START 100
MOVER AREG 10
INCR MACRO &X,&Y,&Z
MOVER AREG "5"
ADD AREG &X
MULT AREG &Y
MOVEM AREG &Z
MEND
DEMO MACRO &X,&M
MOVEM AREG &M
MEND
INCR A,B,C
DEMO DANISH,SHADAB
ADD AREG 10
""".strip().split("\n")
idx = 0 ;
keywords = ["MOVEM","MOVER","ADD","MULT","MEND","DIV","CMP","JNZ","STOP","END","START"];
NAMTAB_AND_DEFTAB = {}
while idx<program.__len__():
    statement = program[idx].split(" ")
    #Macro Record Here
    if statement[0] not in keywords and statement[1] == "MACRO":
        #Processing Begins Here
        params = statement[2].split(",")
        NAMTAB_AND_DEFTAB[statement[0]] = {
                "params":params,
                }
        idx = idx + 1;
        defination = ""
        while True:
            if program[idx] == "MEND":
                idx = idx + 1 ;
                break
            defination += (program[idx]+"\n")
            idx = idx + 1;
        NAMTAB_AND_DEFTAB[statement[0]]["defination"] = defination;
    if statement[0] not in keywords and statement[1] != "MACRO":
        exchange = {i:j for i , j in zip(NAMTAB_AND_DEFTAB[statement[0]]["params"],statement[1].split(","))}
        final = NAMTAB_AND_DEFTAB[statement[0]]["defination"];
        for keys in exchange:
            final = final.replace(keys,exchange[keys]);
        program[idx] = final;
        idx = idx + 1;
    if statement[0] in keywords:
        program[idx] = " ".join(statement)+"\n"
        idx  = idx + 1
program = "".join(program)
print(f"NAMTAB=>\n{[name for name in NAMTAB_AND_DEFTAB.keys()]}\n")
print(f"DEFTAB=>\n{[str(defination)+'=>'+NAMTAB_AND_DEFTAB[defination]['defination'] for defination in NAMTAB_AND_DEFTAB.keys()]}\n")
print("Expanded Program=>\n",re.sub("([A-Z]*) MACRO((.|\n)*)MEND","\n",program))
