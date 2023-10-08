from os import name
from unittest.mock import patch
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register(r"grupos",views.GrupoViewSet)
router.register(r"activos",views.ActivoViewSet)
router.register(r"personal",views.PersonalViewSet)

urlpatterns = [
    
    #path("contact/<str:name>", views.contact, name="index"),
    path("/<str:name>", views.index, name="index"),
    #path("grupos/", views.grupos, name="grupos"),
    #path("activos/", views.activos, name="activos"), 

    path('',include(router.urls)),
    path('activos/grupo/<str:grupo>',views.activo_grupo_contab,)
]