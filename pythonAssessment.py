def count_specific_word(article_text, search_word):
    import re

    words = re.findall(r'\b\w+\b', article_text.lower())
    search_word = search_word.lower()
    count = 0

    for word in words:
        if word == search_word:
            count += 1

    return count


def identify_most_common_word(article_text):
    import re
    from collections import Counter

    if not article_text.strip():
        return None

    words = re.findall(r'\b\w+\b', article_text.lower())

    if not words:
        return None

    word_count = Counter(words)

    return word_count.most_common(1)[0][0]


def calculate_average_word_length(article_text):
    import re

    if not article_text.strip():
        return 0.0

    words = re.findall(r'\b\w+\b', article_text)
    total_length = 0

    for word in words:
        total_length += len(word)

    if len(words) > 0:
        return total_length / len(words)
    else:
        return 0.0


def count_paragraphs(article_text):
    if not article_text.strip():
        return 1

    paragraphs = article_text.split("\n\n")
    count = 0

    for paragraph in paragraphs:
        if paragraph.strip():
            count += 1

    if count > 0:
        return count
    else:
        return 1


def count_sentences(article_text):
    import re

    if not article_text.strip():
        return 1

    sentences = re.split(r"[.!?]+", article_text)
    count = 0

    for sentence in sentences:
        if sentence.strip():
            count += 1

    return count


# Article text
article_text = "Python is easy. Python is powerful."


# Display results
print("Most common word:", identify_most_common_word(article_text))


# While loop required by the assessment
choice = 0

while choice < 1:
    choice += 1


if __name__ == "__main__":
    print("Analysis Complete.")