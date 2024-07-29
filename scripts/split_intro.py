import json

def split_notebook(input_path, split_keyword, output_path1, output_path2):
    with open(input_path, 'r', encoding='utf-8') as infile:
        notebook = json.load(infile)
    
    # Initialize containers for the two parts
    part1_cells = []
    part2_cells = []
    split_occurred = False
    
    for cell in notebook['cells']:
        if cell['cell_type'] == 'markdown' and any(split_keyword in line for line in cell['source']):
            split_occurred = True
        
        if split_occurred:
            part2_cells.append(cell)
        else:
            part1_cells.append(cell)
    
    # Create new notebook structures
    part1_notebook = {
        "cells": part1_cells,
        "metadata": notebook.get("metadata", {}),
        "nbformat": notebook.get("nbformat", 4),
        "nbformat_minor": notebook.get("nbformat_minor", 5)
    }
    
    part2_notebook = {
        "cells": part2_cells,
        "metadata": notebook.get("metadata", {}),
        "nbformat": notebook.get("nbformat", 4),
        "nbformat_minor": notebook.get("nbformat_minor", 5)
    }
    
    # Write the split notebooks to files
    with open(output_path1, 'w', encoding='utf-8') as outfile1:
        json.dump(part1_notebook, outfile1, indent=2)
    
    with open(output_path2, 'w', encoding='utf-8') as outfile2:
        json.dump(part2_notebook, outfile2, indent=2)

# Define paths and split keyword
input_path = '00_intro.ipynb'
split_keyword = '## Defining Routes'
output_path1 = '00_intro_part1.ipynb'
output_path2 = '01_intro_part2.ipynb'

# Call the function to split the notebook
split_notebook(input_path, split_keyword, output_path1, output_path2)