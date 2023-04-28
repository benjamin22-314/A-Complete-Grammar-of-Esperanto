import re

# Read the HTML file into a string
with open('The Project Gutenberg eBook of A Complete Grammar of Esperanto, by Ivy Kellerman Reed.html', 'r') as f:
    html_str = f.read()

# Define the regex pattern to match the start of a lesson
lesson_pattern = re.compile(r'^<center class="lesson"><b>LESSON \w+\.</b></center>$', re.MULTILINE)

# Split the HTML string into separate lesson sections
lesson_sections = re.split(lesson_pattern, html_str)

# Loop through the lesson sections and save each one to a separate file
for i, lesson_section in enumerate(lesson_sections[1:], start=1):
    filename = f"./split_lessons/Lesson {i} - Esperanto Grammar.html"
    with open(filename, 'w') as f:
        f.write(lesson_section)