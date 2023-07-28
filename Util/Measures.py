import time

def print_proccess_time(f):
    '''
    Mide e imprime el tiempo que se tardo la ejecucion de la funcion que decora
    '''
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = f(*args, **kwargs)
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        print(f"{f.__name__} ejecutado en {tiempo_ejecucion} segundos.")
        return resultado
    return wrapper