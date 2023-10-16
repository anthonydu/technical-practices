# read the string filename
filename = input()

count = 0
total = 0

with open(filename, "r") as f:
    lines = f.readlines()
    for line in lines:
        bytes = int(line.split(" ")[-1])
        if bytes > 5000:
            count += 1
            total += bytes

with open("bytes_" + filename, "w") as f:
    f.write(str(count) + "\n" + str(total))