import json

def main():
    json_data = '''
    {
        "id": 101,
        "title": "Dune",
        "author": "Frank Herbert",
        "year": 1965,
        "genres": ["Science Fiction", "Adventure"]
    }
    '''
    
    print("--- Parsing JSON ---")
    book_dict = json.loads(json_data)
    
    print(f"ID: {book_dict['id']}")
    print(f"Title: {book_dict['title']}")
    print(f"Author: {book_dict['author']}")
    print(f"Year: {book_dict['year']}")
    print(f"Genres: {book_dict['genres']}")

    print("\n--- Modifying Data ---")
    book_dict['rating'] = 4.8                  
    book_dict['genres'].append("Space Opera")      
    print("Data modified successfully.")

    print("\n--- Converting Back to JSON String ---")
    updated_json_string = json.dumps(book_dict, indent=4)
    print(updated_json_string)

if __name__ == "__main__":
    main()