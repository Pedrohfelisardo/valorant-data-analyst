
from dados import load_csv_data, preprocess_data
from stats import calculate_team_totals, compare_players
import pandas as pd

def main():
    # Carregando os dados dos times e duelos
    caminho_arquivo1 = "C:\\Users\\Pedro Felisardo\\OneDrive\\Desktop\\Projetos\\Time1.csv"
    caminho_arquivo2 = "C:\\Users\\Pedro Felisardo\\OneDrive\\Desktop\\Projetos\\Time2.csv"
    caminho_duelos1 = "C:\\Users\\Pedro Felisardo\\OneDrive\\Desktop\\Projetos\\DuelosTime1vsTime2.csv"
    caminho_duelos2 = "C:\\Users\\Pedro Felisardo\\OneDrive\\Desktop\\Projetos\\DuelosTime2vsTime1.csv"

    # Carregar dados

    time1 = preprocess_data(load_csv_data(caminho_arquivo1,
                                          column_names=["time", "nome", "agente", "kills", "mortes", "assists",
                                                        "plantes", "disarms_spike"]))
    time2 = preprocess_data(load_csv_data(caminho_arquivo2,
                                          column_names=["time", "nome", "agente", "kills", "mortes", "assists",
                                                        "plantes", "disarms_spike"]))


    duelos_time1vs2 = preprocess_data(load_csv_data(caminho_duelos1))
    duelos_time2vs1 = preprocess_data(load_csv_data(caminho_duelos2))

    # Exibir exemplos dos dados carregados
    print("Dados do Time 1:")
    print(time1.head())

    print("\nDados do Time 2:")
    print(time2.head())

    # Calcular totais para os times
    if time1 is not None and time2 is not None:
        team1_totals = time1['kills'].sum()
        team2_totals = time2['kills'].sum()

        print("\nTotais do Time 1:")
        print(team1_totals)

        print("\nTotais do Time 2:")
        print(team2_totals)

    # Comparar jogadores (Exemplo com Time 1)
    if time1 is not None:
        player_comparison1 = compare_players(time1, 'nome', ['kills', 'mortes', 'assists'])
        print("\nComparação entre jogadores do Time 1:")
        print(player_comparison1)

    if time2 is not None:
        player_comparison2 = compare_players(time2, 'nome', ['kills', 'mortes', 'assists'])
        print("\nComparação entre jogadores do Time 2:")
        print(player_comparison2)

    if time1 is not None and time2 is not None:
        combined_data = pd.concat([time1, time2])
        ranking = combined_data[['nome', 'kills','mortes']].sort_values(by='kills', ascending=False).reset_index(drop=True)
        print("\nRanking Geral de Kills:")
        print(ranking)

if __name__ == "__main__":
    main()
