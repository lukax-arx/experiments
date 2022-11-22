print("Hallo ich Bin calli")
print("Ich rechne für dich")

Zahl1=int(input("1. Zahl: "))
Zahl2=int(input("2. Zahl: "))
Rechenzeichen=input("Addieren? (+), Subtrahieren? (-), Multiplizieren? (*), Dividieren? (/): ")
Ergebnis=0
if Rechenzeichen=="+":
    Ergebnis=Zahl1+Zahl2
if Rechenzeichen=="-":
    Ergebnis=Zahl1-Zahl2
if Rechenzeichen=="*":
    Ergebnis=Zahl1*Zahl2
if Rechenzeichen=="/":
    Ergebnis=Zahl1/Zahl2

print("Ergebnis:", Ergebnis)




