import os
import numpy as np
import pandas as pd
from tqdm import tqdm
from PyPDF2 import PdfReader


# extract text from .pdf to dictionary
def create_df_pdf(path_to_pdfs='pdf_docs/'):
    dict_df_pdf = {}
    for pdf in tqdm(os.listdir(path_to_pdfs)):
        path_to_pdf = path_to_pdfs+pdf
        reader = PdfReader(path_to_pdf)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        dict_df_pdf[path_to_pdf] = text
    
    return dict_df_pdf


if __name__ == '__main__':

    new_df_pdf = create_df_pdf()
    data_frame = pd.DataFrame(new_df_pdf, index=range(0, len(new_df_pdf))).T.iloc[:, 1]
    print(data_frame.head())

    with open('all_pdf_text.txt', 'w') as f:
        for index, line in tqdm(zip(data_frame.index, data_frame.values)):
            f.write(index)
            f.write('\n'+line +'\n')