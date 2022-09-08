#!/usr/bin/env python
from __future__ import print_function

# Using readlines()
file1 = open("material_color_list.txt", "r")
Lines = file1.readlines()

readmefile = open("README.md", "w")
count = 0
# Strips the newline character
for line in Lines:
    name = line.split(" ")[0].strip() + ".svg"
    hex = line.split(" ")[1].strip()
    r = int(hex[1:3], 16) / 255.0
    g = int(hex[3:5], 16) / 255.0
    b = int(hex[5:7], 16) / 255.0
    if ("_100" in name) or ("_500" in name) or ("_900" in name):
        count += 1
        f = open(name, "w")
        f.write('<svg id="a" data-name="a" xmlns="http://www.w3.org/2000/svg" height="40" width="40">')
        f.write('<defs><style>.st1{fill:%s;}</style></defs><rect class="st1" x="0" y="0" width="40" height="40"/></svg>' %(hex))
        f.close()
        if ("_500" in name):
            readmefile.write('<img src="%s"> %.2f %.2f %.2f [%s] ' % (name, r, g, b, name[:-4]))
        else:
            readmefile.write('<img src="%s"> %.2f %.2f %.2f ' % (name, r, g, b))
        if (count % 3 == 0):
            readmefile.write('\n\n')
