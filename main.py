import logging
import sys
logging.basicConfig(level=logging.DEBUG)

def kalkulator():
    try:
        operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
    except ValueError:
        logging.error("Nieprawidłowa wartość argumentu działania: %s" % operation)
        sys.exit(1)
    if operation < 1 or operation > 4:
        logging.error("Podaj właściwą wartość cyfry działania")
        sys.exit(1)
    a = input("Podaj wartość pierwszej liczby:")
    try:
        a = float(a)
    except ValueError:
        logging.error("Nieprawidłowa wartość pierwszej liczby: %s" %a)
        sys.exit(1)
    
    b = input("Podaj wartość drugiej liczby:")
    try:
        b = float(b)
    except ValueError:
        logging.error("Nieprawidłowa wartość drugiej liczby: %s" % b)

    if operation == 1: #operacja dodawania
        additive = a+b
        sign = ""
        while sign != "=":
            sign = input("Podawaj liczby, wciśnij \"=\" by zsumować:")
            try:
                additive = additive + float(sign)
            except ValueError:
                logging.info("Suma wynosi %.2f"%additive)
                sys.exit(1)
        logging.info("Suma wynosi %.2f"%additive)


        logging.info("Dodaję %.2f i %.2f" % (a,b))
        print ("Wynik to %.2f" % (a+b))

    elif operation == 2: #operacja odejmowania
        logging.info("Odejmuję liczby %.2f i %.2f" % (a,b))
        print ("Wynik to %.2f" % (a-b))

    elif operation == 3: #operacja mnożenia
        multiplying = a*b
        sign = ""
        while sign != "=":
            sign = input("Podawaj liczby, wciśnij \"=\" żeby wymnożyć:")
            try:
                sign = float(sign)
                multiplying *= sign
            except ValueError:
                logging.info("Wynik mnożenia wynosi %.2f"%multiplying)
        print("Wynik to %.2f" % multiplying)

    elif operation == 4: #operacja dzielenia
        logging.info("Dzielę %.2f przez %.2f" % (a,b))
        print("Wynik to %.2f" % (a/b))
    else:
        logging.error("Podaj prawidłową wartość!")
        exit(1)
    
print(kalkulator())