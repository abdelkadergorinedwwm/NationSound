from django.contrib import admin
from .models import Scene, Concert, Artiste, MessagesUrgents, Partenaire, TypePartenaire, MessageContact
from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import format_html
from django.shortcuts import render
from django.http import HttpResponse


# --- Artiste Admin ---
@admin.register(Artiste)
class ArtisteAdmin(admin.ModelAdmin):
    list_display = ('nom',)  # Affichage uniquement du nom de l'artiste
    search_fields = ('nom',)  # Recherche par nom


# --- Concert Admin ---
@admin.register(Concert)
class ConcertAdmin(admin.ModelAdmin):
    list_display = ('artiste', 'scene', 'date_concert', 'heure_concert')  # Affichage des concerts avec artiste, scène, date et heure
    list_filter = ('scene', 'date_concert')  # Filtre par scène et date


# --- Scene Admin ---
@admin.register(Scene)
class SceneAdmin(admin.ModelAdmin):
    list_display = ('nom_scene',)  # Affichage uniquement du nom de la scène


# --- Messages Urgents Admin ---
@admin.register(MessagesUrgents)
class MessagesUrgentsAdmin(admin.ModelAdmin):
    list_display = ('message', 'is_active', 'created_at')  # Affichage du message, état actif et date de création
    list_filter = ('is_active',)  # Filtre pour l'état du message (actif ou non)


@admin.register(Partenaire)
class PartenaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type_partenaire', 'website_du_partenaire', 'logo_preview')
    list_filter = ('type_partenaire',)  # Permet de trier par type de partenaire
    search_fields = ('nom', 'type_partenaire__nom')  # Recherche par nom et type de partenaire

    def logo_preview(self, obj):
        if obj.logo:
            return f'<img src="{obj.logo.url}" width="50" height="50" />'
        return "Pas d'image"
    logo_preview.allow_tags = True
    logo_preview.short_description = "Aperçu du logo"

@admin.register(TypePartenaire)
class TypePartenaireAdmin(admin.ModelAdmin):
    list_display = ('nom',)





