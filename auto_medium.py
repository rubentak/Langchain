# Reading in a python notebook file as a text document and cleaning


#%% READING
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Reading in a python files as a text document
text = open("langchain.ipynb", "r")

# print frirst 5 lines of text
for x in range(50):
    print(text.readline())

#%% CLEANING
# when "celltype is code" then "source" is code
# when "celltype is markdown" then "source" is markdown
import json
# extracht the code and markdown from the text file
code = []
markdown = []
notebook = []

with open('langchain.ipynb', 'r') as f:
    data = json.load(f)

for cell in data['cells']:
    if cell['cell_type'] == 'markdown':
        markdown.append(cell['source'])
    elif cell['cell_type'] == 'code':
        code.append(cell['source'])

for cell in data['cells']:
    notebook.append(cell['source'])

# append the markdown and code to a text file
with open('data/markdown.txt', 'w') as f:
    for item in markdown:
        f.write("%s\n" % item)

with open('data/code.txt', 'w') as f:
    for item in code:
        f.write("%s\n" % item)

with open('data/notebook.txt', 'w') as f:
    for item in notebook:
        f.write("%s\n" % item)

# read in the markdown and code text files
markdown = open("data/markdown.txt", "r")
code = open("data/code.txt", "r")
notebook = open("data/notebook.txt", "r")
#




