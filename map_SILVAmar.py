from collections import defaultdict
import HTSeq, re

# NCBI mapping (Maps silva accessions to ncbi tax ids)
ncbi = defaultdict(int)
with open("taxmap_embl_ssu_ref_128.txt") as data:
	for line in data:
		linelist = line.split("\t")
		if linelist[5].strip() in ncbi:
			ncbi[linelist[5].strip()].append(linelist[0])
		else:
			ncbi[linelist[5].strip()] = [linelist[0]]

# MarDBs (parse all mar tax ids)
mar = []
with open("MarDB.tsv") as data:
	for line in data:
		linelist = line.split("\t")
		mar.append(linelist[51])

with open("MarRef.tsv") as data:
	for line in data:
		linelist = line.split("\t")
		mar.append(linelist[51])
yes = 0
no = 0
out = []

# Map all coresponding tax ids from ncbi to mar
for entry in mar:
	if entry in ncbi:
		for accession in ncbi[entry]:
			out.append(accession)
		yes += 1
	else:
		no += 1
print "----"
print "Mar taxonomy accessions total: "+str(len(mar))
print "Mar taxonomy accessions matched: "+str(yes)
print "Mar taxonomy accessions NOT matched: "+str(no)
print "----"

print "Total SILVA accessions matched: "+str(len(out))
out = set(out)
print "Unique SILVA accessions: "+str(len(out))
print "----"
inputfile = "SILVA_128_SSURef_tax_silva_trunc.fasta"
outputfile = "output/mapseq_marDBs_ref.fasta"
outhandle = open(outputfile, "w")
outcount = 0
for seq in HTSeq.FastaReader(inputfile):
	match = re.search('(.+?)\.', seq.name)
	if match.group(1) in out:
		outcount +=1
		seq.write_to_fasta_file(outhandle)
		
print "Parsing {}, writing to {}".format(inputfile, outputfile)
print "Sequences written: "+str(outcount)
print "----"
print "Done"
