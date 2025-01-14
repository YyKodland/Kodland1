print("Hola si estas aqui no entiendes algo")
meme = {
            "CRINGE": "Pena ajena",
            "LOL": "Una respuesta común a algo gracioso",
            "MEME":"Algo gracioso"
            
            }
for i in range(5):
    palabra = input("Escribe algo que no entiendas en mayuscula:")

    if palabra in meme.keys():
          print(meme[palabra])
    else:
        print("Palabra no reconocida")
