# Importamos la librería termcolor para agregar color al texto
from termcolor import colored
import time
import os

def welcome_bonito():
    # Limpiamos la terminal para un efecto más limpio
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Texto en estilo ASCII con la palabra "Welcome!"
    mensaje = r"""
 __        __   _                             
 \ \      / /__| | ___ ___  _ __ ___   ___  
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ 
   \ V  V /  __/ | (_| (_) | | | | | |  __/ 
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  
                                                   
    """
    
    # Imprimir el mensaje "Welcome!" con color cian y negritas
    print(colored(mensaje, 'cyan', attrs=['bold']))
    
    # Mensaje adicional con color amarillo y negritas
    print(colored("¡Welcome!", 'yellow', attrs=['bold']))
    
    # Añadimos un efecto de espera antes del final
    time.sleep(2)

# Llamamos a la función para que imprima el mensaje bonito
if __name__ == "__main__":
    welcome_bonito()