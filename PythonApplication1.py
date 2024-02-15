try:
    print("Tere! Olen sinu uus sõber — Python!")
    nimi=input("Mis on sinu nimi on? ")
    print(nimi,",oi kui ilus nimi!")
    indeks=input(nimi+" Kas leian Sinu keha indeksi? 0-ei, 1-jah=")
    if indeks=="1":
        pikkus=int(input(nimi+",Sinu pikkus(cm=>)"))
        mass=float(input("Mis on sinu kaal? "))
        indeks=mass/(0.01*pikkus)**2
        print(nimi+"! Sinu keha indeks on:",round(indeks,1))
        if indeks<16:
            print("Tervisele ohtlik alakaal")
        elif 16<indeks<19:
             print("Alakaal")
        elif 19<indeks<25:
            print("Normaalkaal")
        elif 25<indeks<30:
            print("Ülekaal")
        elif 30<indeks<35:
            print("Rasvumine")
        elif 35<indeks<40:
            print("Tugev rasvumine")
        elif 40>indeks:
             print("Tervisele ohtlik rasvamine")
        elif indeks =="0":
            print("Kahju! See on väga kasulik info")
            print(" ")
            print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")
#try:
    #print("Ainult arvud!")
except:
    print("ValueError")






print("Tere! Olen sinu uus sõber — Python!")
nimi=input("Mis on sinu nimi on?")
print(nimi,",oi kui ilus nimi!")
indeks=input(nimi+"Kas leian Sinu keha indeksi? 0-ei, 1-jah=")
if indeks=="1":
     pikkus=int(input(nimi+",Sinu pikkus(cm=>)"))
     mass=float(input("Mis on sinu kaal? "))
     indeks=mass/(0.01*pikkus)**2
     print(nimi+"!Sinu keha indeks on:",round(indeks,1))
     if indeks<16:
        print("Tervisele ohtlik alakaal")
     elif 16<indeks<19:
             print("Alakaal")
     elif 19<indeks<25:
        print("Normaalkaal")
     elif 25<indeks<30:
        print("Ülekaal")
     elif 30<indeks<35:
        print("Rasvumine")
     elif 35<indeks<40:
        print("Tugev rasvumine")
     elif 40>indeks:
        print("Tervisele ohtlik rasvamine")
elif indeks=="0":
    print("Kahju! See on väga kasulik info")
    print(" ")
    print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")