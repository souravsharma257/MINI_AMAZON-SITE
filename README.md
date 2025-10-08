MINI_AMAZON-SITE
 
Project Overview
MINI_AMAZON-SITE is a simple Django-based e-commerce website. It mimics the feel of Amazon – browse products, filter by categories (Electronics, Fashion, Books, Home), search, add to cart/wishlist, and view orders. Includes user login/register. Perfect for Django beginners.
Features

User Authentication: Login, Register, Logout (using Django built-in auth)
Products: Add/Edit via Admin (categories: Home, Fashion, Books, Electronics)
Home Page: Product grid, search bar, sidebar filters
Detail View: Image, description, price, Add to Cart
Cart & Wishlist: Add/remove items
Orders: History for logged-in users
UI: Simple responsive design (CSS/JS)

Tech Stack

Backend: Django 4.x (Python 3.8+)
Database: SQLite (db.sqlite3)
Frontend: HTML (18%), CSS (10%), JS (0.6%)
Other: Pillow for images (in requirements.txt)

Setup Instructions

Clone the Repo:
textgit clone https://github.com/souravsharma27/MINI_AMAZON-SITE.git
cd MINI_AMAZON-SITE

Virtual Environment (Recommended):
textpython -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

Install Dependencies:
textpip install -r requirements.txt
(If missing: pip install django pillow)
Database Setup:
textpython manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # Create admin user

Static/Media Files:
textpython manage.py collectstatic

Images: Upload via admin to media/images/ folder.


Run Server:
textpython manage.py runserver

Open: http://127.0.0.1:8000/



Admin Panel

URL: http://127.0.0.1:8000/admin/
Add products: Shop > Products (upload images to media/images/).

File Structure
textMINI_AMAZON-SITE/
├── db.sqlite3          # Database
├── manage.py           # Django manager
├── requirements.txt    # Dependencies
├── images/             # Static images
│   └── media/          # Subfolder for media
├── mini_amazon/        # Main project folder (settings, urls)
├── shop/               # App (models, views, urls)
├── static/             # CSS/JS files
└── README.md           # This file
Usage

Home: Browse products, View/Add to Wishlist/Cart.
Login: Unlock personal features.
Admin: Manage products.

Screenshots
<img src="images/home.png" alt="Home Page">  
Contributing

Fork the repo.
Create branch: git checkout -b feature/add-something.
Commit: git commit -m "Add feature".
Push & PR: On GitHub.

Issues
Found a bug? Open an Issue.
License
MIT License – Free to use/modify.
Built by souravsharma27 🚀 Questions? Comment below!
