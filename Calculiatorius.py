def kelimas_laipsniu(numeris, kelimas):  # laipsnio kelimo funkcija
    resultatas = 1
    for index in range(kelimas):
        resultatas = resultatas * numeris
    return resultatas


print("WELCOME TO THE BEST BASIC CALCULATOR!!!")
# pradinis funkcijos pasirikimas kuris mus ikelia i loop
op = input("Pasirinkite funkcija (+ - / * laipsnis) arba exit iseiti: ")

while op != "exit":  # pagrindinis loopas iki kol neparaso zmogus exit
    if op == "+":
        try:  # apsauga nuo raidziu ivedimo
            num1 = float(input("pasirinkote sudeti pirmas skaicius: "))
            num2 = float(input("pasirinkote sudeti antras skaicius: "))
            print("resultatas = ", num1, "+", num2, " = ", num1 + num2)
            op = input("Pasirinkite funkcija (+ - / * laipsnis) arba exit iseiti: ")
        except ValueError:
            print("Ivesti neteisingi duomenys!!! Naudokite skaicius!")
    elif op == "-":
        try:
            num1 = float(input("pasirinkote atimti pirmas skaicius: "))
            num2 = float(input("pasirinkote atimti antras skaicius: "))
            print("resultatas = ", num1, "-", num2, " = ", num1 - num2)
            op = input("Pasirinkite funkcija (+ - / * laipsnis) arba exit iseiti: ")
        except ValueError:
            print("Ivesti neteisingi duomenys!!! Naudokite skaicius!")
    elif op == "/":
        try:
            num1 = float(input("pasirinkote dalyba pirmas skaicius: "))
            num2 = float(input("pasirinkote dalyba antras skaicius: "))

            try:  # try kad suhandlint dalyba is nulio
                print("resultatas = ", num1, "/", num2, " = ", num1 / num2)
                op = input("Pasirinkite funkcija (+ - / * laipsnis) arba exit iseiti: ")
            except ZeroDivisionError:
                print("Dalyba is nulio NEGALIMA!")

        except ValueError:
            print("Ivesti neteisingi duomenys!!! Naudokite skaicius!")
    elif op == "*":
        try:
            num1 = float(input("pasirinkote daugyba pirmas skaicius: "))
            num2 = float(input("pasirinkote daugyba antras skaicius: "))
            print("resultatas = ", num1, "*", num2, " = ", num1 * num2)
            op = input("Pasirinkite funkcija (+ - / * laipsnis) arba exit iseiti: ")
        except ValueError:
            print("Ivesti neteisingi duomenys!!! Naudokite skaicius!")
    elif op == "laipsnis":
        try:
            numeris = int(input("iveskite skaiciu kuri nori kelti laipsniu "))
            kelimas = int(input("iveskite laipsni "))
            kelimas_laipsniu(numeris, kelimas)
            print("resultatas = ", numeris, "pakeltas", kelimas, "laipsniu yra" , kelimas_laipsniu(numeris, kelimas))
            op = input("Pasirinkite funkcija (+ - / * laipsnis) arba exit iseiti: ")
        except ValueError:
            print("Ivesti neteisingi duomenys!!! Naudokite skaicius!")
    else:
        op = input("Neteisinga funkcija!! \nPasirinkite funkcija (+ - / * laipsnis) arba exit iseiti: ")

print("Viso gero!")  # Exit text
exit(0)
