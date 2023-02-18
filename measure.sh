#!/bin/bash

cargo init
echo "perfcnt = \"0.8.0\"" >> Cargo.toml

declare -a counters=("CPUCycles" "Instructions" "BranchMisses")
declare -a blocksizes=("8" "16" "32" "64")
for counter in "${counters[@]}"
do
	RESULT="./result_$counter"
	> $RESULT
	
	for i in {1..20}
	do
		blocknumber=$((i*512))
		for blocksize in "${blocksizes[@]}"
		do
			echo "$blocknumber $blocksize" >> $RESULT
			python3 genere_code.py $blocknumber $blocksize $counter
			cargo build --release
			sudo ./target/release/fff67 >> $RESULT
		done
		
	done
done

#python3 draw.py

echo "the end"
