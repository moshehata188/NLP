"""
Mohamed Mohamed Shehata Shehata Badawy
FCAI|DU Level 4 - CS department  
Task 2  ( Natural Language Processing )
"""
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

df = pd.read_csv("./IMDB Dataset.csv")


print(df.head())


def tokenize_text(text):
    tokens = word_tokenize(text.lower())
    return tokens


def stem_tokens(tokens):
    porter = PorterStemmer()
    stemmed_tokens = [porter.stem(token) for token in tokens]
    return stemmed_tokens


df['Tokenized_text'] = df['review'].apply(tokenize_text)
df['Stemmed_text'] = df['Tokenized_text'].apply(stem_tokens)


print(df[['review', 'Tokenized_text', 'Stemmed_text']].head())

# Write DataFrame to a text file
df.to_csv('output.txt', sep='\t', index=False)
