# Spy Cat Agency

This project is a simple full-stack web application that allows the Spy Cat Agency (SCA) to manage their agents and missions. It consists of a **Django REST API** (backend) and a **Next.js frontend**.

---

## 📁 Repositories

* **Backend (Django):** Located in the `/backend` folder
* **Frontend (Next.js):** Located in the `/frontend` folder

---

## 🚀 Getting Started

### Backend (Django)

#### Requirements:

* Python 3.12
* pip
* virtualenv (optional but recommended)

#### Installation:

```bash
cd backend
python -m venv env
source env/bin/activate  # or .\env\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

#### Available Endpoints:

**Cat Endpoints**

```
GET     /api/cats/                         # List all spy cats
POST    /api/cat/create/                   # Create a new cat
GET     /api/cat/<id>/                     # Retrieve details of a cat
PUT     /api/cat/<id>/update/              # Update a cat (e.g., salary)
DELETE  /api/cat/<id>/delete/              # Delete a cat
```

**Mission Endpoints**

```
GET     /api/missions/                     # List all missions
POST    /api/mission/create/               # Create a mission with targets
GET     /api/mission/<id>/detail/          # Retrieve mission with targets
PUT     /api/mission/<id>/update/          # Update mission (e.g., mark complete)
DELETE  /api/mission/<id>/delete/          # Delete mission if no cat assigned
POST    /api/mission/<id>/assign-cat/      # Assign a cat to a mission
```

**Target Endpoints**

```
PUT     /api/target/<id>/update/           # Update target notes/completion
```

---

### Frontend (Next.js)

#### Requirements:

* Node.js (v18+ recommended)
* npm

#### Installation:

```bash
cd frontend
npm install
npm run dev
```

#### Features:

* 📋 List of spy cats
* ➕ Form to add a new cat
* 💰 Edit salary
* 🗑️ Delete cat
* UI built using TailwindCSS
* Graceful error handling

---

## 📫 Postman Collection

All API endpoints are documented and available in this Postman collection:
👉 [Postman Collection Link](https://.postman.co/workspace/My-Workspace~1000c327-0c8b-4eb7-8cd5-e546a80b2a03/collection/36472400-564a3b50-1613-466b-8f1e-5f5d6b689dc5?action=share&creator=36472400)

