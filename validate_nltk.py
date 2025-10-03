import nltk

required_nltk_resources = {
    "vader_lexicon": "sentiment/vader_lexicon",
    "stopwords": "corpora/stopwords",
}

for pkg_name, pkg_path in required_nltk_resources.items():
    try:
        nltk.data.find(pkg_path)
        print(f"NLTK resource '{pkg_name}' found (path: {pkg_path}).")
    except LookupError:
        print(f"NLTK resource '{pkg_name}' not found. Downloading...")
        nltk.download(pkg_name)
