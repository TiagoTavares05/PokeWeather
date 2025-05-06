import requests
from config import weather_api_key

def cidade_temperatura(cidade):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={weather_api_key}&units=metric&lang=pt_br"
        response = requests.get(url)
        response.raise_for_status()  # dispara erro se a resposta for diferente de 200
        dados = response.json()
        temperatura = dados['main']['temp']
        return temperatura
    except requests.exceptions.HTTPError:
        raise ValueError("Cidade não encontrada ou inválida.")
    except requests.exceptions.RequestException:
        raise ValueError("Erro na conexão com a API.")
    except (KeyError, TypeError):
        raise ValueError("Erro ao processar os dados da API.")
