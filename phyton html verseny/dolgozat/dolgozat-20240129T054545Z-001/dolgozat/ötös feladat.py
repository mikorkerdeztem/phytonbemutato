valasz = input("Adj meg egy szót (tömeg/sorozat/tszám): ")

if valasz == "tömeg":
    tomeg = float(input("Add meg a testtömeged: "))
    if tomeg > 60:
        print("Le kell fogynod!")
elif valasz == "sorozat":
    for i in range(30, 143, 7):
        print(i)
elif valasz == "tszám":
    tszam = float(input("Add meg a tizedes törtet: "))
    kerekitett = round(tszam, 3)
    print(kerekitett)
else:
    print(["tömeg", "sorozat", "tszám"], ": ezekből kellett volna választanod")
