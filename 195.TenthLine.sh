# Read from the file file.txt and output the tenth line to stdout.
#if [ `wc -l < file.txt` -ge 10 ];
#then 
    #head -10 file.txt | tail -1
    #sed -n 10p file.txt
    #awk "NR==10" file.txt
#else 
#    echo ""
#fi
i=0
while [ $i -lt 10 ] && read line;
do
    ((i++))
    if [ $i -eq 10 ];
    then
        echo $line
    fi
done < file.txt
    
    
