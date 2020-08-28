from sklearn.preprocessing import OneHotEncoder
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import re
import nltk


stemmer = SnowballStemmer("english")
lemmatizer = WordNetLemmatizer()


def binarize_columns(df, cols):
    for col in cols:
        df = binarize_column(df, col)
    return df


def binarize_column(df, col):
    df.loc[:, col] = df[col].fillna(False)
    df.loc[:, col] = df[col].astype(int)
    return df


def tokenize(text):
    # A pattern to only keep letter tokens
    pattern = re.compile('[a-zA-Z]')
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    # A list of tokens to keep
    valid_tokens = []
    for token in tokens:
        if re.search(pattern, token):
            valid_tokens.append(token)
    return valid_tokens


def stem(tokens):
    # Uses SnowballStemmer from NLTK
    stems = [stemmer.stem(token) for token in tokens]
    return stems

def lemma(tokens):
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmas


def tokenize_and_stem(text):
    return stem(tokenize(text))


def tokenize_and_lemma(text):
    return lemma(tokenize(text))