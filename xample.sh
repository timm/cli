out=${0%.*}.out
cat<<EOF|while read -r x;do printf "\n#-------\n%% $x\n";$x;done|cat -n> $out
python3 xample.py -h
python3 xample.py
python3 xample.py -w vic
python3 xample.py -s 1000
EOF
cat $out
