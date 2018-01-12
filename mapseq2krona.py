#/usr/bin/python
import argparse, collections

parser = argparse.ArgumentParser(description='This script converts Mapseq formated results to KronaTools (ktImportText)')
parser.add_argument('input', help="Input file (Mapseq output file)", type=str)
parser.add_argument('-c', type=float, default=0.5, help="Confidence score threshold. (default 0.5)")
args = parser.parse_args()

data = collections.defaultdict(str)

# Iterator to return all lists in the data dictionary
def yield_all_lists(data):
	for k,v in data.items():
		yield tuple(v)

# Parse
with open(args.input) as handle:
	for line in handle:
		if line.startswith("#"):
			continue
		line = line.strip().split("\t")
		data[line[0]]= line[13:]

# Apply threshold cut off
for k,v in data.items():
	for x, _ in enumerate(v):
		if x%3 == 0:
			if float(min(v[x+1], v[x+2])) >= args.c:
				if x == 0:
					data[k] = [v[x]]
				else:
					data[k].append(v[x])

# Print Krona format
krona = collections.Counter(yield_all_lists(data))
for k,v in krona.items():
	taxa = "\t".join(list(k))
	print "{}\t{}".format(v,taxa)

		
#print data, args.c
