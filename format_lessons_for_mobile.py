import os
from bs4 import BeautifulSoup

def reformat_html_for_mobile(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Set viewport for mobile devices
    viewport_tag = soup.new_tag('meta')
    viewport_tag.attrs['name'] = 'viewport'
    viewport_tag.attrs['content'] = 'width=device-width, initial-scale=1'
    soup.insert(0, viewport_tag)

    # Add CSS for mobile devices
    style_tag = soup.new_tag('style')
    style_tag.string = '''
        body {
            font-family: Arial, sans-serif;
            font-size: 16px;
            line-height: 1.5;
            margin: 0;
            padding: 1em;
        }
        p, table {
            margin-bottom: 1em;
        }
        table {
            border-collapse: collapse;
            width: 100%;
        }
        td {
            border: 1px solid #ccc;
            padding: 0.5em;
        }
        center {
            text-align: center;
        }
    '''
    soup.append(style_tag)

    # Remove nowrap attribute from table cells
    for td in soup.find_all('td'):
        del td['nowrap']

    return str(soup)


for lesson_file_name in [f"./split_lessons/Lesson {i} - Esperanto Grammar.html" for i in range(1, len(os.listdir("./split_lessons")) + 1)]:

    # Read the input HTML file
    with open(lesson_file_name, 'r') as file:
        input_html = file.read()

    # Reformat the HTML for mobile devices
    mobile_html = reformat_html_for_mobile(input_html)

    # Write the reformatted HTML to an output file
    with open(lesson_file_name.replace("split_lessons", "formatted_lessons"), 'w', encoding="utf-8") as file:
        file.write(mobile_html)
