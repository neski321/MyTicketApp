from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from frontapp.models import AccountType
from frontapp import models as fm

# Register your models here.
class AccTypeInline(admin.StackedInline):
    model = AccountType
    can_delete = False
    verbose_name_plural = "Account Type"

class BalanceInline(admin.StackedInline):
    model = fm.Balance
    can_delete = False
    verbose_name_plural = "Balance"

class AccTypeAdmin(UserAdmin):
    #makes the addview in the admin panel not have inlines
    def add_view(self, *args, **kwargs):
        self.inlines = []
        return super(AccTypeAdmin, self).add_view(*args, **kwargs)
    
    #Makes so change view has the inlines
    def change_view(self, *args, **kwargs):
        self.inlines = [AccTypeInline, BalanceInline]
        return super(AccTypeAdmin, self).change_view(*args, **kwargs)



admin.site.unregister(User)
admin.site.register(User, AccTypeAdmin)

#checking promoters in system
admin.site.register(fm.Promoter)
admin.site.register(fm.VenueOwner)
admin.site.register(fm.Concert)
admin.site.register(fm.TicketOrder)