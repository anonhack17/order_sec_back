from django.contrib import admin

from .models import Policy, BypassSheet, BypassSheetField, Standard, Procedure


class BypassSheetInline(admin.TabularInline):  # Или используйте admin.StackedInline для вертикального отображения
    model = BypassSheetField
    extra = 4


@admin.register(BypassSheet)
class BypassSheetFieldAdmin(admin.ModelAdmin):
    inlines = [BypassSheetInline]


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)


@admin.register(Standard)
class StandardAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)


@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)
