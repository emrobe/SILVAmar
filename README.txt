#SILVA mar (mmp.sfb.uit.no)

These scripts maps SILVA mar for mapseq in a two step process.
1. The script map_SILVAmar.py maps SILVA accessions via NCBI taxids to mar taxids, creating SILVA mar, a subset of SILVA SSU containing only SILVA sequences with tax ids pertaining to the marine environment as defined at mmp.sfb.uit.no
2. The script format_mapseq_SILVAmar.py creates a custom reference .tax file needed in classification using mapseq

To run, the first script needs:
-An output directory (mkdir output)
-The two tab formated MAR database files (DB and Ref) found in https://s1.sfb.uit.no/ (MarXX.tsv). Assumes taxid in column 52
-The latest SILVA SSU database (SILVA_XXX_SSURef_tax_silva_trunc.fasta)
-A mapping file (taxmap_embl_ssu_ref_128.txt). Assumes taxid in column 6

The SILVA database and coresponding mapping files are available at https://www.arb-silva.de/download/archive/
