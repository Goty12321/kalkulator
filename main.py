import logging
logging.basicConfig(level=logging.DEBUG)

def kalkulator():
    operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
    a = float(input("Podaj wartość pierwszej liczby:"))
    b = float(input("Podaj wartość drugiej liczby:"))
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
    
print(kalkulator())