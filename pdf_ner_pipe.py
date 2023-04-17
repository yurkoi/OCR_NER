

def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.text+' - ' +str(ent.start_char) + ' - ' + str(ent.end_char) +
                ' - ' + ent.label_ + ' - ' + str(spacy.explain(ent.label_)))
            print('\n')
    else:
        print('No named entities found.')

def pdf_ner(path_to_pdf='pdf_docs/120220823.pdf'):
    reader = PdfReader(path_to_pdf)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    doc = nlp_ner(pdf)
    show_ents(doc)
    # spacy.displacy.render(doc, style="ent", jupyter=True)


if __name__=='__main__':
    pdf_ner()