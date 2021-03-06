import streamlit as st
import spacy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from flair.models import SequenceTagger
from flair.data import Label, Sentence
import nltk

def text_analyzer(my_text, lang):
    try:
        nlp = spacy.load(lang+'_core_web_sm')
    except OSError:
        download_error_message = f"You should download the corresponding language by \'python -m spacy download **{lang:}** \'"
        st.error(download_error_message)
        st.stop()
    nlp_text = nlp(my_text)
    tokens = [token.text for token in nlp_text]
    token_dict = [('"Token": {},\n "Lemma": {}'.format(token.text, token.lemma_)) for token in nlp_text ]
    return token_dict

def spacy_entity_recognition(my_text, lang):
    try:
        nlp = spacy.load(lang+'_core_web_sm')
    except OSError:
        download_error_message = f"You should download the corresponding language by \'python -m spacy download **{lang:}** \'"
        st.error(download_error_message)
        st.stop()
    nlp_text = nlp(my_text)
    entities = [(entity.text, entity.label_) for entity in nlp_text.ents ]
    return entities

def flair_entity_recognition(my_text):
    tagger = SequenceTagger.load('ner')
    sentence = Sentence(my_text)
    tagger.predict(sentence)
    entities = (sentence.to_dict(tag_type = 'ner'))
    return entities

def custom_entity_recognition(my_text):
    tagger = SequenceTagger.load('resources/taggers/example-ner/final-model.pt')
    sentence = Sentence(my_text)
    tagger.predict(sentence) 
    entities = (sentence.to_dict(tag_type = 'ner'))
    return entities
    
def sumy_summarizer(my_text):
    parser = PlaintextParser.from_string(my_text,Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document,3)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result

def main():

    st.title('Basic NLP app using Streamlit')

    #Language choice 
    lang_options = ('en','es','fr','de','it','ru')
    lang_str = st.selectbox(
        'Choose the language supported by spaCy', lang_options)
    lang_bold =  f"Your text is in **{lang_str:}**."
    st.write(lang_bold)

    #Tokenization and Lemmatization
    if st.checkbox('Tokenization and Lemmatization'):
        text_str = st.text_area('Enter Your Text', key = 'token_and_lemma')
        if st.button('Analyze'):
            nlp_result = text_analyzer(text_str, lang_str)
            st.json(nlp_result)

    #spaCy NER
    if st.checkbox('Default Name Entity Recognition from spaCy'):
        text_str = st.text_area('Enter Your Text', key = 'spacy_ner')
        if st.button('Extract Entities', key = 'spacy'):
            nlp_result = spacy_entity_recognition(text_str, lang_str)
            st.json(nlp_result)

    #flair NER
    if st.checkbox('Default Name Entity Recognition from Flair'):
        text_str = st.text_area('Enter Your Text', key = 'flair_ner')
        if st.button('Extract Entities', key = 'flair'):
            nlp_result = flair_entity_recognition(text_str)
            st.json(nlp_result)
    
    #custom NER
    if st.checkbox('Custom Name Entity Recognition in Flair'):
        text_str = st.text_area('Enter Your Text', key = 'custom_flair_ner')
        if st.button('Extract Entities', key = 'custom_flair'):
            nlp_result = custom_entity_recognition(text_str)
            st.json(nlp_result)

    #Summarization
    if st.checkbox('Text Summarization'):
        text_str = st.text_area('Enter Your Text', key = 'sum')
        if st.button('Summarize'):
            st.text("Applying Sumy Summarizer")
            summary_result = sumy_summarizer(text_str)
            st.success(summary_result)

if __name__ == '__main__':
    main()
