# install.py

import frappe

def after_migrate():
    create_custom_fields()

def create_custom_fields():
    custom_fields = [
        # Add your custom field definitions here
        {
            "doctype": "Custom Field",
            "dt": "Company",
            "fieldname": "default_maintenance_tax_template",
            "fieldtype": "Link",
            "label": "Default Maintenance Tax Template",
            "options": "Tax Template",
            "insert_after": "tax_id"
        },
        # Repeat for each custom field needed
    ]

    for field in custom_fields:
        create_custom_field(field)

def create_custom_field(field_data):
    if not frappe.db.exists("Custom Field", field_data["fieldname"]):
        custom_field = frappe.get_doc({
            "doctype": "Custom Field",
            **field_data
        })
        custom_field.insert()
