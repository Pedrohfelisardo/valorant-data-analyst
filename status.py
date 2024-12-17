

def calculate_team_totals(data, team_column, stat_columns):
    
    totals = {}
    try:
        for team in data[team_column].unique():
            team_data = data[data[team_column] == team]
            totals[team] = {stat: team_data[stat].sum() for stat in stat_columns}
        return totals
    except Exception as e:
        print(f"Erro ao calcular totais por time: {e}")
        return None

def compare_players(data, player_column, stat_columns):
    
    try:
        player_stats = data[[player_column] + stat_columns].copy()
        player_stats = player_stats.sort_values(by=stat_columns, ascending=False)
        return player_stats
    except Exception as e:
        print(f"Erro ao comparar jogadores: {e}")
        return None
