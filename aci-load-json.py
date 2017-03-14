import json

fout = open('ACIGroups-csv.txt', 'w')  # open a new file for write


fname = open("ACI-groups.json", "r")
jfile = fname.read()
# print jfile

info = json.loads(jfile)
for headers in info:
    print headers

print "************************"
STR = "Consumer" + "~" + "Provider" + "~" + "Protocol#"+ "~" + "Start_Port#"+ "~" + "End_Port#"
fout.write(STR)
fout.write("\n")

# Write CSV files for Consumer and Provider EPG
for item in info["policies"]:
            Consumer = item["src_name"]
            Provider = item['dst_name']
            for port in item["whitelist"]:
                Proto = port["proto"]
                Port = port["port"]
                STR = Consumer + "~" + Provider + "~" + str(Proto)+ "~" + str(Port[0])+ "~" + str(Port[1])
                print STR
                fout.write(STR)
                fout.write("\n")

for i in range(0,5):
    fout.write("\n")

STR1 = "EPG" + "~" + "IPADD"
fout.write(STR1)
fout.write("\n")


for item in info["clusters"]:
          EPG = item["name"]
          for node in item["nodes"]:
            IPADD = node["ip"]
            STR1 = EPG + "~" + IPADD
            print STR1
            fout.write(STR1)
            fout.write("\n")

