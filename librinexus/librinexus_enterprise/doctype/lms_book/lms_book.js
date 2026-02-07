// Copyright (c) 2026, An advanced LMS with Google Books API and Financial Logic. and contributors
// For license information, please see license.txt

frappe.ui.form.on('LMS Book', {
    refresh: function(frm) {
        // Add a custom button to the form
        frm.add_custom_button('Fetch Data from Google', () => {
            
            if (!frm.doc.isbn) {
                frappe.msgprint("⚠️ Please enter an ISBN first!");
                return;
            }

            frappe.call({
                method: "librinexus.api.fetch_google_book",
                args: { isbn: frm.doc.isbn },
                callback: (r) => {
                    if (r.message) {
                        frm.set_value('title', r.message.title);
                        frm.set_value('author', r.message.author);
                        frm.set_value('cover_image', r.message.image);
                        frappe.msgprint("✅ Book details fetched successfully!");
                    } else {
                        frappe.msgprint("❌ Book not found on Google Books.");
                    }
                }
            });
        });
    }
});
