import json
import os
import re

# Path to the Jupyter notebook file within the local repository
notebook_path = "nbs/05_by_example.ipynb"

# Directory to save the split files
output_dir = "fh_by_example"

# Read the notebook content from the local file
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook_content = json.load(f)

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Initialize variables for capturing the intro cells
intro_cells = []
found_first_example = False

def is_full_example_header(line):
    """Check if a line is a 'Full Example' header."""
    return line.lower().startswith("full example")

def create_notebook(cells):
    """Create a notebook structure from the given cells."""
    return {
        "cells": cells,
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 2
    }

def save_notebook(cells, filename):
    """Save the collected cells to a notebook file."""
    if not cells:
        return

    filepath = os.path.join(output_dir, filename)
    
    # Create the notebook structure
    notebook = create_notebook(cells)
    
    # Write the notebook content to the file
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2)
    
    print(f"Saved {filename}")

# Process each cell in the notebook
for cell in notebook_content['cells']:
    if found_first_example:
        break
    
    cell_type = cell['cell_type']
    source = ''.join(cell['source'])
    
    if cell_type == 'markdown':
        # Check for section headers
        for line in cell['source']:
            if line.strip().startswith("#") and is_full_example_header(line.strip("# ").strip()):
                found_first_example = True
                break
    
    if not found_first_example:
        intro_cells.append(cell)

# Save the intro section before the first "Full Example"
save_notebook(intro_cells, "00_intro.ipynb")

print("Intro section has been saved as 00_intro.ipynb.")
