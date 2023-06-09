#Usage: python extract_selected_cols.py --tsv my_tsv.tsv  --output my_tsv_of_selected_columns.txt --columns col1,col2,col3
#Author: Hojune Lee (ehojune@unist.ac.kr) & ChatGPT

import pandas as pd
import argparse



def extract_columns(input_tsv, output_tsv, selected_columns, file_type):
    # Read the TSV/CSV file into a pandas DataFrame
    seperator = '\t' if file_type is 'tsv' else ',' if file_type is 'csv' else False
    if seperator == False:
        print("FileTypeNotSpecifiedError: please give a value for --file parameter, either csv or tsv")
        return 0
    df = pd.read_csv(input_tsv, sep=seperator, low_memory=False)
    # Extract the selected columns
    selected_df = df[selected_columns]
    # Write the selected columns to a new TSV/CSV file
    selected_df.to_csv(output_tsv, sep=seperator, index=False)


if __name__=="__main__":

    parser = argparse.ArgumentParser(description='python ./extract_sample_name.py --input my_vcf.vcf  --out my_samples.txt')
    parser.add_argument('--input', dest="input", nargs=1, help='path of input tsv file.')
    parser.add_argument('--output', dest="output", nargs=1, help='path of output tsv file.')
    parser.add_argument('--columns', dest="columns", nargs=1, help='columns that you want to extract in the original file, should be comma-seperated without space, packed by double quotation mark. ex) "col1,col2,col3".')
    parser.add_argument('--file', dest="file_type", nargs=1, help='file type, either tsv or csv')

    args = parser.parse_args()
    
    columns = args.columns[0].split(',')
    extract_columns(args.input[0], args.output[0], columns, args.file[0])