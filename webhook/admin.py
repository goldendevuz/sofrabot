from django.contrib import admin

admin.site.site_header = "Goldendev admin"  # Title displayed at the top of the admin page
admin.site.site_title = "@goldendev"    # Title displayed in the browser tab
admin.site.index_title = "Webhook bot"  # Title displayed on the admin index page

from django.utils.html import format_html
from django.db import models as dj_models  # ✅ Avoid shadowing
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import BotUser

class BaseAdmin(admin.ModelAdmin):
    list_per_page = 10
    class Meta:
        abstract = True

# Helper to register admin class dynamically
def register_model(model):
    # Create dynamic resource class
    resource_class = type(
        f"{model.__name__}Resource",
        (resources.ModelResource,),
        {
            "Meta": type("Meta", (), {"model": model}),
        }
    )

    # Fields excluding 'id'
    # Detect ImageFields
    image_fields = [f.name for f in model._meta.fields if isinstance(f, dj_models.ImageField)]
    text_fields = [f.name for f in model._meta.fields if isinstance(f, dj_models.TextField)]

    # Exclude raw text fields from list_display
    fields = tuple(
        f.name for f in model._meta.fields
        if f.name != 'id' and f.name not in image_fields and f.name not in text_fields
    )

    # Base admin attributes
    admin_attrs = {
        "resource_classes": [resource_class],
        "list_display": list(fields),
        "list_filter": fields,
        "search_fields": fields,
    }
        
    for field in text_fields:
        method_name = f"short_{field}"

        def make_text_preview(field_name):
            def short_text(self, obj):
                val = getattr(obj, field_name)
                return (val[:47] + "...") if val and len(val) > 50 else val
            short_text.short_description = field_name
            return short_text

        admin_attrs[method_name] = make_text_preview(field)
        admin_attrs["list_display"].insert(0, method_name)

    # Add custom image display methods
    for field in image_fields:
        method_name = f"show_{field}"

        def make_thumb_func(field_name):
            def thumb(self, obj):
                val = getattr(obj, field_name)
                if val and hasattr(val, 'url'):
                    return format_html(
                        '<a href="{0}" target="_blank">'
                        '<img src="{0}" width="100" height="100" style="object-fit: cover; border-radius: 4px;" />'
                        '</a>',
                        val.url
                    )
                return "-"
            thumb.short_description = field_name
            thumb.allow_tags = True  # optional in modern Django
            return thumb

        admin_attrs[method_name] = make_thumb_func(field)
        admin_attrs["list_display"].append(method_name)



    # Create and register the admin class
    admin_class = type(
        f"{model.__name__}Admin",
        (ImportExportModelAdmin, BaseAdmin),
        admin_attrs
    )

    admin.site.register(model, admin_class)

# ✅ Avoid shadowing django.db.models by renaming this list
registered_models = [
    BotUser
]

for model in registered_models:
    register_model(model)