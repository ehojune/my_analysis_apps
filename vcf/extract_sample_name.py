#Usage: python extract_sample_name.py --input my_vcf.vcf  --out my_samples.txt
#Author: Hojune Lee (ehojune@unist.ac.kr) & ChapGPT

def extract_sampleName_in_vcf(vcf, output):
	print(vcf)
	vcf_file = open(vcf, 'r')
	# iterate through each line of the VCF file
	for line in vcf_file:
		# check if the line starts with '#CHROM'
		if line.startswith('#CHROM'):
			# split the line into columns separated by tabs
			columns = line.strip().split('\t')
			# the sample names start at the 10th column (index 9)
			sample_names = columns[9:]
			# print the sample names
			print(sample_names, "will be written in ", output)
			break
	vcf_file.close()

	output_file = open(output, 'w')
	for sample in sample_names:
		output_file.write(f'{sample}\n')
	output_file.close()


import argparse

if __name__=="__main__":

    parser = argparse.ArgumentParser(description='python ./extract_sample_name.py --input my_vcf.vcf  --out my_samples.txt')
    parser.add_argument('--input', dest="input", nargs=1, help='path of input vcf file that you want to extract sample names in it.')
    parser.add_argument('--output', dest="output", nargs=1, help='path of output sample list text file, including a sample name per line, without header.')

    args = parser.parse_args()
    
    extract_sampleName_in_vcf(args.input[0], args.output[0])