import spacy

# SpaCy modelini yükle
nlp = spacy.load("en_core_web_sm")

# To-Do öğelerini analiz eden işlev
def analyze_todo_item_content(content):
    doc = nlp(content)
    # Analiz işlemleri burada yapılabilir
    # Örneğin, anahtar kelimeleri veya cümlenin duygusal tonunu çıkarabilirsiniz
    return doc
