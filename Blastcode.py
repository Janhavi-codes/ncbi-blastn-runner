## importing important biopython modules

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML 
from Bio import SeqIO
import os

## Taking the fasta file as a input ###

fasta_file = input("Enter the path to the fasta file:")

print("Blast is running......Please wait")
##parsing and reading the fasta file with Seqio(!! file must contain one sequence!!)
try:
    record = SeqIO.read(fasta_file, format="fasta")
except FileNotFoundError:
    print(f"Error: file'{fasta_file}' not found.") 
    exit()
except Exception as e:                                                                                                                                                                                                                                                                                                                                                                                                                      
    print(f"Error reading file: {e}")
    exit()
    
    
##running blast search using NCBIWWW.qtblast
try:
    result_handle = NCBIWWW.qblast("blastn", "nt", record.format("fasta"))
    print("Blast is running......")
    
except Exception as e:
    print(f" error during blast search : {e}")
    exit()
    
## Saving the blast result in XML format
output_file= "blast_result.xml"
with open(output_file, "w") as out_handle:
    out_handle.write(result_handle.read())
    result_handle.close()
print(f"blast result saved to : {output_file}")

###Opening and parsing the blast result###
try:
    with open(output_file) as result_file:
        blast_record = NCBIXML.read(result_file)
except Exception as e:
    print(" Error parsing BLAST XML:", e)
    exit()
    
## Displaying the top 5 matches (alignments)
print ("\n Top 5 blast hit:")
summary_file = "blast_summary.txt"
with open(summary_file, "w") as out:
    out.write("")
for alignment in blast_record.alignments[:5]:
    print(f"\n Title: {alignment.title}")
    print(f" Length: (alignment.lenght)")
    print(f" Acession: {alignment.accession}")
    
## printing the first hsp score###
for hsp in alignment.hsps:
        print(f"   Score: {hsp.score}")
        print(f"   E-value: {hsp.expect}")
        break 
    
## saving the readable summary of all the hits to a .txt file
summary_file = os.path.join(os.path.dirname(__file__), "blast_summary.txt")
with open(summary_file, "w")as out:
    out.write(f" BLAST Summary - All Hits\n\n")
    for alignment in blast_record.alignments:
        out.write(f"Title: {alignment.title}\n")
        out.write(f"Length: {alignment.length}\n")
        out.write(f"Accession: {alignment.accession}\n")
        for hsp in alignment.hsps:
            out.write(f"Score: {hsp.score}\n")
            out.write(f"E-value: {hsp.expect}\n")
            break
        out.write("-" * 50+"\n")
        print(f"\n Full summary saved to : {summary_file}")
        
if os.path.exists("blast_summary.txt"):
    print("✅ File blast_summary.txt exists.")
else:
    print("❌ File was not created.")