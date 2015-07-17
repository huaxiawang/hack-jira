__author__ = 'hwang'
import nltk
import string
from .models import EpsCase, Comment
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

token_dict = {}
stemmer = PorterStemmer()


def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed


def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems


def get_token():
    for case in EpsCase.objects.all():
        summary = case.case_summary.encode("utf-8")
        description = " " if case.case_description is None else case.case_description.encode("utf-8")
        comments = Comment.objects.filter(epsCase=case).values_list('comment_text', flat=True)
        joined_comment = " ".join(comments).encode("utf-8")
        joined_text = " ".join([summary, description, joined_comment]).lower()
        no_punctuation = joined_text.translate(None, string.punctuation)
        token_dict[case.case_key] = no_punctuation


def get_tfidf():
    get_token()
    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    tfs = tfidf.fit_transform(token_dict.values())
    return tfs