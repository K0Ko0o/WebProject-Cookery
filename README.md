# 🍳 Cookery Web Application

A Django-powered web application for managing recipes, ingredients, and kitchen inventories. Designed with a responsive Bootstrap 5 UI and `django-crispy-forms` for clean user interaction.

---

## 🚀 Features

* **Recipe Management**: Create, edit, view, and organize culinary recipes.
* **Ingredient Tracking**: Manage individual ingredients, track caloric content per 100g, and associate items with preferred supermarkets.
* **Dynamic Search & Filtering**: Filter ingredients by supermarket and categories directly through custom Django forms.
* **Responsive Interface**: Built using Bootstrap 5 and Crispy Forms for mobile and desktop compatibility.
* **Environment-Based Configuration**: Secure configuration managed via `.env` files using `python-dotenv`.

---

## 🛠️ Tech Stack

* **Backend**: Python 3.x, Django 4.2+
* **Frontend**: HTML5, CSS3, Bootstrap 5, Django Crispy Forms (`crispy-bootstrap5`)
* **Database**: SQLite3 (Development)
* **Environment Management**: `python-dotenv`

---

## 📂 Project Structure

```text
WebProject-Cookery/
├── common/             # Shared views, context processors, and utilities
├── ingredients/        # Ingredient models, forms, and views
├── recipes/            # Recipe management logic and templates
├── djangoproject/      # Core settings and URL configuration
├── templates/          # Global templates and layout wrappers
│   └── shared/         # Shared components (navbar, base layout)
├── static/             # Static assets (CSS, JS, images)
├── media/              # User-uploaded images (ingredient images)
├── .env.example        # Environment variable blueprint
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
