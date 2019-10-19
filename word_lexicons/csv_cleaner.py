import sys

fd_out_name = sys.argv[1]

fd = open("sentimentlex.csv", "r")
fd_out = open(fd_out_name, "w")

# State words
lines = fd.readlines()[1:]
for line in lines:
    word = line.split(",")[0]#.replace("\"", "")
    if " " in word:
        continue
    # strength = line.split(",")[2]
    fd_out.write("word(" + word + ")" + ".\n")


# State words and its strengts
for line in lines:
    word = line.split(",")[0]#.replace("\"", "")
    if " " in word:
        continue
    strength = line.split(",")[2]
    fd_out.write("word_strength(" + word + ", " + strength + ")" + ".\n")
fd_out.write("word_strength(" + "_" + ", " + str(0) + ")" + ",!.\n")

fd.close()
fd_out.close()
