import sys
import csv

fd_out_name = sys.argv[1]
import csv
fd_out = open(fd_out_name, "w")
w1 = [] 
w2 = []
w3 = []
with open('sentimentlex.csv', "r") as csvfile:
    reader = csv.DictReader(csvfile)

    # State words
    for row in reader:
        #print(row.keys())
        if " " in row['\xef\xbb\xbf"word"']:
            continue
        w1.append("word(\"" + row['\xef\xbb\xbf"word"'] + "\")" + ".\n")
        w2.append("word_class(\"" + row['\xef\xbb\xbf"word"'] + "\", " + row['part_of_speech'] + ")" + ".\n")
        w3.append("word_strength(\"" + row['\xef\xbb\xbf"word"'] + "\", " + row['strength'] + ")" + ".\n")

for i in range(len(w1)):
    fd_out.write(w1[i])

for i in range(len(w2)):
    fd_out.write(w2[i])

for i in range(len(w3)):
    fd_out.write(w3[i])


fd_out.close()
