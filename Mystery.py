print ("Tervetuloa mysteeri luolaan! Löydätkö aarteen vai kuoletko kärmeen puremaan?")
print ("")
print ("Olet luolan suulla. Voit mennä eteenpäin, vasemmalle tai oikealle.")
print ("")
suunta = input("Mihin suuntaan haluat mennä? (eteen, vasen, oikea): ")
if suunta == "eteen":
    print ("Kävelet eteenpäin ja löydät aarteen! Onneksi olkoon!")
elif suunta == "vasen":
    print ("Kävelet vasemmalle ja astut kärmeen päälle. Kärme puraisee sinua ja kuolema seuraa.")
elif suunta == "oikea":
    print ("Kävelet oikealle ja astut ansakuoppaan. Kuolema seuraa.")
else:
    print ("Et osannut valita oikein ja kuolit.")
print ("")
print ("Peli on päättynyt.")
print ("")
print ("Kiitos pelaamisesta!")
print ("")
print ("Paina Enter lopettaaksesi.")
input()


