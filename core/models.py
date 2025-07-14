from django.db import models

class Tournament(models.Model):
    name = models.CharField(max_length=200)
    game = models.CharField(max_length=100)
    prize_pool = models.CharField(max_length=100)
    date = models.DateTimeField()
    banner = models.ImageField(upload_to='tournament_banners/')
    description = models.TextField(blank=True)
    registration_link = models.URLField(blank=True, help_text='Google Form or registration link')

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='team_logos/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    photo = models.ImageField(upload_to='player_photos/', blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='sponsor_logos/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    banner = models.ImageField(upload_to='blog_banners/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(upload_to='testimonial_photos/', blank=True)

    def __str__(self):
        return self.name

class Stream(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    platform = models.CharField(max_length=20, choices=[('twitch', 'Twitch'), ('youtube', 'YouTube')])

    def __str__(self):
        return f"{self.name} ({self.platform})"

class SocialLink(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    icon = models.CharField(max_length=50, help_text='FontAwesome icon class, e.g., fab fa-twitter')

    def __str__(self):
        return self.name
