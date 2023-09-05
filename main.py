import pandas as pd
import glob
import tabula


if __name__ == '__main__':
    files_pdf = glob.glob(r'test_files/*.pdf')
    pdf_tables = tabula.read_pdf(files_pdf[0],
                                 pages='all',
                                 multiple_tables=True,
                                 lattice=True)


