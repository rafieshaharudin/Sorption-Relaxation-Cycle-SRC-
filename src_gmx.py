# Aim : To compile number of water molecules from each MD SRC cycle

import os
from tkinter import Tcl


f99 = open('SRC_MD', 'w')
f99.write('# time(ps)   Zbox(nm)\n ')

# open empty list to append collected data later

file_list = []
Z_list = []
t_list = []
count = 0

# find file in  directory that ends with ".xvg" and sort in correct sequence (require correct address location)

for filename in os.listdir('/mnt/iusers01/ceas01/mjki4ms3/scratch-new/reverse_SRC/SRC_minim/highRH/cont_500_cycles/data_analysis'):
	if filename.endswith('.xvg'):
		file_list.append(filename)
		new_list = Tcl().call('lsort', '-dict', file_list)

# collect data from sorted Z*.xvg file and update time step

for file in new_list:
	f = open(file).readlines()[25:]
	for line in f:
		s = line.split()
		Z_list.append(s[1])
		count += 0.1
		t_list.append(count)

# write collected data into one file for futher analysis

for i, j in zip(t_list, Z_list):
 f99.write(str("%10.4f" % float(i)) + str("%12.6f\n" % float(j)))

f99.close()

exit
