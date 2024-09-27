
from typing import Callable
from py_ggra import parse_file, resolve_nt, expanded_obj_repr_lines, time_info

def write_definitions(nt_definitions: list):
    repres = str(nt_definitions)
    with open("grammar_structure.txt", "w", encoding="utf-8") as doc:
        for line in expanded_obj_repr_lines(repres):
            doc.write(line)
            doc.write("\n")

def joined_sentence(words: list[str]) -> str:
    sentence = " ".join(words)
    sentence = sentence.replace(" ,", ",").replace(" .", ".").replace(" ?", "?").replace(" !", "!")
    return sentence[0].upper() + sentence[1:]

def ramble_til_sentence(sentence: str, sentence_function: Callable[[], str], *, file = None, limit = 10000):
    current = ""
    sentences = 0
    while current != sentence:
        current = sentence_function()
        print(current, file=file)
        sentences += 1
        if sentences == limit:
            break

if __name__ == "__main__":
    filename = "grammars/grammar_german3.ggra"#"grammars/grammar_german3.ggra"

    with open(filename, "r", encoding="utf-8") as doc:
        nt_definitions = parse_file(doc)
    
    def generate_sentence():
        return joined_sentence(resolve_nt(nt_definitions, "Satz", {})) 
    
    # until = ""
    # with open("konversation.txt", "w", encoding="utf-8") as doc:
    #     ramble_til_sentence(until, generate_sentence, file=doc, limit=50_000)
    # print("\nFertig!")
    
    for _ in range(10):
        print(generate_sentence())