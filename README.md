# ncbi-blastn-runner
A simple Python tool to run BLASTN on a FASTA sequence and extract top hit summaries from NCBI and save the result in txt format
# blastn-fasta-tool

A Python script that automates nucleotide BLAST (BLASTN) searches using NCBI's online service. It takes a FASTA sequence as input, performs a BLAST search, and displays the top 5 hits while saving a full summary of all hits to a `.txt` file.

## Features

- Accepts a FASTA file as input (single sequence)
- Runs BLASTN query using NCBI's REST service
- Displays top 5 hits in the terminal
- Saves the complete summary of all BLAST hits in `blast_summary.txt`
- Saves raw BLAST output in `blast_result.xml` (optional reuse)

## Requirements

- Python 3.x
- Biopython

Install required packages using:

```bash
pip install biopython
