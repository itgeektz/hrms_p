import frappe
from frappe.model.delete_doc import check_if_doc_is_linked

def custom_before_cancel(doc, method="Cancel"):
    if doc.doctype == "Salary Structure Assignment":
        # Specify the DocTypes you want to ignore
        doc.ignore_linked_doctypes = ["Salary Slip"]
        