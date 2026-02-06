from django.test import TestCase
from .models import Scene, Artiste, Concert, MessagesUrgents, TypePartenaire, Partenaire, MessageContact
from django.utils import timezone
from django.contrib.messages import get_messages
from django.urls import reverse

class SceneModelTest(TestCase):
    def test_scene_creation(self):
        scene = Scene.objects.create(nom_scene="Zeus")
        self.assertEqual(scene.nom_scene, "Zeus")
        self.assertEqual(str(scene), "Zeus")  # Test de la méthode __str__

class ArtisteModelTest(TestCase):
    def test_artiste_creation(self):
        artiste = Artiste.objects.create(nom="Artiste Test")
        self.assertEqual(artiste.nom, "Artiste Test")
        self.assertEqual(str(artiste), "Artiste Test")  # Test de la méthode __str__

    def test_artiste_with_photo(self):
        artiste = Artiste.objects.create(nom="Artiste Photo", photo="artistes/photo.jpg")
        self.assertEqual(artiste.photo, "artistes/photo.jpg")

class ConcertModelTest(TestCase):
    def test_concert_creation(self):
        artiste = Artiste.objects.create(nom="Artiste Test")
        scene = Scene.objects.create(nom_scene="Nebula")
        concert = Concert.objects.create(
            artiste=artiste,
            scene=scene,
            date_concert="2025-03-26",
            heure_concert="20:00"
        )
        self.assertEqual(concert.artiste.nom, "Artiste Test")
        self.assertEqual(concert.scene.nom_scene, "Zeus")
        self.assertEqual(str(concert), "Artiste Test - Zeus (2025-03-26)")  # Test de la méthode __str__

class MessagesUrgentsModelTest(TestCase):
    def test_message_urgent_creation(self):
        message = MessagesUrgents.objects.create(message="Important message!")
        self.assertEqual(message.message, "Important message!")
        self.assertTrue(message.is_active)  # Par défaut, is_active doit être True
        self.assertIsInstance(message.created_at, timezone.datetime)  # Test de la date de création
        self.assertEqual(str(message), "Important message!")  # Test de la méthode __str__

    def test_message_urgent_inactive(self):
        message = MessagesUrgents.objects.create(message="Inactive message", is_active=False)
        self.assertFalse(message.is_active)  # Vérifier que is_active est False

class TypePartenaireModelTest(TestCase):
    def test_type_partenaire_creation(self):
        type_partenaire = TypePartenaire.objects.create(nom="Sponsor")
        self.assertEqual(type_partenaire.nom, "Sponsor")
        self.assertEqual(str(type_partenaire), "Sponsor")  # Test de la méthode __str__

class PartenaireModelTest(TestCase):
    def test_partenaire_creation(self):
        type_partenaire = TypePartenaire.objects.create(nom="Sponsor")
        partenaire = Partenaire.objects.create(
            nom="Partenaire Test",
            logo="logos/logo.jpg",
            type_partenaire=type_partenaire,
            website_du_partenaire="http://www.example.com"
        )
        self.assertEqual(partenaire.nom, "Partenaire Test")
        self.assertEqual(partenaire.logo, "logos/logo.jpg")
        self.assertEqual(partenaire.website_du_partenaire, "http://www.example.com")
        self.assertEqual(str(partenaire), "Partenaire Test")  # Test de la méthode __str__

class MessageContactModelTest(TestCase):
    def test_message_contact_creation(self):
        message_contact = MessageContact.objects.create(
            nom="Client Test",
            email="client@example.com",
            sujet="Question",
            message="This is a test message."
        )
        self.assertEqual(message_contact.nom, "Client Test")
        self.assertEqual(message_contact.email, "client@example.com")
        self.assertEqual(message_contact.sujet, "Question")
        self.assertEqual(message_contact.message, "This is a test message.")
        self.assertIsInstance(message_contact.date_creation, timezone.datetime)  # Test de la date de création
        self.assertEqual(str(message_contact), "Client Test - Question")  # Test de la méthode __str__

    def test_message_contact_with_response(self):
        message_contact = MessageContact.objects.create(
            nom="Client Test",
            email="client@example.com",
            sujet="Question",
            message="This is a test message.",
            reponse="Here is the answer."
        )
        self.assertEqual(message_contact.reponse, "Here is the answer.")  # Vérifier la réponse

