import requests
from config import weather_api_key

def cidade_temperatura(cidade):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={weather_api_key}&units=metric&lang=pt_br"
        response = requests.get(url)
        response.raise_for_status()  # levanta um erro se o status != 200
        dados = response.json()
        temperatura = dados['main']['temp']
        return temperatura
    except requests.exceptions.HTTPError as e:
        raise ValueError("Cidade não encontrada")
    except Exception as e:
        raise ValueError("Erro ao buscar temperatura")