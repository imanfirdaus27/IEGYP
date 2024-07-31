from bs4 import BeautifulSoup

def extract_tags(html_content, tag_class):
    soup = BeautifulSoup(html_content, 'html.parser')
    tags = soup.find_all(class_=tag_class)
    for tag in tags:
        print(tag.text.strip())

# Assuming sample.html contains your HTML content
with open('sample.html', 'r') as file:
    html_content = file.read()

extract_tags(html_content, 'your-class-name')  # Replace 'your-class-name' with the actual class name