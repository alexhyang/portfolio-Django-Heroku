from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.register, name="register"),
    path("save", views.save, name="save"),
    path("wordlists", views.wordlists, name="wordlist_index"),
    path("add_list", views.add_list, name="add_list"),
    path("wordlists/<str:name>", views.wordlist, name="wordlist"),
    path("wordlists/<str:name>/remove", views.remove_list, name="remove_list")
]