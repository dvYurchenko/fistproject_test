#Задание 1
file = 'C:/Users/Little/Desktop/Юрченко Дарья/text_2.txt'
file_1 = 'C:/Users/Little/Desktop/Юрченко Дарья/text_3.txt'
#stream = open(file, mode='r', encoding=None)
#stream_1 = open(file_1, mode='r', encoding=None)

#line_1 = stream_1.readline()
#line = stream.readline()
#while line != '':
    #for ch in line:
        #words = ch.split()
empty_set = set()
with open(file_1,'r') as file_1:
    content = file_1.read()
    words = content.split()
    for word in words:
        empty_set.add(word)
with open(file,'r') as file:
    content = file.read()
    words = content.split()
    with open("fail_3.txt", 'w') as file_3:
        for word in words:
            if word not in empty_set:
                file_3.write(word + ' ')