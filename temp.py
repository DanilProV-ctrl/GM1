from time import sleep

print('gamburg ' * 3)
i = 0
while i < 10:
    sleep(0.5)
    print(i)
    i += 1
    if i > 10:
        break

j = 0
print('second try; ' * 3)
for j in range(20):
   sleep(0.1) 
   print(j)
   continue

c = 0
print('third try; ' * 3)
for c in 1,2,3:
    print(c)


print('if/else ' * 3)
if i == 9:
    print('NS')
elif i == 10:
    print('NSS')
elif i != 9:
        print('MN')
else:
    print("NO")

    #range(10) - povtor 10 raz
    #continue - cnova, break - vihod
