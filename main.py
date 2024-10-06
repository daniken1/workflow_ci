# Importamos la librería termcolor para agregar color al texto
from termcolor import colored
import time
import os

# Función para imprimir un "Hola, Mundo" bonito
def hola_mundo_bonito():
    # Limpiamos la terminal para un efecto más limpio
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Texto en estilo ASCII
    mensaje = """
    _    _      _ _        __          __        _     _ 
   | |  | |    | | |       \ \        / /       | |   | |
   | |__| | ___| | | ___    \ \  /\  / /__  _ __| | __| |
   |  __  |/ _ \ | |/ _ \    \ \/  \/ / _ \| '__| |/ _` |
   | |  | |  __/ | | (_) |    \  /\  / (_) | |  | | (_| |
   |_|  |_|\___|_|_|\___( )    \/  \/ \___/|_|  |_|\__,_|
                      |/                                
    """
    
    # Imprimir el mensaje "Hola, Mundo" con color y negritas
    print(colored(mensaje, 'cyan', attrs=['bold']))
    
    # Añadimos un efecto de espera antes del final
    time.sleep(2)
    print(colored("¡Bienvenido al mundo de la programación!", 'yellow', attrs=['bold', 'blink']))

# Llamamos a la función para que imprima el mensaje bonito
if __name__ == "__main__":
    hola_mundo_bonito()
