"""Prepare the NLTK resources shared by the notebook and setup script."""

import nltk

RESOURCES = {
    "vader_lexicon": "sentiment/vader_lexicon.zip/vader_lexicon/vader_lexicon.txt",
    "stopwords": "corpora/stopwords/",
}


def ensure_resources():
    for name, path in RESOURCES.items():
        try:
            nltk.data.find(path)
        except LookupError:
            print(f"Downloading missing NLTK resource: {name}")
            if not nltk.download(name, quiet=True):
                raise RuntimeError(f"Could not download NLTK resource: {name}")
            nltk.data.find(path)


if __name__ == "__main__":
    ensure_resources()
