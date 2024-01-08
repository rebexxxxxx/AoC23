#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 09:28:32 2023

@author: rebeccasansale
"""
import re
import pandas as pd
import numpy as np
import itertools as it
from itertools import repeat



#cubes = [r,g,b]
cubes = [12, 13, 14]
filepath = "/Users/rebeccasansale/Desktop/advent_of_code_2023/day2_example_values.txt"
filepath = "/Users/rebeccasansale/Desktop/advent_of_code_2023/day_2_input.txt"
file = pd.read_table(filepath, header = None, delimiter = None)

def main():
    print("Adventing the code: Day 2")
    rejects = np.zeros(len(file))
    with open(filepath, 'r') as f:
        for i, line in enumerate(f):
            #try: #using try since i dont know how errors will be handled
                game = line
                game_split = game.split(';')
                game_split[0] = game_split[0].split(':')[1] #removing the "game x :" from first game 
                #creating a balanced panel
                for j in range(len(game_split)):
                    g = game_split[j]
                    if "red" not in g:
                            g = g + " 0 red"
                    if "blue" not in g:
                            g = g + " 0 blue" 
                    if "green" not in g:
                            g = g + " 0 green"
                    game_split[j] = g
                
                game_split = ''.join(game_split)
                red_pattern = r'\b(?:[0-9]|[12][0-9]|3[0-9]|40)\s*red\b'
                reds = ' '.join(re.findall(red_pattern, game_split))
                reds = [int(word) for word in reds.split() if word.isdigit()]
                
                blue_pattern = r'\b(?:[0-9]|[12][0-9]|3[0-9]|40)\s*blue\b'
                blues = ' '.join(re.findall(blue_pattern, game_split))
                blues = [int(word) for word in blues.split() if word.isdigit()]
                
                green_pattern = r'\b(?:[0-9]|[12][0-9]|3[0-9]|40)\s*green\b'
                greens = ' '.join(re.findall(green_pattern, game_split))
                greens = [int(word) for word in greens.split() if word.isdigit()]

                allcolors = np.array([reds, blues, greens]).T
                allgames = pd.DataFrame(allcolors, columns = ['Red', 'Blue', 'Green'])
                print(allgames)
                for color in range(len(['Red', 'Blue', 'Green'])):
                    col = ['Red', 'Blue', 'Green'][color]
                    if col == 'Red':
                        red_data = allgames['Red']
                        print(red_data.max())
                        if int(red_data.max()) > cubes[0]: rejects[i] = 1
                    if col == 'Green':
                        green_data = allgames['Green']
                        print(green_data.max())
                        if int(green_data.max()) > cubes[1]: rejects[i] = 1
                    if col == 'Blue':
                        blue_data = allgames['Blue']
                        print(blue_data.max())
                        if int(blue_data.max()) > cubes[2]: rejects[i] = 1
        return(np.sum(np.where(rejects==0)[0]+1))
    return(rejects)
        #return(indices)
main()






#part 2
def main():
    print("Adventing the code: Day 2")
    rejects = np.zeros(len(file))
    red_max = np.zeros(len(file))
    blue_max = np.zeros(len(file))
    green_max = np.zeros(len(file))
    powers = np.zeros(len(file))
    with open(filepath, 'r') as f:
        for i, line in enumerate(f):
            #try: #using try since i dont know how errors will be handled
                game = line
                game_split = game.split(';')
                game_split[0] = game_split[0].split(':')[1] #removing the "game x :" from first game 
                #creating a balanced panel
                for j in range(len(game_split)):
                    g = game_split[j]
                    if "red" not in g:
                            g = g + " 0 red"
                    if "blue" not in g:
                            g = g + " 0 blue" 
                    if "green" not in g:
                            g = g + " 0 green"
                    game_split[j] = g
                
                game_split = ''.join(game_split)
                red_pattern = r'\b(?:[0-9]|[12][0-9]|3[0-9]|40)\s*red\b'
                reds = ' '.join(re.findall(red_pattern, game_split))
                reds = [int(word) for word in reds.split() if word.isdigit()]
                
                blue_pattern = r'\b(?:[0-9]|[12][0-9]|3[0-9]|40)\s*blue\b'
                blues = ' '.join(re.findall(blue_pattern, game_split))
                blues = [int(word) for word in blues.split() if word.isdigit()]
                
                green_pattern = r'\b(?:[0-9]|[12][0-9]|3[0-9]|40)\s*green\b'
                greens = ' '.join(re.findall(green_pattern, game_split))
                greens = [int(word) for word in greens.split() if word.isdigit()]

                allcolors = np.array([reds, blues, greens]).T
                allgames = pd.DataFrame(allcolors, columns = ['Red', 'Blue', 'Green'])
                print(allgames)
                for color in range(len(['Red', 'Blue', 'Green'])):
                    col = ['Red', 'Blue', 'Green'][color]
                    if col == 'Red':
                        red_data = allgames['Red']
                        print(red_data.max())
                        red_max[i] = int(red_data.max()) 
                        print(red_max)
                    if col == 'Green':
                        green_data = allgames['Green']
                        print(green_data.max())
                        green_max[i] = int(green_data.max()) 
                        print(green_max)
                    if col == 'Blue':
                        blue_data = allgames['Blue']
                        print(blue_data.max())
                        blue_max[i] = int(blue_data.max()) 
                        print(blue_max)
                        
                answer = np.sum((np.multiply(np.multiply(red_max,green_max), blue_max)))
                print(answer)
                        
    return answer
        
main()



