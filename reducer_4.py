#!/usr/bin/env python3
# -*-coding:utf-8 -*

import sys

current_key = None
neighbors_set = set()  # Use a set to store unique neighbors

def emit_adjacency_list(key, neighbors_set):
    neighbors_str = '\t'.join(neighbors_set)
    print(f"{key}\t1\t{len(neighbors_set)}\t{neighbors_str}")

for line in sys.stdin:
    line = line.strip()
    key, neighbor = line.split('\t', 1)
    
    neighborInfo = neighbor.split('\t', 1)
    if current_key == key:
        if len(neighborInfo) == 1:
            neighbors_set.add(neighborInfo[0])  # Add neighbor to the set
    else:
        if current_key:
            emit_adjacency_list(current_key, neighbors_set)
        current_key = key
        if len(neighborInfo) == 1:
            neighbors_set = {neighborInfo[0]}  # Initialize a new set for the current key
        else:
            neighbors_set = set() # Initialize a new empty set for the current key

if current_key:
    emit_adjacency_list(current_key, neighbors_set)
