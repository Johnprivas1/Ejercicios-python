"""
Problema 5
"""
import random

def generate_random_numbers():
    numbers = []
    for _ in range(20):
        numbers.append(random.randint(0, 100))
    return numbers

def display_list(numbers):
    print("Lista de números generados:")
    for number in numbers:
        print(number, end=",")

def sort_and_display_list(numbers):
    sorted_numbers = sorted(numbers)
    print("\nLista de números ordenados:")
    for number in sorted_numbers:
        print(number, end=",")