from string import printable
from random import choice
from pathlib import Path

def generate_env_file():
    """
    Gera o arquivo .env com as variáveis necessárias para execução da aplicação.

    O arquivo é criado no diretório definido por `get_env_file_path()`.
    Caso o arquivo já exista, nenhuma modificação é realizada.

    Returns:
        bool: True se o arquivo foi criado com sucesso.
              False se o arquivo .env já existia.
    """

    caracters = get_valid_characters()
    env_path = get_env_file_path()

    variaveis = {
        'POSTGRES_DB' : 'app_db',
        'POSTGRES_USER' : 'postgres',
        'POSTGRES_PASSWORD' :  'postgres',
        'DB_HOST' : 'db',
        'DB_PORT' : '5432',
        'SECRET_KEY' : ''.join(choice(caracters) for _ in range(35)),
        
    }
    env_path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        with open(env_path, 'x', encoding='utf-8') as arquivo:
            conteudo = '\n'.join(f"{k}={v}" for k, v in variaveis.items())
            arquivo.write(conteudo)

    except FileExistsError:
        return False
    
    return True



def get_env_file_path():

    current = Path(__file__).resolve()
    root = current.parent.parent
    env_path = root / 'infra' / 'env' / '.env.dev'
    return env_path


def get_valid_characters():
    
    invalidos= ['\t','\n',' ','\r','.',',',"'",'\x0b','\x0c','`','´','\\']
    filtered = filter(lambda c : c not in invalidos, printable)
    caracters = ''.join(filtered)
    return caracters


if __name__ == "__main__":
    generate_env_file()