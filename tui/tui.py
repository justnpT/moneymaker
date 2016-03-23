__author__ = 'justnpT'

markets = {"a": "btccny", "b": "ltccny"}
functionalities = {"a": "analizer", "b": "inna funkcjonalnosc"}
metrics = {"a": "srednia", "b": "mediana"}

choice_question_functionality = "funkcjonalnosci: \na) \nb) inna funkcjonalnosc \nwybieram: "
choice_question_market = "gieldy: \na) btccny \nb) ltccny \nwybieram: "
choice_question_period = "okres analizy: \nzastap % porzadana liczba. %Y %m %d \nwybieram: "
choice_question_metric = "metryka dla analizy: \na) srednia \nb) mediana \nwybieram: "

choice_response_functionality = raw_input(choice_question_functionality)
choice_response_market = raw_input(choice_question_market)
choice_response_period = raw_input(choice_question_period)
choice_response_metric = raw_input(choice_question_metric)

if choice_response_market is "a":
    tu powinno byc wywolanie metody ktora ustawia konfiguracje analizer
potem ten analizer powinien byc wywolany dla konkretnego runku, okresu i metryki
To oznacza ze powinien istniec interface dla konkretnej kazdej funkcjonalnosci
- przeczytaj o interfaceach w pythonie.

TODO: doprowadzic program do wydawania prostej decyzji na temat zakupu/sprzedazy

Cel: jak zaprogramowac wydawanie decyzji ?

1. Oblicza srednia cene w ostatnich n tradeach.
2. Jezeli w ostatnich n tradach srednia cena jest wyzsza niz w ostatnim n+1 tradzie, program dokonuje zakupu.
3. Jezeli nizsza, klasa wydaje polecenie sell
4. jezeli taka sama, klasa nie robi nic

Klasy i foldery:
folder analysis klasa mean
klasa mean potrafi zebrac dane dla okresu dlugosci n
folder i klasa decision, ktora potrafi wydac 3 typy decyzji: sell, buy, hold
