from django.urls import path
from products import views
urlpatterns = [
    path('<int:getCategory>',views.shop,name='shop'),
    path('pro<int:pro_id>',views.product_details,name='product_details'),
]
