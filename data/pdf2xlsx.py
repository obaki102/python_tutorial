import camelot
import pandas as pd

def convert_pdf_to_xlsx(pdf_path, xlsx_path, sheet_name='ConvertedSheet'):
    # Extract tables from PDF into a list of DataFrames
    print("Reading.....")
    tables = camelot.read_pdf(pdf_path, flavor='stream', pages='all')

    # Create an Excel writer
    with pd.ExcelWriter(xlsx_path, engine='openpyxl') as writer:
        print("Converting.....")
        
        # Concatenate all tables into a single DataFrame
        combined_df = pd.concat([table.df for table in tables], ignore_index=True)

        # Write the combined DataFrame to the specified sheet
        combined_df.to_excel(writer, sheet_name=sheet_name, index=False)

if __name__ == "__main__":
    # Replace 'input.pdf' and 'output.xlsx' with your actual file paths
    input_pdf = 'lrgFile.pdf'
    output_xlsx = 'output.xlsx'

    convert_pdf_to_xlsx(input_pdf, output_xlsx)
    print("Conversion completed successfully.")
