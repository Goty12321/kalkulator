import logging
import sys
logging.basicConfig(level=logging.DEBUG)

def kalkulator():
    
    operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))

    a = input("Podaj wartość pierwszej liczby:")
    if isinstance(a, float):
        pass
    elif isinstance(a, int):
        a = float(a)
    else:
        logging.error("Podaj właściwą wartość!")
        sys.exit(1)

    b = input("Podaj wartość drugiej liczby:")
    if isinstance(b, float):
        pass
    elif isinstance(b,int):
        b = float(b)
    else:
        logging.error("Podaj właściwą wartość!")
        sys.exit(1)

    if operation == 1: #operacja dodawania
        logging.info("Dodaję %.2f i %.2f" % (a,b))
        print ("Wynik to %.2f" % (a+b))
    elif operation == 2: #operacja odejmowania
        logging.info("Odejmuję liczby %.2f i %.2f" % (a,b))
        print ("Wynik to %.2f" % (a-b))
    elif operation == 3: #operacja mnożenia
        logging.info("Mnożę %.2f i %.2f" % (a,b))
        print("Wynik to %.2f" % (a*b))
    elif operation == 4: #operacja dzielenia
        logging.info("Dzielę %.2f przez %.2f" % (a,b))
        print("Wynik to %.2f" % (a/b))
    else:
        logging.error("Podaj prawidłową wartość!")
        exit(1)
    
print(kalkulator())