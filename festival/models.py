from django.db import models

class Scene(models.Model):
    nom_scene = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom_scene

class Artiste(models.Model):
    nom = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='artistes/', blank=True, null=True)

    def __str__(self):
        return self.nom

class Concert(models.Model):
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE)
    date_concert = models.DateField()
    heure_concert = models.TimeField()

    def __str__(self):
        return f"{self.artiste.nom} - {self.scene.nom_scene} ({self.date_concert})"




class TypePartenaire(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Partenaire(models.Model):
    nom = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    type_partenaire = models.ForeignKey(TypePartenaire, on_delete=models.CASCADE)
    website_du_partenaire = models.URLField()  # Le site web du partenaire

    def __str__(self):
        return self.nom

class MessageContact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=100)
    message = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    reponse = models.TextField(blank=True, null=True)  # Champ de réponse

    def __str__(self):
        return f"{self.nom} - {self.sujet}"

