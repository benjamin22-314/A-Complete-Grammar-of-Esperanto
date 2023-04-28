import os
from deep_translator import GoogleTranslator
from bs4 import BeautifulSoup


def extract_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    data = {}

    # Extract Vocabulary
    vocabulary_section = soup.find('span', string='Vocabulary.')
    if vocabulary_section:
        vocabulary_table = vocabulary_section.find_next('table')
        if vocabulary_table:
            vocabulary = []
            for td in vocabulary_table.find_all('td'):
                text = td.get_text(strip=True)
                text = text.replace(', ', '||')
                vocabulary.append(text)
            data['vocabulary'] = vocabulary

    # Extract Reading Lesson
    reading_section = soup.find('b', string='READING LESSON.')
    if reading_section:
        reading_paragraph = reading_section.find_next('p')
        if reading_paragraph:
            data['reading_lesson'] = reading_paragraph.get_text(strip=True)

    # Extract Sentences for Translation
    translation_section = soup.find('b', string='SENTENCES FOR TRANSLATION.')
    if translation_section:
        translation_paragraph = translation_section.find_next('p')
        if translation_paragraph:
            data['sentences_for_translation'] = translation_paragraph.get_text(strip=True)

    return data


for lesson_file_name in [f"./formatted_lessons/Lesson {i} - Esperanto Grammar.html" for i in range(1, len(os.listdir("./formatted_lessons")) + 1)]:

    # Read the input HTML file
    with open(lesson_file_name, 'r', encoding="utf-8") as file:
        input_html = file.read()

    # Extract the data from the HTML
    data = extract_data(input_html)

    if data.get('sentences_for_translation', False):

        translated = GoogleTranslator(source='en', target='eo').translate(data["sentences_for_translation"])

        html_to_append = f"""
        <center><b>SENTENCES FOR TRANSLATION - TRANSLATED BY GOOGLE TRANSLATE.</b></center>
        <center>(translations may not be accurate or in the spirit the author intended)</center>
        <p>
        {translated}
        </p>
        """
        
    else:
        html_to_append = ""

    # Write the reformatted HTML to an output file
    with open(lesson_file_name.replace("formatted_lessons", "added_translations"), 'w', encoding="utf-8") as file:
        file.write(input_html + html_to_append)
