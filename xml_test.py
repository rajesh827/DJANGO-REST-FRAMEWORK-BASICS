import xml.etree.ElementTree as ET

book_xml = '''
<book id="101">
    <title>The Alchemist</title>
    <author>Paulo Coelho</author>
    <year>1988</year>
    <genres>
        <genre>Fiction</genre>
        <genre>Adventure</genre>
    </genres>
</book>
'''
print("--- Parsing XML ---")
root = ET.fromstring(book_xml)

print("Book ID:", root.get("id"))
print("Title:", root.find("title").text)
print("Author:", root.find("author").text)
print("Year:", root.find("year").text)
print("Genres:")
for genre in root.find("genres").findall("genre"):
    print("-", genre.text)

print("\n--- Modifying XML Data ---")
rating = ET.Element("rating")
rating.text = "4.7"
root.append(rating)

new_genre = ET.Element("genre")
new_genre.text = "Philosophy"
root.find("genres").append(new_genre)

print("\n--- Converting Back to XML String ---")
updated_xml = ET.tostring(root, encoding="unicode")

print("\nUpdated XML:")
print(updated_xml)