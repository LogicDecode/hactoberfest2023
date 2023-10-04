for file in *.txt; do
    mv "$file" "${file%.txt}_1.txt"
done
