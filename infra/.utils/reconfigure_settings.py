from pathlib import Path
import re


DATABASES = '''DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": config("POSTGRES_DB", default="postgres"),
                "USER": config("POSTGRES_USER", default="postgres"),
                "PASSWORD": config("POSTGRES_PASSWORD", default="postgres"),
                "HOST": config("DB_HOST", default="localhost"),
                "PORT": config("DB_PORT", cast=int, default=5432),
            }
        }'''

def get_env_file_path():
    current = Path(__file__).resolve()
    root = current.parent.parent
   
    env_path = root / 'backend' / 'core' / 'settings.py'
    return env_path



def read_settings():

    item = get_env_file_path()
    print(item)
    try:
        with open(item, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()

    except FileExistsError:
        return False

    
def write_settings():
    item = get_env_file_path()
    content = read_settings()

    if not content:
        return False

    if "from decouple import config" not in content:
        content = content.replace(
            "from pathlib import Path",
            "from pathlib import Path\nfrom decouple import AutoConfig"
        )

    content = content.replace(
        "BASE_DIR = Path(__file__).resolve().parent.parent","BASE_DIR = Path(__file__).resolve().parent.parent\n\n\nenv_loader = AutoConfig(search_path=str(BASE_DIR / 'infra' / 'env'))" \
            '\nENV = env_loader("ENV", default="dev")\n\nENV_FILE_DIR = BASE_DIR / "infra" / "env"\nconfig = AutoConfig(search_path=str(ENV_FILE_DIR))'
    )

    content = re.sub(
        r"SECRET_KEY\s*=\s*['\"].*?['\"]",
        "SECRET_KEY = config('SECRET_KEY')",
        content
        )

    content = re.sub(
    r"(INSTALLED_APPS\s*=\s*\[[^\]]*)",
    r"\1\n    'rest_framework',\n\t 'rest_framework_simplejwt', \n\t 'corsheaders', \n\t'django_extensions' ,\n\t'api', \n\t",
    content
)
    
    content = content.replace('DEBUG = True', "DEBUG = config('DEBUG', cast=bool, default=False)")

    content = re.sub(
        r"DATABASES\s*=\s*\{(?:[^{}]|\{[^{}]*\})*\}",
        DATABASES,
        content
    )

    content = content.replace(
        "LANGUAGE_CODE = 'en-us'", "LANGUAGE_CODE = 'pt-br'",
        
    )

    content = content.replace("TIME_ZONE = 'UTC'" , "TIME_ZONE = 'America/Sao_Paulo'")



    with open(item, 'w', encoding='utf-8') as arquivo:
        arquivo.write(content)

    return True



if __name__ == "__main__":
    write_settings()