import os

NucF = [0] * 4
x=0

with open('Datasets/Ebola.txt') as f1:
    for line in f1:
        for i in range(len(line)):
              x+=1
              if line[i] == 'A':
                    NucF[0] += 1  # line2[i]:
              elif line[i] == 'C':
                    NucF[1] += 1
              elif line[i] == 'G':
                   NucF[2] += 1  # a+T/C+G 0+3/1+2
              elif line[i] == 'T':
                    NucF[3] += 1

y = NucF[1] + NucF[2]
z = NucF[0] + NucF[1] + NucF[2] + NucF[3]
cgcontent = y / z
print('CGcontent:', cgcontent)
print('AT/GC ratio:', (NucF[0]+NucF[3])/(NucF[1]+NucF[2]))