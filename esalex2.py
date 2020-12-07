listaA = []
listaB = []
while True:
    parola = input("inserire la prima parola della lista = ")
    lettere = len(parola)
    listaA.append(parola)
    listaB.append(lettere)
    scelta = input("aggiungere elementi alla lista? ")
    if scelta == "si":
        breakpoint
    else:
        print(listaA)
        print(listaB)
