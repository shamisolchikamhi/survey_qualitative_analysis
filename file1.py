import pandas as pd
import matplotlib
import numpy as np
import nltk
import seaborn
import sklearn
import gensim
import pyLDAvis
import wordcloud
import textblob
import textstat
import spacy

news= pd.read_csv('teachers_data.csv',nrows=10000)
news.head(3)
