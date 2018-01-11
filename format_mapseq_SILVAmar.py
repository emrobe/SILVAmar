#!/usr/bin/python
import HTSeq

output = open("output/mapseq_marDBs_ref.tax", "w")

output.write("#cutoff: 0.00:0.08 0.70:0.35 0.70:0.35 0.70:0.35 0.80:0.25 0.92:0.08 0.95:0.05\n")
output.write("#name: SILVAmar\n")
output.write("#levels: Kingdom Phylum Class Order Family Genus Species\n")

for seq in HTSeq.FastaReader("output/mapseq_marDBs_ref.fasta"):
	output.write(seq.name+"\t"+seq.descr+"\n")

output.close()
