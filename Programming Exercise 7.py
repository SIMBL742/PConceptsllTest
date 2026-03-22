import re

user_paragraph = input("Enter a paragraph: ")

def extract_sentences(user_paragraph):
    pat = r'.*?[.?!]'
    sentences = re.findall(pat, user_paragraph, flags=re.DOTALL)
    return sentences

def show_sentences(sentences):
    for sentence in sentences:
        print(sentence)
    print("There are:", len(sentences), "sentences")

sentences = extract_sentences(user_paragraph)
show_sentences(sentences)