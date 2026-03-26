from django.urls import path
from .views import dashboard, password_reset_mock, product_create, product_delete, product_list, product_update

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("productos/", product_list, name="product_list"),
    path("productos/nuevo/", product_create, name="product_create"),
    path("productos/<int:pk>/editar/", product_update, name="product_update"),
    path("productos/<int:pk>/eliminar/", product_delete, name="product_delete"),
    path("recuperar/", password_reset_mock, name="password_reset_mock"),
]
