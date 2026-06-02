import re
import sys


def count_specific_word(text, search_word):
    if text == "" or search_word == "":
        return 0

    pattern = r"\b" + re.escape(search_word.lower()) + r"\b"
    matches = re.findall(pattern, text.lower())
    return len(matches)


def identify_most_common_word(text):
    if text == "":
        return None

    words = re.findall(r"[a-zA-Z0-9']+", text.lower())
    if len(words) == 0:
        return None

    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    most_common_word = None
    highest_count = 0
    for word in words:
        if counts[word] > highest_count:
            highest_count = counts[word]
            most_common_word = word

    return most_common_word


def calculate_average_word_length(text):
    if text == "":
        return 0

    words = re.findall(r"[a-zA-Z0-9']+", text)
    if len(words) == 0:
        return 0

    total_length = 0
    index = 0
    while index < len(words):
        total_length += len(words[index])
        index += 1

    return total_length / len(words)


def count_paragraphs(text):
    if text == "":
        return 1

    lines = text.splitlines()
    if len(lines) == 0:
        return 1

    paragraphs = 0
    in_paragraph = False
    line_index = 0

    while line_index < len(lines):
        line = lines[line_index].strip()
        if line == "":
            in_paragraph = False
        else:
            if not in_paragraph:
                paragraphs += 1
                in_paragraph = True
        line_index += 1

    if paragraphs == 0:
        return 1

    return paragraphs


def count_sentences(text):
    if text == "":
        return 1

    sentence_marks = re.findall(r"[.!?]+", text)
    if len(sentence_marks) == 0:
        return 1

    return len(sentence_marks)


def load_article_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def main():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = "news_article.txt"

    try:
        article_text = load_article_text(file_path)
    except FileNotFoundError:
        print(f"Could not find the file: {file_path}")
        return

    search_word = "the"

    print("Specific word count:", count_specific_word(article_text, search_word))
    print("Most common word:", identify_most_common_word(article_text))
    print("Average word length:", calculate_average_word_length(article_text))
    print("Paragraph count:", count_paragraphs(article_text))
    print("Sentence count:", count_sentences(article_text))


if __name__ == "__main__":
    main()