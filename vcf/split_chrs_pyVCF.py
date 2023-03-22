#Usage: python extract_sample_name.py --input my_vcf.vcf  --out my_samples.txt
#Author: Hojune Lee (ehojune@unist.ac.kr) & ChapGPT

#import vcf
import os


def split_chrs(input_vcf, output_dir):
	vcf_file = open(input_vcf, 'r')
	chromosomes = [str(i) for i in range(1, 23)] + ['X', 'Y']

	header = ''
	while True:
		line = vcf_file.readline()
		if line.startswith('#CHROM'):
			header = line
			break

	for chromosome in chromosome:
		fw = open(f'{output_dir}/output_{chr}.vcf', 'w')
		fw.write(header)
	# Things to be done



def split_chrs_GATK(input_vcf, output_dir, ref_fa):
	chromosomes = [str(i) for i in range(1, 23)] + ['X', 'Y']

	for chromosome in chromosomes:
		fw = open(f'{output_dir}/output_{chr}.vcf', 'w')
		cmd = "gatk SelectVariants "
		cmd += f"-R {ref_fa} "
		cmd += f"-V {input_vcf} -L chr{chromosome} "
		cmd += f"-O {output_dir}/output_chr{chromosome}.vcf "
		os.system(cmd)


def split_chrs_pyVCF(input_vcf, output_dir): 
	# Open the input VCF file
	vcf_reader = vcf.Reader(open(input_vcf, 'r'))

	# Create a dictionary to store the output VCF writers by chromosome
	output_writers = {}

	# Iterate over the records in the input VCF file
	for record in vcf_reader:
		# Get the chromosome of the current record
		chrom = record.CHROM
		
		# Check if an output writer has already been created for this chromosome
		if chrom not in output_writers:
			# If not, create a new output writer and write the VCF header
			output_file = open(f'{output_dir}/output_{chrom}.vcf', 'w')
			output_writer = vcf.Writer(output_file, vcf_reader)
			output_writer.write_header()
			output_writers[chrom] = output_writer
		
		# Write the record to the output writer for its chromosome
		output_writers[chrom].write_record(record)

	# Close all output files
	for output_writer in output_writers.values():
		output_writer.close()
	


import argparse

if __name__=="__main__":

	parser = argparse.ArgumentParser(description='python ./extract_sample_name.py --input my_vcf.vcf  --out my_samples.txt')
	parser.add_argument('--input_vcf', dest="input_vcf", nargs=1, help='path of input vcf fil.')
	parser.add_argument('--output_dir', dest="output_dir", nargs=1, help='path of output dir that will contain vcf files splitted by chromosome')
	parser.add_argument('--ref_fa', dest="ref_fa", nargs=1, help='reference fasta file which is indexed with GATK IndexFeatureFile, only for the case of GATK')


	args = parser.parse_args()
	split_chrs_GATK(args.input_vcf[0], args.output_dir[0], args.ref_fa[0])
	"""
	try:
		split_chrs_pyVCF(args.input_vcf[0], args.output_dir[0])
	except ModuleNotFoundError as e:
		print("install pyvcf by: conda install -c bioconda pyvcf\n If you already installed, please make new virtual env of python 3.6 and reinstall pyvcf, then re-run this, as pyvcf is not compatible with python 3.7 and higher")
	"""	