from db.models import Session, init_db, Trainer, Pokemon
from services.pokeapi import get_pokemon
from services.weather import cidade_temperatura
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    init_db()
    session = Session()
    while True:
        clear()
        print("---------------------------------")
        print("|           Bem-Vindo           |")
        print("|   Selecione a opção desejada  |")
        print("|   1- Adicionar um Treinador   |")
        print("|    2- Capturar um Pokémon     |")
        print("|        3- Treinadores         |")
        print("|     4- Remover um Pokémon     |")
        print("|    5- Remover um Treinador    |")        
        print("|         6- Ver o clima        |")
        print("|           7- Sair             |")
        print("---------------------------------")

        try:
            op = int(input("Digite aqui: "))

            #Adicionar Treinador

            if op == 1:
                name = input("Nome do treinador: ").strip()
                name = name.lower()
                if not name or not name.isalpha():
                    print("Nome não pode estar vazio e não pode ser numérico.")
                    input("Pressione Enter para continuar...")
                    clear()
                    continue
                if session.query(Trainer).filter_by(name=name).first():
                    input("Já existe um treinador com esse nome. Escolha outro.")
                    clear()
                    continue
                else:
                    trainer = Trainer(name=name)
                    session.add(trainer)
                    session.commit()
                    input("Treinador cadastrado.")
                    clear()
                    

            #Adicionar Pokémon

            elif op == 2:
                treinadores = session.query(Trainer).all()
                if not treinadores:
                    input("Nenhum treinador cadastrado.")
                    clear()
                    continue
                for i, t in enumerate(treinadores, 1):
                    print(f"{i}. {t.name}")

                name = input("Nome do treinador: ").strip()
                name = name.lower()
                trainer = session.query(Trainer).filter_by(name=name).first()
                if not trainer:
                    input("Treinador não encontrado.")
                    clear()
                    continue
                #Garante a contagem de até 6 pokémons
                pokemon_count = session.query(Pokemon).filter_by(trainer_id=trainer.id).count()
                if pokemon_count >= 6:
                    input("Limite de 6 Pokémon atingido.")
                    clear()
                    continue
                poke_name = input("Nome do Pokémon: ").strip()
                if not poke_name or not poke_name.isalpha():
                    input("Nome não pode estar vazio e não pode ser numérico.")
                    clear()
                    continue
                info = get_pokemon(poke_name)
                if info:
                    pokemon_name, pokemon_type = info
                    pokemon_types = ", ".join(pokemon_type)
                    pokemon = Pokemon(name = pokemon_name, type = pokemon_types, trainer = trainer)
                    session.add(pokemon)
                    session.commit()
                    input(f"{pokemon_name} adicionado.")
                    clear()
                else:
                    input(f"{poke_name} não encontrado")
                    clear()
    

            #Listar Treinadores

            elif op == 3:
                treinadores = session.query(Trainer).all()
                if not treinadores:
                    input("Nenhum treinador cadastrado.")
                    clear()
                    continue

                for treinador in treinadores:
                    print(f"\nTreinador: {treinador.name}")
                    if treinador.pokemons:
                        for poke in treinador.pokemons:
                            print(f"  - {poke.name} ({poke.type})")
                        input("")
                    else:
                        input("Nenhum pokémon cadastrado.")
                clear()

            #Remover Pokémon

            elif op == 4:
                name = input("Nome do treinador: ").strip()
                name = name.lower()
                trainer = session.query(Trainer).filter_by(name=name).first()
                if not trainer:
                    input("Treinador não encontrado!!")
                    clear()
                    continue
                if not trainer.pokemons:
                    input("Esse treinador não possui pokémons.")
                    clear()
                    continue
                print("\nPokémons cadastrados:")
                for i, poke in enumerate(trainer.pokemons, 1):
                    print(f"{i}. {poke.name} ({poke.type})")
                try:
                    escolha = int(input("Digite o número do pokémon a ser excluído: "))
                    if  len(trainer.pokemons) >= escolha >= 1:
                        pokemon_excluir = trainer.pokemons[escolha - 1]
                        session.delete(pokemon_excluir)
                        session.commit()
                        input(f"{pokemon_excluir.name} foi excluído com sucesso.")
                        clear()
                    else:
                        input("Escolha inválida.")
                        clear()
                except ValueError:
                    input("Entrada inválida. Digite um número.")
                    clear()

            #Remover Treinador

            elif op == 5:
                treinadores = session.query(Trainer).all()
                if not treinadores:
                    input("Nenhum treinador cadastrado.")
                    clear()
                    continue
                for i, t in enumerate(treinadores, 1):
                    input(f"{i}. {t.name}")
                try:
                    escolha = int(input("Digite o número do treinador a ser excluído: "))
                    if len(treinadores) >= escolha >= 1:
                        treinador_excluir = treinadores[escolha - 1]
                        session.delete(treinador_excluir)
                        session.commit()
                        input(f"{treinador_excluir.name} foi excluído com sucesso.")
                        clear()
                    else:
                        input("Escolha inválida.")
                        clear()
                except ValueError:
                    input("Entrada inválida. Digite um número.")
                    clear()
                    
            #Pesquisa clima cidade

            elif op == 6:
                try:
                    cidade = input("Digite o nome da cidade: ")
                    temp = cidade_temperatura(cidade.lower())
                    if temp >= 30:
                        pokemon_name, pokemon_type = get_pokemon("charmander")
                        input(f"Hoje o dia está quente em {cidade}, com uma temperatura de {temp}°. Isso faz dele um ótimo momento para caçar pokémons do tipo {''.join(pokemon_type)}, como o {pokemon_name}!")
                    elif temp >= 20:
                        pokemon_name, pokemon_type = get_pokemon("treecko")
                        input(f"Hoje o dia está agradável em {cidade}, com uma temperatura de {temp}°. Isso faz dele um ótimo momento para caçar pokémons do tipo {''.join(pokemon_type)}, como o {pokemon_name}!")
                    elif temp >= 10:
                        pokemon_name, pokemon_type = get_pokemon("mudkip")
                        input(f"Hoje o dia está frio em {cidade}, com uma temperatura de {temp}°. Isso faz dele um ótimo momento para caçar pokémons do tipo {''.join(pokemon_type)}, como o {pokemon_name}!")
                    else:
                        pokemon_name, pokemon_type = get_pokemon("glalie")
                        input(f"Hoje o dia está congelante em {cidade}, com uma temperatura de {temp}°. Isso faz dele um ótimo momento para caçar pokémons do tipo {''.join(pokemon_type)}, como o {pokemon_name}!")
                except ValueError:
                    input("Entrada inválida. Digite uma cidade válida.")
                    clear()

            #Sair

            elif op == 7:
                input("Saindo do programa...")
                return

        except ValueError:
            print("Entrada inválida! Digite um número válido.")