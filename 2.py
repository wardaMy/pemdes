loop = "y"
while loop == "y":
    print (" ===================================================================\n",
           "                KALKULATOR BANGUN DATAR (CM)                       \n",
           "===================================================================\n") 
          
    print ("Pilih Opsi\n",
           "1. Persegi\n",
           "2. Persegi Panjang\n",
           "3. Segitiga\n",
           "4. Lingkaran\n",
           "5. Layang-layang\n",
           "6. Jajar genjang\n",
           "7. Trapesium\n"
           " 8. Belah Ketupat")
    e=int (input("Masukkan opsi :"))
    print (" ===================================================================")
    if e==1 :
        print ("PERSEGI")
        a=float(input("Sisi :"))
        b=a*a
        c=4*a
        print ("Luas = ",a," x ",a," = ",b," CM²")
        print ("Keliling = 4 x",a," = ",c," CM")
    elif e==2 :
        print ("PERSEGI PANJANG")
        a=float(input("Panjang :"))
        b=float(input("Lebar :"))
        c=a*b
        d=2*(a+b)
        print ("Luas = ",a," x ",b," = ",c,"CM²")
        print ("Keliling = 2x(",a,"+",b,") =",d,"CM")
    elif e==3 :
        print ("SEGITIGA")
        a=float(input("Alas :"))
        t=float(input("Tingi :"))
        sa=float(input("Sisi a :"))
        sb=float(input("Sisi b :"))
        sc=float(input("Sisi c :"))
        l=(a*t)/2
        k=sa+sb+sc
        print ("Luas = (",a,"x",t,")/2 = ",l," CM²")
        print ("Keliling = ",sa,"+",sb,"+",sc," = ",k," CM")
    elif e==4 :
        print ("LINGKARAN")
        r=float(input("Jari-jari :"))
        l=3.14*(r**2)
        k=2*3.14*r
        print ("Luas = 3.14x",r,"² =",l," CM²")
        print ("Keliling = 2x3.14x",r," = ",k," CM")
    elif e==5 :
        print ("LAYANG-LAYANG")
        d1=float(input("Diagonal 1 :"))
        d2=float(input("Diagonal 2 :"))
        sa=float(input("Sisi a :"))
        sb=float(input("Sisi b :"))
        sc=float(input("Sisi c :"))
        sd=float(input("Sisi d :"))
        l=(d1*d2)/2
        k=sa+sb+sc+sd
        print ("Luas = (",d1,"x",d2,")/2 = ",l," CM²")
        print ("Keliling = ",sa,"+",sb,"+",sc,"+",sd," = ",k," CM")
    elif e==6 :
        print ("JAJARGENJANG")
        a=float(input("Alas :"))
        t=float(input("Tingi :"))
        sa=float(input("Sisi a :"))
        sb=float(input("Sisi b :"))
        sc=float(input("Sisi c :"))
        sd=float(input("Sisi d :"))
        l=a*t
        k=sa+sb+sc+sd
        print ("Luas = ",a," x ",t," = ",l,"CM²")
        print ("Keliling = ",sa,"+",sb,"+",sc,"+",sd," = ",k," CM")
    elif e==7 :
        print ("TRAPESIUM")
        a=float(input("Sisi a :"))
        b=float(input("Sisi b :"))
        c=float(input("Sisi c :"))
        d=float(input("Sisi d :"))
        t=float(input("tingi :"))
        l=((a+b)*t)/2
        k=a+b+c+d
        print ("Luas = ((",a,"+",b,")x",t,")/2 =",l," CM²")
        print ("Keliling = ",a,"+",b,"+",c,"+",d," = ",k," CM")
    elif e==8 :
        d1=float(input("Diagonal 1 :"))
        d2=float(input("Diagonal 2 :"))
        sa=float(input("Sisi a :"))
        sb=float(input("Sisi b :"))
        sc=float(input("Sisi c :"))
        sd=float(input("Sisi d :"))
        l=(d1*d2)/2
        k=sa+sb+sc+sd
        print ("Luas = (",d1,"x",d2,")/2 = ",l," CM²")
        print ("Keliling = ",sa,"+",sb,"+",sc,"+",sd," = ",k," CM")
    else :
        print ("MAAF OPSI TIDAK ADA")
    loop = str(input("Ingin menghitung lagi?(enter 'y' jika iya): "))
        
