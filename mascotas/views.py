from django.shortcuts import render

# Create your views here.
def mis_mascotas(request):
        context = {
                "mascota1":"Zoe",
                "mascota2":"Ayun",
                "mascota3":"Negrito",
                "lista_mascotas": ["Zoe2", "Ayun2", "Negrito2"],
                "id": 0,
                "fecha": "2024/05/30"
        }
        return render(request,"mascotas.html",context)


def mascotas_id(request,id):
        print("el valor del id es",id)
        context = {
                "id":id
        }
        return render(request,"mascotas.html",context)