class ViewsTestCase(TestCase):

    def setUp(self):
        """Création des objets nécessaires aux tests"""
        # Créer des scènes, artistes et concerts
        self.scene_zeus = Scene.objects.create(nom_scene="Zeus")
        self.artiste_test = Artiste.objects.create(nom="Artiste Test")
        self.concert_test = Concert.objects.create(
            artiste=self.artiste_test,
            scene=self.scene_zeus,
            date_concert="2025-03-26",
            heure_concert="20:00"
        )
        self.type_partenaire = TypePartenaire.objects.create(nom="Sponsor")
        self.partenaire_test = Partenaire.objects.create(
            nom="Partenaire Test",
            logo="path_to_logo",
            type_partenaire=self.type_partenaire,
            website_du_partenaire="https://www.partenaire.com"
        )
        self.message_urgent = MessagesUrgents.objects.create(message="Message Urgent", is_active=True)

        # URLS
        self.url_accueil = reverse('accueil')  # page d'accueil
        self.url_billetterie = reverse('billetterie')  # page billetterie
        self.url_contact = reverse('contact')  # page contact
        self.url_faq = reverse('faq')  # page FAQ
        self.url_programmation = reverse('programmation')  # page programmation
        self.url_partenaires = reverse('partenaires')  # page partenaires

    def test_accueil_view(self):
        response = self.client.get(self.url_accueil)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nation Sound Festival")
        self.assertContains(response, self.message_urgent.message)

    def test_billetterie_view(self):
        """Test pour vérifier que la page de billetterie s'affiche correctement"""
        response = self.client.get(self.url_billetterie)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Billetterie")

    def test_contact_view_get(self):
        """Test pour vérifier que la page de contact s'affiche correctement"""
        response = self.client.get(self.url_contact)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contact")

    def test_contact_view_post(self):
        """Test pour vérifier la soumission du formulaire de contact"""
        response = self.client.post(self.url_contact, {
            'nom': 'Test User',
            'email': 'test@example.com',
            'sujet': 'Demande',
            'message': 'Message de test'
        })
        self.assertEqual(response.status_code, 302)  # Redirection après soumission
        self.assertRedirects(response, self.url_contact)
        
        # Vérifier que le message de succès a été ajouté
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Votre message a bien été envoyé !")

    def test_faq_view(self):
        """Test pour vérifier que la page FAQ s'affiche correctement"""
        response = self.client.get(self.url_faq)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "FAQ")

    def test_programmation_view(self):
        """Test pour vérifier que la page programmation fonctionne avec et sans filtre"""
        # Test sans filtre
        response = self.client.get(self.url_programmation)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Programmation")
        self.assertContains(response, self.concert_test.artiste.nom)
        self.assertContains(response, self.scene_zeus.nom_scene)
        
        # Test avec filtre par scène
        response = self.client.get(self.url_programmation + '?scene=Zeus')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.concert_test.artiste.nom)
        self.assertContains(response, self.scene_zeus.nom_scene)

    def test_partenaires_view(self):
        """Test pour vérifier que la page des partenaires fonctionne avec et sans filtre"""
        # Test sans filtre
        response = self.client.get(self.url_partenaires)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Partenaires")
        self.assertContains(response, self.partenaire_test.nom)

        # Test avec filtre par type de partenaire
        response = self.client.get(self.url_partenaires + f'?type_partenaire={self.type_partenaire.nom}')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.partenaire_test.nom)

    def test_invalid_url(self):
        """Test pour vérifier qu'une URL invalide retourne une page 404"""
        response = self.client.get('/url_invalide/')
        self.assertEqual(response.status_code, 404)