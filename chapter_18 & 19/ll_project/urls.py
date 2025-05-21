from django.contrib import admin
from django.urls import path

from django.urls import path
from . import views

"""
URL configuration for ll_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',('accounts.urls')),
    path('',('learning_logs.urls')),
]

"""Defines URL patterns for learning_logs."""

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    
    # Page for adding a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for adding a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for adding a new entry.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]