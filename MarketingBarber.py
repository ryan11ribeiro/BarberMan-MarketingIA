import requests
import os
from dotenv import load_dotenv
from groq import Groq


cidade = str(input("Insira o nome da sua cidade: "))

cidadeSemEspaco = cidade.replace(" ", "%20")

urlApi = f"https://wttr.in/{cidadeSemEspaco}?format=j1"

print(f" Aguarde só um momento. \n ")

load_dotenv()
keyGroq = os.getenv("keyGroq")
respostaIA = Groq(api_key=keyGroq)

try: 
    response = requests.get(urlApi)
    dadosTempo = response.json()
    temperatura_atual = dadosTempo['current_condition'][0]['temp_C']
    condicao_texto = dadosTempo['current_condition'][0]['weatherDesc'][0]['value'].lower()

    temperatura_atual = int(temperatura_atual)


    print (f"\n Temperatura: {temperatura_atual} ºC")
    print (f"\n Condição climática é : {condicao_texto} \n")

    varGroq = respostaIA.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages= [{
            "role": "user",
            "content": f"Crie um texto BEM curto, formatado e convidativo para cortar na barbearia usando a temperatura{temperatura_atual} e a condição climatica {condicao_texto}."}
        ]
    )
    textoGroq = varGroq.choices[0].message.content
    print(textoGroq)
except:
    print(f"Erro ao solicitar ao sistema. Verifique o nome da cidade.")