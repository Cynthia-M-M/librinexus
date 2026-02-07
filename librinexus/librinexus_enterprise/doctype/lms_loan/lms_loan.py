# Copyright (c) 2026, An advanced LMS with Google Books API and Financial Logic. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class LMSLoan(Document):
    def before_insert(self):
        # Runs only once when you create the document
        if self.type == "Issue":
            self.validate_debt()
            self.validate_stock()
            self.update_stock(-1)
        elif self.type == "Return":
            self.update_stock(1)
            self.apply_fees()

    def validate_debt(self):    
        member = frappe.get_doc("LMS Member", self.member)
        if member.total_debt > 500:
            frappe.throw(f"🚫 Transaction Denied: {member.full_name} has a debt of KES {member.total_debt}. Limit is 500.")

    def validate_stock(self):
        # Ensure physical books
        book = frappe.get_doc("LMS Book", self.book)
        if book.available_copies < 1:
            frappe.throw(f"📚 {book.title} is out of stock!")

    def update_stock(self, change):
        # Automate inventory tracking
        book = frappe.get_doc("LMS Book", self.book)
        book.available_copies += change
        
        # Update Status automatically
        if book.available_copies > 0:
            book.status = "Available"
        else:
            book.status = "Out of Stock"
        book.save()

    def apply_fees(self):
        if not self.paid:
            # Get fee from the Book's Category
            # We fetch: Loan -> Book -> Category -> Fine Rate
            category_name = frappe.db.get_value("LMS Book", self.book, "category")
            fee = frappe.db.get_value("LMS Category", category_name, "daily_fine_rate") or 50
            
            # Add to member debt
            member = frappe.get_doc("LMS Member", self.member)
            member.total_debt += fee
            member.save()
            frappe.msgprint(f"💰 Rent Fee of KES {fee} has been added to {member.full_name}'s debt.")