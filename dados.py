

import pandas as pd

def load_csv_data(file_path, sep=';', header=0, column_names=None):
  
    try:
        data = pd.read_csv(file_path, sep=sep, header=header)
        
        if len(data.columns) == 1:
            data = data[data.columns[0]].str.split(sep, expand=True)
            if column_names is not None and len(column_names) == data.shape[1]:
                data.columns = column_names
            else:
                raise ValueError("O número de colunas no CSV não corresponde ao fornecido em column_names.")
        
        if column_names is not None:
            for col in column_names:
                if col in ['kills', 'mortes', 'assists', 'plantes', 'disarms_spike']:
                    data[col] = pd.to_numeric(data[col], errors='coerce')
        return data
    except Exception as e:
        print(f"Erro ao carregar o arquivo {file_path}: {e}")
        return None

def preprocess_data(data):
    
    if data is not None:
        try:
            
            data.columns = [str(col).strip().lower().replace(' ', '_').replace(';', '_') for col in data.columns]
            
            if data.iloc[0].str.contains('time', case=False).any():
                data = data.iloc[1:].reset_index(drop=True)
            return data
        except Exception as e:
            print(f"Erro ao processar os dados: {e}")
    return None
