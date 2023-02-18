import matplotlib.pyplot as plt
import re

with open("result_BranchMisses", 'r') as branchmisses:
	count = 0

	x = []
	y = []
	for line in branchmisses:
		if count%12==0:
			x.append(int(re.search(r'\d+', line).group()))
		if count%12==1:
			y.append(int(re.search(r'\d+', line).group()))
		count+=1

plt.scatter(x,y, c = 'red')
plt.savefig("BranchMisses.svg")
