#!/usr/bin/env python

import re

#!/usr/bin/env python


fname = "events_1400_to_1600.txt"
fh = open(fname, "r")

fout = open('output-csv.txt', 'w')  # open a new file for write
STR = "Affected" + "~" + "Description" + "~" + "Created"  # create the headers
fout.write(STR)
fout.write("\n")

lst = list()
for line in fh:
    if line.startswith("affected"):
        line.rstrip()  # strip right line feeds from line
        lst1 = re.findall( ": .*", line)
        lst.append(lst1)




    if line.startswith("descr"):
        line.rstrip()
        lst2 = re.findall(": .*", line)
        lst.append(lst2)



    if line.startswith("created"):
        line.rstrip()
        lst3 = re.findall(": .*", line)
        lst.append(lst3)

        # make CSV File, once done, import into excel with delimiter ~
        STR = lst[0][0] + "~" + lst[1][0] + "~" + lst[2][0]
        print STR
        fout.write(STR)
        fout.write("\n")
        # Reinitialize list
        lst = list()

fout.close()

