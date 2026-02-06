from django.shortcuts import render, redirect
from .models import Scene, Artiste, Concert, MessageUrgent, Partenaire, TypePartenaire, MessageContact
from django.contrib import messages

# 🔹 PAGE D'ACCUEIL
def accueil(request):
    message_urgent = MessageUrgent.objects.filter(is_active=True).first()
    
    context = {
        'message_urgent': message_urgent
    }
    return render(request, 'monsite/index.html', context)

# 🔹 BILLETTERIE
def billetterie(request):
    return render(request, 'monsite/billetterie.html')

# 🔹 PAGE CONTACT
def contact(request):
    return render(request, 'monsite/contact.html')

# 🔹 FAQ
def faq(request):
    return render(request, 'monsite/faq.html')

# 🔹 PROGRAMMATION
def programmation(request):
    concerts = Concert.objects.all()
    scenes = Scene.objects.all().distinct()
    dates = Concert.objects.values_list('date_concert', flat=True).distinct()

    # Récupérer les concerts par scène si un filtre est appliqué
    scene_filter = request.GET.get('scene', '')
    if scene_filter:
        concerts = concerts.filter(scene__nom_scene=scene_filter)

    return render(request, 'monsite/programmation.html', {
        'concerts': concerts,
        'scenes': scenes,
        'dates': sorted(dates)  # Trie les dates pour qu'elles s'affichent dans l'ordre
    })

# 🔹 PARTENAIRES
def partenaires(request):
    # Récupérer tous les types de partenaires
    type_partenaire_list = TypePartenaire.objects.all()

    # Récupérer tous les partenaires
    partenaires = Partenaire.objects.all()

    # Récupérer le type de partenaire sélectionné dans l'URL (GET)
    selected_type = request.GET.get('type_partenaire', None)
    if selected_type:
        # Filtrer les partenaires en fonction du type sélectionné
        partenaires = partenaires.filter(type_partenaire__nom=selected_type)

    # Passer les partenaires et la liste des types de partenaires au template
    return render(request, 'monsite/partenaires.html', {
        'partenaires': partenaires,
        'type_partenaire_list': type_partenaire_list  # Passer la liste des types de partenaires
    })

def contact(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        email = request.POST['email']
        sujet = request.POST['sujet']
        message = request.POST['message']

        MessageContact.objects.create(nom=nom, email=email, sujet=sujet, message=message)

        messages.success(request, "Votre message a bien été envoyé !")
        return redirect('contact')  # Redirige l'utilisateur après soumission

    return render(request, 'monsite/contact.html')
