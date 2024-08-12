# Exercise 10: Multilingual Phrasebook Compiler
"""
Objective: Design a Python program to compile a multilingual phrasebook from various language text files, focusing on handling encoding and decoding with UTF-8. This exercise will involve file handling for processing text in different languages and incorporate Python concepts like functions, string manipulation, and try-except blocks.

Problem Statement: Create a Python program that consolidates common phrases in different languages into a single phrasebook. Each language will have its phrases stored in a separate file (e.g., phrases_english.txt, phrases_spanish.txt, phrases_french.txt), with each line containing a common phrase. The program should combine these phrases into a single file (multilingual_phrasebook.txt), ensuring proper handling of various character encodings.
filename = 'Module3/Lesson5/Exercise10/english_phrases.txt'
"""

def read_phrases(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []

def compile_phrasebook(languages, output_file):
    compiled_phrases = ""
    for language in languages:
        phrases = read_phrases(f"Module3/Lesson5/Exercise10/{language}_phrases.txt")
        compiled_phrases += f"--- {language.title()} ---\n" + "\n".join(phrases) + "\n\n"
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(compiled_phrases)


def main():
    languages = ['english', 'spanish', 'french']
    compile_phrasebook(languages, 'Module3/Lesson5/Exercise10/multilingual_phrasebook.txt')
    print("Compiled multilingual phrasebook.")

if __name__ == '__main__':
    main()