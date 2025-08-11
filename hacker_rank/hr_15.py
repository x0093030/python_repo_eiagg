
#!/bin/python3

import math
import os
import random
import re
import sys
import pdb

def sort():
    """Sort a list of students based on their scores and names."""
    final_list = []
    final_final_list = []
    NAME = 0
    SCORE = 1
    #OKstudents = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]   # TC1 same score (at middle) but different names
    #OKstudents = [['Tina', 20], ['Shina', 20.1], ['Mina', 20.01], ['Tina', 20.001], ['Nina',30]]       # TC2 same name (at start) but different scores
    #OKstudents = [['Kane', 38.21], ['Turner', 37.2], ['Turner', 37.2], ['Awad', 41], ['Hash', 39]]     # TC3 same score (at start) and same name
    students = [['Kane', 38.21], ['Turner', 40.2], ['Turner', 40.2], ['Awad', 41], ['Hash', 39]]     # TC4 same score (at middle) and same name
    students.sort(key=lambda x: x[1], reverse=False) # Sort by score in ascending order, using second element of each sublist
    #students.sort(key=lambda x: x[1], reverse=True)  # Sort by score in descending order, using second element of each sublist
    print(f"\n {students} \n")
    #pdb.set_trace()  # Set a breakpoint here to inspect the state
    found_second_lowest_flag = False  # Flag to check if we have found the second lowest score
    for i in range(0, len(students)-1):
        current_score = students[i][SCORE]
        next_score = students[i+1][SCORE]
        if i == 0:  # If it's the first iteration, append the first student's name
            if current_score == next_score:
                #final_list.append([students[i][NAME], students[i][SCORE]])
                continue
            elif (current_score < next_score) and (found_second_lowest_flag == False):
                final_list.append([students[i+1][NAME], students[i+1][SCORE]])
                found_second_lowest_flag = True
        else:
            if (current_score == next_score):                                               #TC4
                final_list.append([students[i][NAME], students[i][SCORE]])
                final_list.append([students[i+1][NAME], students[i+1][SCORE]])
            elif (current_score < next_score) and (found_second_lowest_flag == False):
                final_list.append([students[i+1][NAME], students[i+1][SCORE]])
                found_second_lowest_flag = True# Append the name of N second lowest score

    #final_list.sort(reverse=False)  # Sort names alphabetically
    for name, score in final_list:
        final_final_list.append(name)  # Create a final list with names only

    #final_final_list.sort(key=lambda x: x[0])  # Sort by name alphabet
    unique_list = list(set(final_final_list))  # Remove duplicates
    unique_list.sort(key=lambda x: x[0])  # Sort again to maintain order after removing duplicates
    print("final_list", unique_list)

def sort_2_testcases():
    """Valida la lógica de la segunda calificación más baja con varios casos de prueba."""
    def print_second_lowest(students):
        # Ordena la lista de estudiantes por calificación de menor a mayor
        students.sort(key=lambda x: x[1])
        print(f"\n {students} \n")
        pdb.set_trace()  # Set a breakpoint here to inspect the state
        
        # Obtiene una lista ordenada de las calificaciones únicas
        scores = sorted({x[1] for x in students})
        print(f"\n {scores} \n")
        pdb.set_trace()  # Set a breakpoint here to inspect the state
        
        # Si hay más de una calificación diferente
        if len(scores) > 1:
            # La segunda calificación más baja es la que está en la posición 1
            second_lowest = scores[1]
            
            # Filtra los estudiantes que tienen esa segunda calificación más baja
            final_list = [x for x in students if x[1] == second_lowest]
            print(f"\n {final_list} \n")
            pdb.set_trace()  # Set a breakpoint here to inspect the state
            
            # Filtra los nombres de los estudiantes que tienen esa segunda calificación más baja
            final_list = [x[0] for x in students if x[1] == second_lowest]
            print(f"\n {final_list} \n")
            pdb.set_trace
        else:
            # Si solo hay una calificación, la lista final queda vacía
            final_list = []
        
        final_list.sort(key=lambda x: x[0], reverse=False)
        print(f"Estudiantes con la segunda calificación más baja: {final_list}")

    # Casos de prueba
    students1 = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    students2 = [['Tina', 20], ['Shina', 20.1], ['Mina', 20.01], ['Tina', 20.001], ['Nina', 30]]
    students3 = [['Kane', 38.21], ['Turner', 37.2], ['Turner', 37.2], ['Awad', 41], ['Hash', 39]]
    students4 = [['Kane', 38.21], ['Turner', 40.2], ['Turner', 40.2], ['Awad', 41], ['Hash', 39]]

    print('Test case 1:')
    print_second_lowest(students1)
    print('Test case 2:')
    print_second_lowest(students2)
    print('Test case 3:')
    print_second_lowest(students3)
    print('Test case 4:')
    print_second_lowest(students4)
    
def task():
    """Determine if a number is 'Weird' or 'Not Weird' based on given conditions."""
    n = abs(int(input()))

    if n>=1 and n<=100:
        if (n%2 == 0 ):
            if (n>=2 or n<=5):
                print("Not Weird")
            elif (n >=6 or n<=20):
                # NOTE, when n=20, expected Weird
                print("Weird")
            elif (n>20):
                print("Not Weird")
        else:
            print("Weird")  
             
if __name__ == '__main__':
    #task()
    sort_2_testcases()
