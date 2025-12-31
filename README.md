# 📿 Azkar - Islamic Remembrance Application

<div align="center">

![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A beautiful and intuitive Django web application for managing and browsing Islamic Adhkar (remembrances). Organize your daily Dhikr by categories, search through your collection, and maintain a personal library of Islamic supplications.

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [API](#-api-endpoints) • [Contributing](#-contributing)

</div>

---

## ✨ Features

- 🕌 **Dhikr Management** - Full CRUD operations for Islamic remembrances
- 📂 **Category Organization** - Organize Adhkar by categories (Morning, Evening, Prayer, etc.)
- 🔍 **Search Functionality** - Quickly find specific Dhikr with powerful search
- ⬅️ ➡️ **Navigation** - Easy previous/next navigation between Dhikr entries
- 📱 **Responsive Design** - Beautiful interface that works on all devices
- 🚀 **Production Ready** - Configured with Gunicorn for deployment

---

## 🛠️ Tech Stack

| Technology       | Purpose                |
| ---------------- | ---------------------- |
| **Django 6.0**   | Web Framework          |
| **Python 3.12+** | Programming Language   |
| **SQLite**       | Database               |
| **Gunicorn**     | Production WSGI Server |
| **HTML/CSS**     | Frontend Templates     |

---

## 📦 Installation

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)
- Git

### Quick Start

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/azkar_project.git
   cd azkar_project
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**

   ```bash
   python manage.py runserver
   ```

7. **Open your browser**
   ```
   http://127.0.0.1:8000
   ```

---

## 🚀 Usage

### Browsing Adhkar

- **Home Page**: View all Dhikr entries
- **Categories**: Browse Dhikr organized by category
- **Search**: Use the search bar to find specific Dhikr

### Managing Adhkar

- **Add New Dhikr**: Create new remembrance entries
- **Edit Dhikr**: Modify existing entries
- **Delete Dhikr**: Remove entries from your collection

### Admin Panel

Access the Django admin panel at `/admin/` to manage:

- Categories
- Dhikr entries
- Users

---

## 📁 Project Structure

```
azkar_project/
├── azkar/                  # Main application
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates
│   │   ├── base.html           # Base template
│   │   ├── all_dhikr.html      # All Dhikr listing
│   │   ├── category_list.html  # Category listing
│   │   ├── dhikr_detail.html   # Single Dhikr view
│   │   ├── dhikr_by_category.html
│   │   ├── add_dhikr.html      # Add new Dhikr
│   │   └── edit_dhikr.html     # Edit Dhikr
│   ├── admin.py            # Admin configuration
│   ├── forms.py            # Django forms
│   ├── models.py           # Database models
│   ├── urls.py             # URL routing
│   └── views.py            # View functions
├── core/                   # Project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # Root URL configuration
│   ├── wsgi.py             # WSGI configuration
│   └── asgi.py             # ASGI configuration
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
├── Procfile                # Heroku deployment config
└── README.md               # This file
```

---

## 🗄️ Database Models

### Category

| Field  | Type      | Description                  |
| ------ | --------- | ---------------------------- |
| `id`   | Integer   | Primary key (auto)           |
| `name` | CharField | Category name (max 50 chars) |

### Dhikr

| Field      | Type       | Description            |
| ---------- | ---------- | ---------------------- |
| `id`       | Integer    | Primary key (auto)     |
| `text`     | TextField  | The Dhikr text content |
| `category` | ForeignKey | Related category       |

---

## 🔗 API Endpoints

| Method     | Endpoint          | Description         |
| ---------- | ----------------- | ------------------- |
| `GET`      | `/`               | List all Dhikr      |
| `GET`      | `/?q=<query>`     | Search Dhikr        |
| `GET`      | `/categories/`    | List all categories |
| `GET`      | `/category/<id>/` | Dhikr by category   |
| `GET`      | `/dhikr/<id>/`    | Dhikr detail view   |
| `GET/POST` | `/add/`           | Add new Dhikr       |
| `GET/POST` | `/edit/<id>/`     | Edit Dhikr          |
| `POST`     | `/delete/<id>/`   | Delete Dhikr        |

---

## 🌐 Deployment

### Heroku Deployment

The project includes a `Procfile` for easy Heroku deployment:

```bash
# Login to Heroku
heroku login

# Create a new app
heroku create your-app-name

# Deploy
git push heroku main

# Run migrations
heroku run python manage.py migrate
```

### Production Checklist

Before deploying to production, ensure you:

- [ ] Set `DEBUG = False` in settings
- [ ] Generate a new `SECRET_KEY`
- [ ] Configure `ALLOWED_HOSTS` properly
- [ ] Set up a production database (PostgreSQL recommended)
- [ ] Configure static files with WhiteNoise
- [ ] Enable HTTPS

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Inspired by the beautiful tradition of Islamic Dhikr
- Built with ❤️ using Django

---

<div align="center">

**May this application be a source of barakah (blessing) for all who use it** 🤲

⭐ Star this repository if you found it helpful!

</div>
