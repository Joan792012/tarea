meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "CRUSH": "Persona que te gusta o de la que estás enamorado/a",
            "DE CHILL": "Estar relajado, tranquilo o sin preocupaciones",
            "EN EL PLAN": "Se utiliza para explicar algo o introducir una idea",
            "ERES LA CABRA": "Viene del inglés GOAT (Greatest Of All Time), significa que alguien es el mejor en algo",
            "HEATER": "Persona que genera mucho odio en redes sociales",
            "HEAVY": "Se usa para expresar que algo es muy fuerte o intenso",
            "HYPE": "Mucha emoción o expectativa ante algo",
            "PEC": "Acrónimo de Por El Culo se utiliza para expresar que algo está muy bien o mola mucho",
            "TIRAR BEEF": "Discutir o pelearse con alguien, especialmente en redes sociales",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

        
if word in meme_dict.keys():
    print(meme_dict[word])
    # ¿Qué debemos hacer si se encuentra la palabra?
else:
    print("lo lamento no se encuentra esa palabra")
    # ¿Qué hacer si no se encuentra la palabra?
