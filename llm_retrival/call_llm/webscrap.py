from bs4 import BeautifulSoup

# Specify the path to your local HTML file
file_path = 'C:/Users/laith/Downloads/Superlinear Returns.html'

# Open the file in read mode and parse it with BeautifulSoup
with open(file_path, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Replace <br> tags with newline characters
for br in soup.find_all("br"):
    br.replace_with("\n")

# Extract text
text = soup.get_text()

# Use strip() to remove leading/trailing whitespace and then split based on two or more newline characters
sections = [section.strip() for section in text.split("\n\n") if section.strip()]

# Print the sections separated by a clear marker for readability
for index, section in enumerate(sections):
    print(f"Section {index + 1}: {section}\n")
    print("---------\n")
