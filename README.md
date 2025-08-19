# 🏋️ Zeus Gym - Sistema de Gestión de Gimnasio

![React](https://img.shields.io/badge/Frontend-React-61DAFB?logo=react&logoColor=white)  ![Django](https://img.shields.io/badge/Backend-Django-092E20?logo=django&logoColor=white)  ![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-4169E1?logo=postgresql&logoColor=white)  ![Railway](https://img.shields.io/badge/Deploy-Railway-0B0D0E?logo=railway&logoColor=white)  ![License: MIT](https://img.shields.io/badge/License-MIT-green)  

Aplicación web fullstack para la administración integral de un gimnasio.  
Su objetivo es brindar una solución integral para la administración de gimnasios, permitiendo la gestión tanto del lado administrativo como del socio.
---

## 🚀 Demo

🔗 [Ver aplicación en producción](https://zeus-gym-production.up.railway.app)  

---

## ✨ Características principales

👨‍💼 **Administración**

- Gestión de socios (alta, baja, modificación).
- Control de ingresos diarios al gimnasio.
- Administración de clases (días, horarios, instructores).
- Gestión de caja y registro de pagos.
- Administración de membresías (tipos, precios, duración).
- Gestión de usuarios del sistema con diferentes roles:
- Administrador: acceso completo.
- Recepcionista: acceso limitado a la atención diaria.

🏋️ **Socios**

- Acceso al portal web del gimnasio.
- Inscripción en clases disponibles.
- Visualización de sus membresías y vencimientos.

## 🛠️ Tecnologías utilizadas

**Frontend**
- React  
- Bootstrap  
- React Router  

**Backend**
- Django REST Framework  
- PostgreSQL

**Infraestructura**
- Railway (deploy)  
- Whitenoise (static files)  
- Gunicorn (WSGI server)  
- Celery + Redis (tareas asíncronas)  

---

## 📸 Capturas de pantalla
<img width="800" height="600" alt="Captura de pantalla 2025-07-24 190825" src="https://github.com/user-attachments/assets/cb856019-a2e9-4f55-b32b-080caf48c6ce" />

<img width="800" height="600" alt="Captura de pantalla 2025-07-25 001422" src="https://github.com/user-attachments/assets/89ca702f-c7b2-4df7-bea1-105d1f2a463d" />

---

## ⚙️ Instalación y uso local

Requisitos previos
 
- Python 3.10+
- Node.js 18+
- PostgreSql
- Git

🔹 Backend (Django)
- Clonar el repositorio
git clone https://github.com/tuusuario/zeus-gym.git
cd zeus-gym/backend

- Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows

//Instalar dependencias:
pip install -r requirements.txt

- Migrar base de datos:
python manage.py makemigrations
python manage.py migrate

- Crear superusuario
python manage.py createsuperuser

- Ejecutar servidor
python manage.py runserver


🔹 Frontend (React)

cd ../gym-frontend

- Instalar dependencias
npm install

- Ejecutar proyecto
npm start

git clone https://github.com/tuusuario/zeus-gym.git
cd zeus-gym
