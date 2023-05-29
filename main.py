"""Module with functions."""


def largest_sum(numbers: list[int]) -> tuple[int, int]:
    if len(numbers) < 2:
        return None
    """Encontra e retorna os dois números que somados dão o maior valor."""
    sorted_numbers = sorted(numbers)
    
    primeiro = sorted_numbers[-2]  # o primeiro número da soma
    segundo =  sorted_numbers[-1]  # o segundo número da soma
    return primeiro, segundo


#def largest_sum(numbers):
#    if len(numbers) < 2:
 #       return None
  #  sorted_numbers = sorted(numbers)
   # return sorted_numbers[-2], sorted_numbers[-1]

