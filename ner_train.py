import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
import json

nlp = spacy.blank("en") # load a new spacy model
db = DocBin() 
f = open('annotations(1).json')
TRAIN_DATA = json.load(f)


def create_spacy_data():
    for text, annot in tqdm(TRAIN_DATA['annotations']): 
        doc = nlp.make_doc(text) 
        ents = []
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            if span is None:
                print("Skipping entity")
            else:
                ents.append(span)
        doc.ents = ents 
        db.add(doc)

    db.to_disk("./training_data.spacy") # save the docbin object


if __name__ == '__main__':
    print(TRAIN_DATA)

    create_spacy_data()