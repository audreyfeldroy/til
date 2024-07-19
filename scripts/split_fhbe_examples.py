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

# Initialize variables for grouping cells by sections
section_name = None
section_cells = []
example_counter = 1

def is_full_example_header(line):
    """Check if a line is a 'Full Example' header."""
    return line.lower().startswith("full example")

def sanitize_filename(name):
    """Sanitize the section name to create a valid filename."""
    # Keep only alphanumeric characters and underscores
    sanitized = re.sub(r'\W+', '_', name)
    return sanitized.lower()

def create_notebook(cells):
    """Create a notebook structure from the given cells."""
    return {
        "cells": cells,
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 2
    }

def save_section(section_name, section_cells, example_counter):
    """Save the collected section cells to a notebook file."""
    if not section_name or not section_cells:
        return
    
    # Create a short filename from the section name
    short_name = sanitize_filename(section_name)
    filename = f"{example_counter:02d}_ex_{short_name}.ipynb"
    filepath = os.path.join(output_dir, filename)
    
    # Create the notebook structure
    notebook = create_notebook(section_cells)
    
    # Write the notebook content to the file
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2)
    
    print(f"Saved {filename}")

# Process each cell in the notebook
for cell in notebook_content['cells']:
    cell_type = cell['cell_type']
    source = ''.join(cell['source'])
    
    if cell_type == 'markdown':
        # Check for section headers
        for line in cell['source']:
            if line.strip().startswith("#") and is_full_example_header(line.strip("# ").strip()):
                # Save the previous section if any
                save_section(section_name, section_cells, example_counter)
                
                # Start a new section
                section_name = line.strip("# ").strip()
                section_cells = [cell]
                example_counter += 1
                break
        else:
            # If no header, add the cell to the current section
            if section_name:
                section_cells.append(cell)
    else:
        # Add code cells to the current section
        if section_name:
            section_cells.append(cell)

# Save the last section if any
save_section(section_name, section_cells, example_counter)

print("Notebook has been split into separate files.")