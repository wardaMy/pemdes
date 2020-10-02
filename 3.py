loop = "y"
while loop == "y":
    print ("          MENGHITUNG BMI          ")
    print ("  ________________________________ \n",
           "|___BMI___|__STATUS BERAT BADAN__|\n",
           "|  <18.5  |Kekurangan Berat Badan|\n",
           "|18.5-24.9|    Normal (Ideal)    |\n",
           "|25.0-29.9| Kelebihan Berat Badan|\n",
           "|__>=30.0_|_Kegemukan (Obesitas)_|\n",
           "                                  ")
    B=float(input ("Berat Badan(Kg) = "))
    T=float(input("Tinggi Badan(M) = "))
    BMI=B/(T**2)
    if BMI<18.5:
        print ("BMI    :", BMI)
        print ("Status : Kekurangan Berat Badan")
    elif 18.5<=BMI<=24.9:
        print ("BMI    :", BMI)
        print ("Status : Normal (Ideal)")
    elif 25.0<=BMI<=29.9:
        print ("BMI    :", BMI)
        print ("Status : Kelebihan Berat Badan")
    elif BMI>=30.0 :
        print ("BMI    :", BMI)
        print ("Status : Kegemukan (Obesitas)")
    else :
        print ("Periksa kembali inputan anda")

    loop = str(input("Ingin coba lagi?(enter 'y' jika iya): "))

    

