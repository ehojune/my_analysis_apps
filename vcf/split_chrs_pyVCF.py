#Usage: python extract_sample_name.py --input my_vcf.vcf  --out my_samples.txt
#Author: Hojune Lee (ehojune@unist.ac.kr) & ChapGPT

import vcf


def split_chrs_pyVCF(input_vcf, output_dir): 
	# Open the input VCF file
	vcf_reader = vcf.Reader(open(input_vcf, 'r'))

	# Create a dictionary to store the output VCF files by chromosome
	output_files = {}

	# Iterate over the records in the input VCF file
	for record in vcf_reader:
		# Get the chromosome of the current record
		chrom = record.CHROM
		
		# Check if an output file has already been created for this chromosome
		if chrom not in output_files:
			# If not, create a new output file and write the VCF header
			output_files[chrom] = open(f'{output_dir}/output_{chrom}.vcf', 'w')
			output_files[chrom].write(str(vcf_reader.metadata))
			output_files[chrom].write('#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n')
		
		# Write the record to the output file for its chromosome
		output_files[chrom].write(str(record) + '\n')

	# Close all output files
	for f in output_files.values():
		f.close()
	


import argparse

if __name__=="__main__":

	parser = argparse.ArgumentParser(description='python ./extract_sample_name.py --input my_vcf.vcf  --out my_samples.txt')
	parser.add_argument('--input_vcf', dest="input_vcf", nargs=1, help='path of input vcf fil.')
	parser.add_argument('--output_dir', dest="output_dir", nargs=1, help='path of output dir that will contain vcf files splitted by chromosome')

	args = parser.parse_args()
	try:
		split_chrs_pyVCF(args.input_vcf[0], args.output_dir[0])
	except ModuleNotFoundError as e:
		print("install pyvcf by: conda install -c bioconda pyvcf\n If you already installed, please make new virtual env of python 3.6 and reinstall pyvcf, then re-run this, as pyvcf is not compatible with python 3.7 and higher")