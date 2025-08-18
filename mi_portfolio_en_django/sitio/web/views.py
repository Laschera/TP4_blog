from django.shortcuts import render
from django.http import Http404

def index(request):
    # Renderiza templates/index.html por defecto
    return render(request, "index.html")

def page(request, page):
    # Permite renderizar cualquier otra plantilla: templates/<page>.html
    # Ej: /about -> templates/about.html ; /tienda/productos -> templates/tienda/productos.html
    template_name = f"{page}.html"
    try:
        return render(request, template_name)
    except Exception:
        raise Http404("Página no encontrada: " + template_name)
    