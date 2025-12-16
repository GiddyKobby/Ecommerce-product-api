# E-commerce Product API (Django + DRF)

![GitHub last commit](https://img.shields.io/github/last-commit/giddykobby/Ecommerce-product-api)
![GitHub repo size](https://img.shields.io/github/repo-size/giddykobby/Ecommerce-product-api)
![GitHub issues](https://img.shields.io/github/issues/giddykobby/Ecommerce-product-api)
![GitHub stars](https://img.shields.io/github/stars/giddykobby/Ecommerce-product-api?style=social)

> **Status:** In Development  
> **Tech Stack:** Django · Django REST Framework · SQLite  
> **Role:** Backend Developer (Capstone Project)  
> **Goal:** Build a fully functional E-commerce Product API with authentication, search, filtering, and deployment.

---

## 📌 Overview
This is my Backend Development Capstone Project built using **Python**, **Django**, and **Django REST Framework**.  
The API supports product management, user authentication, search, filtering, and pagination.

---

## 🚀 Features
- Product CRUD (Create, Read, Update, Delete)
- Category management
- User authentication (Django Auth / JWT)
- Role-based access control (Admin vs User)
- Product search by name or category
- Filtering (price range, category, stock availability)
- Pagination
- Admin dashboard for product & category management

---

## 🛠 Tech Stack
- Python 3
- Django 5+
- Django REST Framework
- SQLite (development)
- GitHub + Git for version control

---

## 📁 Project Structure

ecommerce-api/
├── config/ # Django project settings
├── products/ # Product app (models, views, serializers)
├── docs/ # Screenshots & documentation
├── manage.py
└── requirements.txt



---

## 🗺 Project Roadmap

### ✅ Phase 1: Setup
- [x] Create Django project
- [x] Configure DRF
- [x] Add Product & Category models
- [x] Register models in admin
- [] Push initial project to GitHub

### 🚧 Phase 2: Core API
- [x] Product CRUD (Create, Read, Update, Delete)
- [x] Category CRUD
- [x] User authentication (JWT)
- [x] Role-based permissions (Admin-only create/update/delete, authenticated users read-only)


### 🔍 Phase 3: Search & Filters
- [ ] Search by product name
- [ ] Filter by category
- [ ] Price range filter
- [ ] Stock availability filter
- [ ] Pagination on product listing

### 🌐 Phase 4: Deployment
- [ ] Prepare `requirements.txt`
- [ ] Setup environment variables
- [ ] Deploy to PythonAnywhere / Render / Heroku
- [ ] Test all deployed endpoints

### ⭐ Phase 5: Stretch Goals
- [ ] Product reviews
- [ ] Wishlist
- [ ] Discounts & promotions
- [ ] Multiple product images

---

## 📌 How to Run Locally

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# or source venv/bin/activate for Mac/Linux

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

👨‍💻 Author

Gideon Osei Acheampong
Backend Developer (Python / Django)

