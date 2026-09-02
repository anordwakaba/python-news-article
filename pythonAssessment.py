def count_specific_word(article_text, search_word):
    import re
    words = re.findall(r'\b\w+\b', article_text)
    count = 0

    for word in words:
        if word == search_word:
            count += 1

    return count


def identify_most_common_word(article_text):
    import re
    from collections import Counter

    words = re.findall(r'\b\w+\b', article_text.lower())
    word_count = Counter(words)

    return word_count.most_common(1)[0][0]


article_text = "Python is easy. Python is powerful."



print(identify_most_common_word(article_text))
def calculate_average_word_length(article_text):
    words = article_text.split()
    total_length = 0

    for word in words:
        word = word.strip(".,!?;:")
        total_length += len(word)

    if len(words) > 0:
        return total_length / len(words)
    else:
        return 0

    if len(words) > 0:
        return total_length / len(words)
    else:
        return 0.0







def count_paragraphs(article_text):
    paragraphs = article_text.split("\n\n")

    if len(paragraphs) > 0:
        return len(paragraphs)
    else:
        return 0


def count_sentences(article_text):
    sentences = article_text.split(".")
    count = 0

    for sentence in sentences:
        if sentence.strip():
            count += 1

    return count




choice = 0

while choice < 1:
    choice += 1

print("Analysis Complete.")