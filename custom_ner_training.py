from typing import List
from flair.datasets import ColumnCorpus
from flair.models import SequenceTagger
from flair.trainers import ModelTrainer
from flair.data import Corpus
from flair.embeddings import *

columns = {0 : 'text', 1 : 'ner'}
data_folder = '/Users/Dmytro_Bezushchak/Desktop/NLP_app'

# Initializing the corpus
corpus: Corpus = ColumnCorpus(data_folder, columns,
                              train_file = 'train.txt',
                              test_file = 'test.txt',
                              dev_file = 'dev.txt')

tag_type = 'ner'
tag_dictionary1 = corpus.make_tag_dictionary(tag_type=tag_type)

embedding_types: List[TokenEmbeddings] = [
        WordEmbeddings('glove'),
        # other embeddings
        ]
embeddings: StackedEmbeddings = StackedEmbeddings(
                                embeddings=embedding_types)

tagger : SequenceTagger = SequenceTagger(hidden_size=256,
                                        embeddings=embeddings,
                                        tag_dictionary=tag_dictionary1,
                                        tag_type=tag_type,
                                        use_crf=True)
                                        
trainer : ModelTrainer = ModelTrainer(tagger, corpus)

trainer.train('resources/taggers/example-ner',
               learning_rate=0.1,
               mini_batch_size=32,
               max_epochs=150)
print(tagger)
