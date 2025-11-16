ROLE_MENUS = {
    "management": [
        {"name": "Dashboard", "url": "core:manager_dashboard", "icon": "ni-dashboard"},
        {"name": "Ailixir AI", "url": "ai:startchat", "icon": "ni-cpu"},
        {"name": "Add Staff", "url": "staff:add", "icon": "ni-user-add"},
        {"name": "List Staff", "url": "staff:list", "icon": "ni-users"},
    ],

    "admin": [
        {"name": "Dashboard", "url": "core:admin_dashboard", "icon": "ni-dashboard"},
        {"name": "Ailixir AI", "url": "ai:startchat", "icon": "ni-cpu", "perm": "ai.add_chatsession"},
        {"name": "Add Staff", "url": "staff:add", "icon": "ni-user-add", "perm": "staff.add_staffprofile"},
        {"name": "List Staff", "url": "staff:list", "icon": "ni-users"},
        {"name": "Notifications", "url": "notifications:list", "icon": "ni-bell"},
        {"name": "Send Notifications", "url": "notifications:create", "icon": "ni-plus"},
        {"name": "Products", "url": "products:list", "icon": "ni-package"},
        {"name": "Add Product", "url": "products:add", "icon": "ni-plus", "perm": "product.add_product"},
        {"name": "Add Category", "url": "products:category_add", "icon": "ni-folder-plus", "perm": "product.add_productcategory"},
        {"name": "Permissions", "url": "permissions:role_list", "icon": "ni-lock", "perm": "auth.view_permission"},
        {"name": "Research Experiments", "url": "research:experiment_list", "icon": "ni-book"},
        {"name": "Add Experiment","url": "research:experiment_add","icon": "ni-plus-circle",},
        {"name": "Lab Notes","url": "research:labnote_list","icon": "ni-notes",},

        #{"name": "Settings", "url": "core:settings", "icon": "ni-setting"},
    ],

    "sales": [
        {"name": "Dashboard", "url": "core:sale_dashboard", "icon": "ni-dashboard"},
        {"name": "Ailixir AI", "url": "ai:startchat", "icon": "ni-cpu"},
        {"name": "Customers", "url": "sales:customers", "icon": "ni-users"},
    ],

    "production": [
        {"name": "Dashboard", "url": "core:production_dashboard", "icon": "ni-dashboard"},
        {"name": "Production Tasks", "url": "production:tasks", "icon": "ni-briefcase"},
        {"name": "Inventory", "url": "production:inventory", "icon": "ni-archive"},
    ],

    "research": [
        {"name": "Dashboard", "url": "core:research_dashboard", "icon": "ni-dashboard"},
        {"name": "Ailixir AI", "url": "ai:startchat", "icon": "ni-cpu"},
        {"name": "Lab Notes", "url": "research:lab_notes", "icon": "ni-notes"},
    ],

    "quality": [
        {"name": "Dashboard", "url": "core:quality_dashboard", "icon": "ni-dashboard"},
        {"name": "Quality Reports", "url": "quality:reports", "icon": "ni-report"},
        {"name": "Ailixir AI", "url": "ai:startchat", "icon": "ni-cpu"},
    ],

    "customer": [
        {"name": "Dashboard", "url": "core:customer_dashboard", "icon": "ni-dashboard"},
        {"name": "Support Tickets", "url": "support:tickets", "icon": "ni-help-fill"},
    ],

    "logistics": [
        {"name": "Dashboard", "url": "core:logistic_dashboard", "icon": "ni-dashboard"},
        {"name": "Deliveries", "url": "logistics:deliveries", "icon": "ni-truck"},
    ],
}