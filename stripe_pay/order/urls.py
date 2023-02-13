from django.urls import path

from . import views

app_name = 'order'


urlpatterns = [
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path(
        'buy/<int:item_id>/',
        views.create_checkout_session,
        name='item_checkout'
    ),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('cancel/', views.CancelView.as_view(), name='cancel'),
]
