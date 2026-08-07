#Antes

def CalcularPromedio(Lista):
    s=0
    for x in Lista:
     s=s+x
    return s/len(Lista)
 
l=[1,2,3,4,5]
print(CalcularPromedio(l))

#Después 

def calcular_promedio(Lista) -> float:
    """Calcula el promedio de una lista de números.
 
    Args:
        Lista: lista de números.
 
    Returns:
        El promedio de los números en la lista.
        
    """
    suma = 0
    for x in Lista:
     suma = suma + x
    return suma / len(Lista)
 
def main() -> None:
    lista = [1, 2, 3, 4, 5]
    print(calcular_promedio(lista))


if __name__ == "__main__":
    main()