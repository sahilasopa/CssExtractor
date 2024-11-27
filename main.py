from bs4 import BeautifulSoup
import re

"""
This program extracts relevant CSS rules from one or more CSS files based on HTML files.
It categorizes rules into:
1. Definitely styling rules (e.g., class selectors like `.btn`).
2. Possibly styling rules (e.g., generic tag selectors like `div`).

The author hated to extract the used css classes from big projects or libraries like bootstrap, 
sometimes when working with large css projects, including 2 different css sources breaks each other and can be inefficient,
the below code only gives you the css affecting your html, no more using 10000 lines of css file for just one <button class='btn btn-primary'>. 
"""


def extract_css(html_files, css_files, output_css_file="extracted.css"):
    classes_set = set()
    tags_set = set()

    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file.read(), 'html.parser')

            for tag in soup.find_all(True):
                tags_set.add(tag.name)
                if 'class' in tag.attrs:
                    classes_set.update(tag['class'])

    print("Extracted CSS Classes:\n")
    for class_name in sorted(classes_set):
        print(f".{class_name}")

    print("\nExtracted HTML Tags:\n")
    for tag_name in sorted(tags_set):
        print(tag_name)

    definitely_styling = []
    possibly_styling = []

    for css_file in css_files:
        with open(css_file, 'r', encoding='utf-8') as file:
            css_content = file.read()

        for class_name in sorted(classes_set):
            # GOD knows how i got this working
            pattern = rf'\.{re.escape(class_name)}[^\{{]*\{{[^}}]*\}}'
            matches = re.findall(pattern, css_content, re.MULTILINE)
            definitely_styling.extend(matches)

        for tag_name in sorted(tags_set):
            # GOD knows how i got this working
            pattern = rf'\b{re.escape(tag_name)}[^\{{]*\{{[^}}]*\}}'
            matches = re.findall(pattern, css_content, re.MULTILINE)
            possibly_styling.extend(matches)

    with open(output_css_file, 'w', encoding='utf-8') as output_file:
        # Definitely styling
        output_file.write("/* DEFINITELY STYLING RULES */\n")
        for rule in definitely_styling:
            output_file.write(rule + "\n\n")

        # Possibly styling
        output_file.write("\n/* POSSIBLY STYLING RULES */\n")
        for rule in possibly_styling:
            output_file.write(rule + "\n\n")

    print(f"\nExtracted CSS rules written to {output_css_file}")


if __name__ == "__main__":
    html_files = ["input.html"]  # Add more HTML files as needed
    css_files = ["input.css"]  # Add more CSS files as needed

    output_css_file = "extracted.css"

    extract_css(html_files, css_files, output_css_file)
