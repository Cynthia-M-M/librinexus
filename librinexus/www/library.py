import frappe

def get_context(context):
    # 1. GET URL PARAMETERS (Search & Category)
    search_query = frappe.form_dict.get("search")
    category_filter = frappe.form_dict.get("category")
    
    # Pass these back to HTML so we can highlight the active tab
    context.search_query = search_query
    context.current_category = category_filter or "All"

    # 2. IF SEARCHING (Global Search)
    if search_query:
        context.search_mode = True
        context.search_results = frappe.get_all("LMS Book", 
            fields=["name", "route", "title", "author", "cover_image", "status", "category", "price"],
            filters={"title": ["like", f"%{search_query}%"]},
            ignore_permissions=True
        )
        return

    # 3. IF NOT SEARCHING -> APP MODE
    context.search_mode = False
    
    # Hero Book (Always show the latest Featured book)
    context.hero_book = frappe.db.get_value("LMS Book", 
        {"cover_image": ["is", "set"], "description": ["is", "set"]}, 
        ["name", "route", "title", "author", "cover_image", "description", "price"], 
        order_by="creation desc",
        as_dict=True
    )

    # 4. FILTER LOGIC (Making the Links Real)
    filters = {}
    if category_filter and category_filter != "All":
        filters["category"] = category_filter

    # Fetch books based on the filter
    context.all_books = frappe.get_all("LMS Book",
        fields=["name", "route", "title", "author", "cover_image", "status", "category", "price", "is_premium"],
        filters=filters,
        order_by="creation desc",
        ignore_permissions=True
    )

    # 5. FETCH "TECH" SPECIFICALLY (For the Horizontal Scroll)
    context.tech_books = frappe.get_all("LMS Book",
        fields=["name", "route", "title", "author", "cover_image", "status", "price", "is_premium"],
        filters={"category": "Tech"},
        limit=5,
        ignore_permissions=True
    )