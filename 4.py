no=[]
angka = int(input("Masukkan panjang deret!"))
for w in range (angka):
    no.append(int(input("masukkan angka=")))
for i in range (0,len(no)-1):
    min = i
    for j in range (i+1, len (no)):
        if no[j] < no [min]:
            min = j
    temp = no[i]
    no[i] = no [min]
    no[min]= temp
    
i=0
max=no[0]
min=no[0]
for i in range (i,len(no)-1):
    i = i+1
    if(no[i]>max):
        max=no[i]
    elif(no[i]<min):
        min=no[i]
print ("Deret =",no)
print ("Nilai minimal =", min)
print("Nilai maksimal =",max)


