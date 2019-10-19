import sys

fd_out_name = sys.argv[1]

fd = open("sentimentlex.csv", "r")
fd_out = open(fd_out_name, "w")
lines = fd.readlines()[1:]

# State words
for line in lines:
    word = line.split(",")[0]
    if " " in word:
        continue
    fd_out.write("word(" + word + ")" + ".\n")


# State word and its wordclass
#wcl = []
for line in lines:
    word = line.split(",")[0]
    word_class = line.split(",")[5].replace("\"", "")
    # if word_class not in wcl:
    #     wcl.append(word_class)
    if " " in word:
        continue
    fd_out.write("word_class(" + word + ", " + word_class + ")" + ".\n")

# for i in wcl:
#     print(i)


# State words and its strengts
for line in lines:
    word = line.split(",")[0]
    if " " in word:
        continue
    strength = line.split(",")[2]
    fd_out.write("word_strength(" + word + ", " + strength + ")" + ".\n")


fd.close()
fd_out.close()
