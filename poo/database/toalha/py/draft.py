#include <stdio.h>

class towel:
    def __init__(self, color: str, size: str):
        self. color: str=color
        self.size: str=size
        self.wetness: int=0

print("Qual a cor da sua toalha?")
color = input()
towel(color, "p") 
print(f'sua toalha é {color.})