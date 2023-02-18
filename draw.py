import matplotlib.pyplot as plt
import re

color_and_xs_and_ys = {'8':('red',[],[]),'16':('blue',[],[]),'32':('orange',[],[]),'64':('green',[],[])}

with open("result_BranchMisses", 'r') as branchmisses:
	count = 0
	current_block_size = 0

	for line in branchmisses:
		if count%2==0:
			numbers = re.findall(r'\d+', line)
			current_block_size=numbers[1]
			color_and_xs_and_ys[current_block_size][1].append(int(numbers[0]))
		if count%2==1:
			color_and_xs_and_ys[current_block_size][2].append(int(re.search(r'\d+', line).group()))
		count+=1

for (color,x,y) in color_and_xs_and_ys.values():
	plt.scatter(x,y, c = color)

plt.savefig("BranchMisses.svg")
