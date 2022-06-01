from lxml import html, etree

# Main Function
if __name__ == '__main__':

    # Provide the path of the html file
    file = "input.html"

    # Open the html file and Parse it,
    # returning a single element/document.
    with open(file, 'r', encoding='utf-8') as inp:
        htmldoc = html.fromstring(inp.read())

    # Open a output.xml file and write the
    # element/document to an encoded string
    # representation of its XML tree.
    with open("output.xml", 'wb') as out:
        out.write(etree.tostring(htmldoc))