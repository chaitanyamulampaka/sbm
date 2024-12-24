from django.contrib import admin
from app.models import pcards
from app.models import productViewer
from app.models import Profile,Cart,CartItem,Address
class pcardsAdmin(admin.ModelAdmin):
    list_display=('product_id','pcardimg','pcardname','pcardcost','pcarddiscount','pcardoldprice','pcardrating')
admin.site.register(pcards,pcardsAdmin)
class productViewerAdmin(admin.ModelAdmin):

    list_display=('product_id','smallimg1','smallimg2','smallimg3','smallimg4','mainimg','productdescription')
 
admin.site.register(productViewer,productViewerAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','username', 'fname', 'mobile')
admin.site.register(Profile,ProfileAdmin)
# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display=('user',)
admin.site.register(Cart,CartAdmin)

class CartItemAdmin(admin.ModelAdmin):
    list_display=('cart','product','quantity')
admin.site.register(CartItem,CartItemAdmin)

class AdressAdmin(admin.ModelAdmin):
    list_display=('user','name','a_mobile','pincode','state','city','house_no','area','landmark')
admin.site.register(Address,AdressAdmin)