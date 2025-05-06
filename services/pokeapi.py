import requests

def get_pokemon(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}/"
    response = requests.get(url)

    if response.status_code == 200:
        response_dict = response.json()
        pokemon_name = response_dict['name']
        pokemon_types = [entry['type']['name'] for entry in response_dict['types']]
        return pokemon_name, pokemon_types
    else:
        raise ValueError(f"Pókemon '{nome}' não encontrado.")
    
""""
nome = "bulbasaur"
pokemon_name, pokemon_types = get_pokemon(nome) 
print(f"Nome: {pokemon_name}")
print(f"Tipos: {', '.join(pokemon_types)}")
"""