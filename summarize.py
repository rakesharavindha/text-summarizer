import re
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.nlp.tokenizers import Tokenizer

LANGUAGE = "english"

class SimpleTokenizer:
    def to_sentences(self, text):
        return re.split(r'(?<=[.!?])\s+', text.strip())

    def to_words(self, sentence):
        return re.findall(r'\b\w+\b', sentence.lower())

def summarize_text(text, max_sentences=3):
    parser = PlaintextParser.from_string(text, SimpleTokenizer())
    summarizer = LexRankSummarizer(Stemmer(LANGUAGE))
    summarizer.stop_words = get_stop_words(LANGUAGE)
    summary = summarizer(parser.document, max_sentences)
    return " ".join(str(sentence) for sentence in summary)
