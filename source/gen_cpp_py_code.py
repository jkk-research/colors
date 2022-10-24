#!/usr/bin/env python
from __future__ import print_function

# Using readlines()
file1 = open("material_color_list.txt", "r")
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
    name = line.split(" ")[0].strip() + ".svg"
    hex = line.split(" ")[1].strip()
    r = int(hex[1:3], 16) / 255.0
    g = int(hex[3:5], 16) / 255.0
    b = int(hex[5:7], 16) / 255.0
    if ("_500" in name) or ("_500" in name) or ("_500" in name):
        count += 1
        #print(count)
        #print("const float %s_r = %.2f, %s_g = %.2f, %s_b = %.2f;" % (name[:-4], r, name[:-4], g, name[:-4], b))
        print("%s_r = %.2f, %s_g = %.2f, %s_b = %.2f" % (name[:-4], r, name[:-4], g, name[:-4], b))
        #print("%s = {%.0f, %.0f, %.0f}" % (name[:-4], r * 255, g *255,  b * 255))
        #print("{%.0f, %.0f, %.0f}, " % (r * 255, g *255,  b * 255))
