from Bio import SeqIO
from Bio.Blast import NCBIXML

def main():
    rewrite_to_fasta()
    Open_XML()

def rewrite_to_fasta():
    with open("format.unknown", "rU") as Input:
        with open("Afvink4.fasta", "w") as Output:
            seq = SeqIO.parse(Input, "genbank")
            count = SeqIO.write(seq, Output, "fasta")
    print("%i Sequenties herschreven" % count)

def Open_XML():
    T="_"*160
    blast_record = NCBIXML.read(open("blast_report.xml"))   
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            print(T)
            print ("Alignment")
            print ("Sequence  :", alignment.title)
            print ("Length    :", alignment.length)
            print ("E-value   :", hsp.expect)
            print ("Score     :", hsp.score)
            print ("Alignment:")
            print ('\tquery  :',hsp.query)
            print ('\t        ',hsp.match)
            print ('\tsubject:',hsp.sbjct)
    print(T)
    
main()