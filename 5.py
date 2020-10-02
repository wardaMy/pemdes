def main ():
    ulang=0
    salah=0
    print ("*************************************************\n"
           "                SILAHKAN LOGIN\n"
           "*************************************************\n")
    while ulang<3:
        username=(input("Username : "))
        password=(input("Password : "))
        if username=="warda" and password=="infor":
            print ("Selamat anda berhasil masuk")
        else:
            print ("Maaf Username/Password anda salah")
            salah=salah+1
            if salah==3:
                print ("Anda sudah 3 kali salah, coba lagi nanti")
        ulang=ulang+1
main()

  

