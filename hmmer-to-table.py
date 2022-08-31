#!/usr/bin/env python3


import sys
import argparse
from pprint import pprint


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--files', 
	required=True,
	nargs="+",
	help='hmmer output files')

parser.add_argument('-o', '--output_file',
	required=False,
	default = False,
	nargs="?",
	help='output file name. Defaults to stdout.')




args = parser.parse_args()
files = args.files
output_file = args.output_file

header = "query\tquery_accession\tquery_description\ttarget_accession\ttarget_description\tfull_eval\tfull_score\tfull_bias\tdom_n\tdom_qual\tdom_score\tdom_bias\tdom_ceval\tdom_ieval\thmm_from\thmm_to\tali_from\tali_to\tenv_from\tenv_to\tacc"


if output_file:
	outf = open(output_file, 'w')
	print(header, file=outf)
	print(f"Writing to: {output_file}")
else:
	print(header)

for file in files:
	with open(file, 'r') as f:
		lines = f.readlines()

		lines = [l.strip() for l in lines if l[0] != "#"]

		# iterates through file using pop(), allowing us to skip lines using the del fuction.
		while len(lines) > 0:
			line = lines.pop(0).strip()


			# gets query information based on line starts
			if line.startswith("Query:"):
				query = " ".join(line.split(":")[1:]).strip()

			if line.startswith("Accession:"):
				query_accession = " ".join(line.split(":")[1:]).strip()

			if line.startswith("Description:"):
				query_description = " ".join(line.split(":")[1:]).strip()

			# identifies the key for showing the full protein entries, skips lines to the information lines, and writes them to a dictionary
			if line.startswith("Scores for complete sequences (score includes all domains):"):
				del lines[:3]

				full_d = {}

				while True:
					full_line = lines.pop(0).strip().split()

					if len(full_line) == 0:
						break
					else:

						target_accession   = full_line[8]
						target_description = " ".join(full_line[9:])

						full_d[target_accession] = {
						'full_eval' : full_line[0],
						'full_score' : full_line[1],
						'full_bias' : full_line[2],
						'target_accession' : target_accession,
						'target_description' : target_description
						}

			# Looks for a domain set by the accession id. Prints out for each domain line found along with generic information.
			if line.startswith(">>"):
				target_accession = line.split()[1]
				del lines[:2]

				while True:
					dom_line = lines.pop(0).strip().split()

					if len(dom_line) == 0:
						break
					else:
						# print(dom_line)


						del dom_line[14]
						del dom_line[11]
						del dom_line[8]

						out_line = [query, query_accession, query_description, 
							target_accession,
							full_d[target_accession]['target_description'],
							full_d[target_accession]['full_eval'],
							full_d[target_accession]['full_score'],
							full_d[target_accession]['full_bias']] + dom_line

						if output_file:
							print("\t".join(out_line), file=outf)
						else:
							print("\t".join(out_line))


if output_file:
	outf.close()

				# sys.exit()


