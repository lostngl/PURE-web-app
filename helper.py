from bioscrape import *
from biocrnpyler import *
import numpy as np
import time
import os

directory = os.getcwd()

def process_input(data):
    return data.upper()

#Definition to un-nest lists that will be created by models

def flatten(t):
    return [item for sublist in t for item in sublist]

#User will copy the sequence bwteen end of promoter and start of terminator of DNA strain
#mGapt_UTR1_deGFP 

dna_seq = ''

def update_dna_sequence(sequence):
    global dna_seq
    dna_seq = process_input(sequence)
    return f'DNA sequence updated to: {dna_seq}'

def analyze_dna():
    return f'analyzing DNA sequence: {dna_seq}'
