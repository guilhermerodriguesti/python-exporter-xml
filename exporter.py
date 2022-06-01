# Import the required library
from bs4 import BeautifulSoup

# Main Function
if __name__ == '__main__':

    # Provide the path of the html file
    file = "input.html"

    # Open the html file and Parse it
    # using Beautiful soup's html.parser.
    with open(file, 'r', encoding='utf-8') as inp:
        soup = BeautifulSoup(inp, 'html.parser')

    # Split the document by lines and join the lines
    # from index 1 to remove the doctype Html as it is
    # present in index 0 from the parsed document.
    lines = soup.prettify().splitlines()
    content = "\n".join(lines[1:])

    # Open a output.xml file and write the modified content.
    with open("output.xml", 'w', encoding='utf-8') as out:
        out.write(content)
