import os
import sys

from bs4 import BeautifulSoup
import html2text


def extract_content(html_file, markdown_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    for script in soup(['script', 'style', 'meta', 'link', 'head', 'noscript']):
        script.decompose()

    for img in soup.find_all('img'):
        if 'src' in img.attrs:
            img.replace_with(f"![Image]({img['src']})")

    for math in soup.find_all('span', class_='texmath'):
        img_tag = math.find('img')
        if img_tag and 'src' in img_tag.attrs:
            math.replace_with(f"![]({img_tag['src']})")

    converter = html2text.HTML2Text()
    converter.ignore_links = False
    converter.ignore_images = False
    markdown_text = converter.handle(str(soup))

    with open(markdown_file, 'w', encoding='utf-8') as md_file:
        md_file.write(markdown_text)

    print(f"Converted {html_file} to {markdown_file}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <html_file> [markdown_file]")
        sys.exit(1)

    html_file = sys.argv[1]
    markdown_file = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(html_file)[0] + ".md"

    extract_content(html_file, markdown_file)