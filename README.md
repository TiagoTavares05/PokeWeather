# 🌤️ PokeWeather

Projeto feito em Python que utiliza as APIs da **PokeAPI** e da **OpenWeatherMap** para cadastrar treinadores Pokémon, seus Pokémons (máx. 6 por treinador) e exibir a temperatura de cidades.

## 🔧 Tecnologias

- Python 3
- SQLAlchemy
- PokeAPI
- OpenWeatherMap API
- SQLite (para banco local)
- python-dotenv

## ▶️ Como rodar o projeto

1. Clone o repositório:
   
   git clone https://github.com/TiagoTavares05/PokeWeather.git

   cd PokeWeather

3. instale as dependências:
   
   pip install -r requirements.txt

4. Configure seu .env:

   DATABASE_URL=sqlite:///trainers.db

   weather_api_key=sua_chave_aqui

5. Rode o projeto:
   
   python main.py
