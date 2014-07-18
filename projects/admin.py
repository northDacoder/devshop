from django.contrib import admin
from models import *


class CompanyAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('name',)



class ProjectAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('name',)



class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(User)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Developer, DeveloperAdmin)
