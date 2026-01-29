from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Personnel # Importe ton modèle Personnel
from django.db import transaction

from django.contrib.auth import authenticate, login, logout
def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
      

        # Vérification si l'utilisateur existe déjà
        if User.objects.filter(email=email).exists():
            messages.error(request, "Cet email est déjà enregistré.")
            return redirect('register')

        try:
            # On utilise une 'transaction' pour s'assurer que si l'un échoue, rien n'est créé
            with transaction.atomic():
                # 1. Création de l'utilisateur de base
                user = User.objects.create_user(
                    username=email, # On utilise l'email comme identifiant
                    email=email,
                    password=password,
                    first_name=prenom,
                    last_name=nom
                )
                
                # 2. Création du profil Personnel lié
                personnel = Personnel.objects.create(
                    user=user,
                    first_name=nom,
                    last_name=prenom,
                    email=email,
                )
                
                messages.success(request, f"L'utilisateur {nom} a été enregistré avec succès.")
                return redirect('/login/')

        except Exception as e:
            messages.error(request, "Une erreur est survenue lors de l'enregistrement.")
            print(f"Erreur : {e}")

    return render(request, 'register.html')
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Django utilise par défaut 'username', mais nous passons l'email ici
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            
            # Vérification si c'est un membre du personnel pour un message personnalisé
            is_staff = hasattr(user, 'personnel')
            if is_staff:
                messages.success(request, f"Bon retour, {user.last_name} ! L'interface Personnel est prête. 🍁")
            else:
                messages.success(request, "Connexion réussie. Prêt pour le NCLC 10 ?")
            
            return redirect('dashboard') # Redirige vers ta page d'accueil
        else:
            # Message d'erreur si les identifiants sont faux
            messages.error(request, "Identifiants invalides. Veuillez réessayer.")
            return redirect('login')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté. À bientôt !")
    return redirect('login')
def home(request):
    return render(request, 'index.html')


def login_view(request):
    return render(request, 'authentification/login.html')


def register_view(request):
    return render(request, 'authentification/register.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def forgot_password_view(request):
    return render(request, 'authentification/forgot_password.html')


def verificationotp(request):
    return render(request, 'authentification/otp_code.html')


def admin_view(request):
    return render(request, 'configurations/configurations.html')

