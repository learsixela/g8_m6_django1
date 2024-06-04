from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User

# Create your views here.
def about(request):
    return render(request,"about.html",{})

def index(request):
    return render(request,"index.html",{})

def hola(request):
    return HttpResponse("""
    <h1>Hola Mundo</h1>
    <p>Este es mi primer html desde django</p> 
    """)

def test(request):
	return HttpResponse("""
			<h1>Esta es otra pagina</h1>
			<p>este es otro parrafo</p>
			<img src="" alt="imagen de prueba">
	""")

def home(request):
    return HttpResponse("""
		<!doctype html>
		<html lang="en">

		<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>Home::</title>
		<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
				integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
		</head>

		<body>
		<h1>Hello, world!</h1>
		<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
				integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
				crossorigin="anonymous"></script>
		</body>

		</html>
                
    """)

def contact(request):
    return HttpResponse("""
		<!doctype html>
		<html lang="en">

		<head>
			<meta charset="utf-8">
			<meta name="viewport" content="width=device-width, initial-scale=1">
			<title>Contact::</title>
			<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
				integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
		</head>

		<body>
			<div class="container">
				<div class="mb-3">
					<label for="exampleFormControlInput1" class="form-label">Email address</label>
					<input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
				</div>
				<div class="mb-3">
					<label for="exampleFormControlTextarea1" class="form-label">Example textarea</label>
					<textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
				</div>
			</div>
			<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
				integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
				crossorigin="anonymous"></script>
		</body>

		</html>
    """)


def login(request):
    if request.method =="GET":
            print("Estoy en login get")
            return render(request,"login.html")
    
    if request.method =="POST":
            print("Estoy en login post")
            return redirect("/")
        
def registro(request):
    if request.method == "GET":
        return render(request,"registro.html",{})
    
    if request.method == "POST":
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
		#creacion de usuario
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        context = {
            "email":request.POST['email'],
        }

        request.session["email"]= request.POST['email']

        return render(request,"index.html",context)