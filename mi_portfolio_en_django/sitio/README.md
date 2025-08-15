# Tu página en Django — Plantilla lista para pegar archivos

Esta plantilla te deja **subir directamente tu HTML, CSS, JS e imágenes** para que tu sitio estático funcione en Django.

## Estructura
```
tu_sitio_django/
├─ manage.py
├─ mysite/
│  ├─ __init__.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ asgi.py
│  └─ wsgi.py
├─ web/
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  └─ views.py
├─ templates/           ← pegá acá tus .html (index.html, about.html, etc.)
└─ static/              ← pegá acá css/js/img (respetando subcarpetas css, js, img)
   ├─ css/
   ├─ js/
   └─ img/
```

## Cómo usarlo
1. **Instalá dependencias**
   ```bash
   pip install -r requirements.txt
   ```

2. **Iniciá el proyecto**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

3. **Pegá tus archivos**
   - HTML → `templates/` (el archivo principal debería llamarse `index.html`).
   - CSS → `static/css/`
   - JS  → `static/js/`
   - Imágenes → `static/img/`

   Navegá a <http://127.0.0.1:8000/> para ver `index.html` y a rutas como `/about` para ver `templates/about.html`.

## Tips
- Si tu HTML original usa rutas relativas, actualizalas a `/static/...` para servir CSS/JS/imagenes (ej: `<link rel="stylesheet" href="/static/css/styles.css">`).
- Podés crear subcarpetas dentro de `templates/` (ej. `tienda/productos.html`) y acceder con `/tienda/productos`.
- En producción recordá ejecutar `python manage.py collectstatic` y configurar `STATIC_ROOT` en el servidor.

## Requisitos
- Python 3.10+
- Django 5.x