import frappe
import requests

@frappe.whitelist()
def fetch_google_book(isbn):
    # We keep the function name 'fetch_google_book' so the button still works!
    # But now we use Open Library to bypass the Google block.
    
    # 1. Clean the ISBN (remove dashes or spaces)
    clean_isbn = isbn.replace("-", "").strip()
    
    # 2. Open Library API URL
    url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{clean_isbn}&format=json&jscmd=data"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Open Library returns data with the key "ISBN:978..."
        key = f"ISBN:{clean_isbn}"
        
        if key in data:
            info = data[key]
            
            # Get the cover image (Large or Medium)
            cover_url = info.get("cover", {}).get("large") or info.get("cover", {}).get("medium")
            
            # Get the author name safely
            author_name = "Unknown"
            if "authors" in info:
                author_name = info["authors"][0]["name"]

            return {
                "title": info.get("title"),
                "author": author_name,
                "image": cover_url
            }
        else:
            frappe.msgprint("❌ Book not found in Open Library database.")
            return None

    except Exception as e:
        frappe.log_error(f"API Error: {str(e)}")
        return None