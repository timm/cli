out=${0%.*}.out
cat<<EOF|while read -r x;do printf "\n#-------\n%% $x\n";$x;done|cat -n> $out
python3 clink.py -h
python3 clink.py
python3 clink.py -w vic
python3 clink.py -s 1000
EOF
cat $out
