from django.urls import path
from .views import ExpenseListView, ExpenseDetailView

urlpatterns = [
    path('api/expenses/', ExpenseListView.as_view(), name='api_expenses_list'),
#ExpenseListView=afisare+creare
    path('api/expenses/<int:pk>/', ExpenseDetailView.as_view(), name='api_expenses_detail'),
#ExpenseListView=update+delete+details for one expense
    #poate sa nu fie api/
]
