# FAQ Management System

A robust Django-based FAQ management system with real-time translation capabilities, WYSIWYG editing, and Redis caching.

Features
Multi-language support with automatic translation
Rich text editing with CKEditor
Redis-powered caching for optimal performance
RESTful API with language selection
User-friendly admin interface

# Quick Start
Prerequisites

```bash
Python 3.8+
Redis
Django 4.0+
```

# Installation

 1. Clone the repository:
 ```bash
git clone https://github.com/Goving98/BharatFD_backend.git
cd faq-system
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```


# Running the System

1. Start Redis server(In WSL or Ubuntu Terminal):
```bash
redis-server
```

2. Run Django server:
```bash
python manage.py runserver
```

Access the system:


Main interface: http://127.0.0.1:8000


Admin panel: http://127.0.0.1:8000/admin


API endpoints: Get FAQs in specific language



http://127.0.0.1:8000/?lang=hi  # Hindi


http://127.0.0.1:8000/?lang=bn  # Bengali


http://127.0.0.1:8000/?lang=es  # Spanish




# Admin Interface
The system includes a custom admin interface for managing FAQs:

Access admin panel at /admin
Navigate to FAQs section
Use the WYSIWYG editor for formatting answers
Translations are automatically generated on save

# Architecture Overview

Models: FAQ model with dynamic translation fields
Caching: Redis-based caching for translated content
API: Django REST Framework with language parameter support
Frontend: Bootstrap-based responsive interface
Editor: CKEditor integration for rich text editing

