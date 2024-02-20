import json
file = open(r"C:\Users\Asus\Desktop\pp2\lab4\json\ex.json")
x = json.loads(file.read())


dn = []
for i in range(len(x["imdata"])):
    dn.append(x["imdata"][i]["l1PhysIf"]["attributes"]["dn"])

speed = []
for i in range(len(x["imdata"])):
    speed.append(x["imdata"][i]["l1PhysIf"]["attributes"]["fecMode"])

mtu = []
for i in range(len(x["imdata"])):
    mtu.append(x["imdata"][i]["l1PhysIf"]["attributes"]["mtu"])



print(f"""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")
for i in range(len(x["imdata"])):
    print(dn[i], "\t"*3, "      ", speed[i], " ", mtu[i])