fhand = open('romeo.txt')
word_list = list()
for line in fhand:
    #print(line.rstrip())
    words = line.split()
    for word in words:
        if word not in word_list:      
            word_list.append(word)    
word_list.sort()
print(word_list)