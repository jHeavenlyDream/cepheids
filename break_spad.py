#разибка спад архива tracemode поканально
import re

#Список файлов
#оригинальный файл предварительно разбил командой split
files = ['xaa', 'xab', 'xac', 'xad']
series = {}

for file in files:
    print("read: " + file)
    #parse
    #with open(file, 'r', encoding='utf-8) as f:
    with open(file, 'r') as f:
        for line in f:
            sep = re.split(' ', line)
            sep = ' '.join(sep).split()
            sep.pop()
            l = len(sep)
            name = ' '.join(sep[0:len(sep)-3])
            if name in series:
                series[name].append([sep[l-3], sep[l-2], sep[l-1]])
            else:
                series[name] = []
                series[name].append([sep[l-3], sep[l-2], sep[l-1]])

    #write
    names = list(series.keys())
    print("write")
    #print(names)
    for name in names:
        filename = (name+".txt").replace(" ", "_").replace("<", "").replace(">", "")
        with open(filename, "a", encoding='ISO-8859-1') as fp:
            for values in series[name]:
                  #fp.write(';'.join(values) + "\n")
                  fp.write(values[0] + " " + values[1] + ";" + values[2]+ "\n")
    series.clear()
