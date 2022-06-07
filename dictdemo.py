cources={"DBDA":120,"DAC":240}
print(cources)
print(cources["DBDA"]) #RETRIVE THE VALUES
cources["DBDA"]=150 #overwrite the value
cources["DHPCSA"]=10 #add new key in dictionary
print(cources)

for k in cources.keys():  #gives < values
    if(cources[k])<100:
        print(f"{k}---{cources[k]}")

for k in cources.keys(): #gives > values
    if(cources[k])>100:
        print(f"{k}---{cources[k]}")

for k,v in cources.items(): #[(DBDA,120),(DAC,240),()]
    if(v)<100:
        print(f"{k}---{v}")