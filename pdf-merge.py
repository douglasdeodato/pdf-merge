import PyPDF2
import os

def merge_pdfs(input_folder, output_file):
    pdf_merger = PyPDF2.PdfMerger()

    # Get a list of all PDF files in the input folder
    pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]

    # Sort the files to maintain order if needed
    pdf_files.sort()

    # Merge all PDF files into one
    for pdf_file in pdf_files:
        file_path = os.path.join(input_folder, pdf_file)
        pdf_merger.append(file_path)

    # Write the merged PDF to the output file
    with open(output_file, 'wb') as output:
        pdf_merger.write(output)

    print(f'Merged {len(pdf_files)} PDF files into {output_file}')

# Set the input folder containing your PDF files
input_folder = '/path/to/your/pdf/files'

# Set the output file name for the merged PDF
output_file = '/path/to/your/output/merged.pdf'

# Call the merge_pdfs function
merge_pdfs(input_folder, output_file)
