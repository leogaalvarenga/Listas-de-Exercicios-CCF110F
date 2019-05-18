tempo = int(input("Quanto tempo sua viagem levou, em horas? \n"))

velo = int(input("Qual foi a sua velocidade media, em km/h? \n"))

distancia = tempo * velo

litros = distancia / 12

print("Você percorreu ", distancia, " quilometros e gastou", litros, "litros de combustivel.")
