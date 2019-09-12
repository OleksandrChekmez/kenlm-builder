if [ "$1" != "" ]; then
	input_dir="$(dirname "$1")"
	filename_without_extension=$(basename $1 | cut -d. -f1)
    #cat data/$1 | python3 process_from_output.py | ~/mosesdecoder/bin/lmplz -o 3 > results/$(echo $1| cut -d'.' -f 1).arpa
    python3 process_from_csv.py $1 | ~/mosesdecoder/bin/lmplz -o 3 > results/$filename_without_extension.arpa
#    python3 process.py data/$1 | ~/mosesdecoder/bin/lmplz --discount_fallback -S 70% -o 3 > $(echo $1| cut -d'.' -f 1).arpa
    #~/mosesdecoder/bin/query lm_csr_64k_vp_3gram.klm <beverly.csv
	~/mosesdecoder/bin/build_binary results/$filename_without_extension.arpa results/$filename_without_extension.klm
else
    echo "Parameter 1 is empty. Usage usage ./build.sh <text_file>"
fi

