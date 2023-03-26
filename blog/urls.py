from django.urls import path
from blog import views

urlpatterns = [
    path('blog/', views.BlogList.as_view()),
]
