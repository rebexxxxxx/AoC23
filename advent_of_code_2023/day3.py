# Advent of Code day 3

import re
import pandas as pd
import numpy as np

 #to retrieve certain lines of the data frame
#convert first line to a string, lets see if its easy to index a string
line1 = file.iloc[0,:].to_string(header=False, index=False)
line4 = file.iloc[4,:].to_string(header=False, index=False)

def main():
    #filepath = "/Users/rebeccasansale/Desktop/advent_of_code_2023/day3_input.txt"
        print("Adventing the code: Day 3")
        filepath = "/Users/rebeccasansale/Desktop/advent_of_code_2023/day3_example_values.txt"
        file = pd.read_table(filepath, header = None, delimiter = None)
        symbols = {'*', '$', '-', '+', '@', '#', '%', '^', '&', '\\', '/', '~', '`', ';', '<', '>', '?', ':', '{', '}', '|', '='}
        sum_count = 0
        for i in range(0, (len(file))):
                print("line in file:",i)  
                if i > 0:
                    previous_line = file.iloc[i-1,:]
                    previous_line = previous_line.astype(str).str.cat(sep='') 
                
                previous_line_symbol = False 
                current_line = file.iloc[i,:]
                current_line = current_line.astype(str).str.cat(sep='') 
                
                if i < len(file):
                    next_line = file.iloc[(i+1),:]
                    next_line = next_line.astype(str).str.cat(sep='') 

                current_line_num = {m.start(0):int(m.group(0)) for m in re.finditer("\d+", current_line)}
                if len(current_line_num) ==0: pass
                for key in current_line_num:
                    # what about strings at the beginning and end of the line?
                    #if key = 0, then lower bound is 0 and upper bound is length of number + 1
                    if key == 0:
                        current_line_index_check = np.array([0, int(key)+len(str(current_line_num[key]))+1])
                        # next_line_index_check = np.linspace(0, len(str(current_line_num[key])), len(str(current_line_num[key]))+1)
                    elif ((key-1)+len(str(current_line_num[key]))) == (len(str(current_line))-1):
                        current_line_index_check = np.array([int(key)-1, int(key)+len(str(current_line_num[key]))])
                        # next_line_index_check = np.linspace(int(key)-1, key+len(str(current_line_num[key])), len(str(current_line_num[key]))+1)
                    else:
                        current_line_index_check = np.array([int(key)-1, int(key)+len(str(current_line_num[key]))])
                    
                    #init symbol variables
                    cl_low_symbol = False
                    cl_high_symbol = False
                    next_line_symbol = False
                    previous_line_symbol = False
                    
                    if not (current_line[current_line_index_check[0]].isnumeric() or (current_line[current_line_index_check[0]] == '.')):
                        cl_low_symbol = True
                    if not (current_line[current_line_index_check[1]].isnumeric() or (current_line[current_line_index_check[1]] == '.')):
                        cl_high_symbol = True
                
                    if i < len(file):
                        next_line_check = next_line[current_line_index_check[0]:current_line_index_check[1]]
                    if any(symbol in next_line_check for symbol in symbols):
                        next_line_symbol = True
                        
                    if i > 0:
                        previous_line_check = previous_line[current_line_index_check[0]:current_line_index_check[1]]
                        if any(symbol in previous_line_check for symbol in symbols):
                            previous_line_symbol = True
                        
                    #only counting number once     
                    if cl_low_symbol or cl_high_symbol or next_line_symbol or previous_line_symbol:
                        sum_count += current_line_num[key]
                        print("current_line_num[key]:",current_line_num[key])
        return sum_count
main()
        




def main_balls():
    filepath = "/Users/rebeccasansale/Desktop/advent_of_code_2023/day3_example_values.txt"
    file = pd.read_table(filepath, header = None, delimiter = None)
    for i in range(0, len(file)):
            current_line = file.iloc[i,:]
            current_line = current_line.astype(str).str.cat(sep='') 
            #current_line = current_line.to_string
            print(current_line)
            print(type(current_line))
            

main_balls()


    






