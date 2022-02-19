#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: jascha paris
#@title: DEMCON Decode Challenge

import numpy as np
import sys

def create_out_str(generation):
    out_str=np.full((len(generation),)," ")
    out_str[generation==1]="*"
    return ''.join(out_str) + '\n'

def calc_automaton(n_cells, n_generations, true_indices_start, automaton_config):
    gen = np.zeros((n_cells+2,), dtype=int)
    gen[true_indices_start[(true_indices_start>0) * (true_indices_start<=n_cells)]] = 1
    out_str = create_out_str(gen[1:-1])
    for idx in range(n_generations-1):
        gen[1:-1] = automaton_config[4*np.roll(gen,1)+2*gen+np.roll(gen,-1)][1:-1]
        out_str = out_str + create_out_str(gen[1:-1])
    return(out_str)

if __name__ == "__main__":
    # parsing inputs
    data = sys.stdin.readlines()
    operation = data[0].lstrip(' ').rstrip('\n').split(' ')[0]
    n_cells = int(data[0].lstrip(' ').rstrip('\n').split(' ')[1])
    n_generations = int(data[0].lstrip(' ').rstrip('\n').split(' ')[2])
    true_indices_start = np.array(data[1].lstrip('init_start ').rstrip(' init_end\n').split(' '), dtype=int)
    if operation=='A':
        automaton_config = np.array([0,1,0,1,1,1,1,0], dtype=int)
    elif operation=='B':
        automaton_config = np.array([0,1,1,0,1,0,1,0], dtype=int)
    else:
        automaton_config = np.array(data[2].lstrip(' ').rstrip('\n').split(' '), dtype=int)[0:8]
        automaton_config[automaton_config>0]=1
    # run automaton
    print(calc_automaton(n_cells, n_generations, true_indices_start, automaton_config))
    