# 🏋️ Zeus Gym - Sistema de Gestión de Gimnasio

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
- PostgresSql 

**Infraestructura**
- Railway (deploy)  
- Whitenoise (static files)  
- Gunicorn (WSGI server)  
- Celery + Redis (tareas asíncronas)  

---

## 📸 Sistema en uso


---

## ⚙️ Instalación y uso local

Requisitos previos
 
- Python 3.10+
- Node.js 18+
- PostgreSql
- Git

🔹 Backend (Django)
# Clonar el repositorio
git clone https://github.com/tuusuario/zeus-gym.git
cd zeus-gym/backend

# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows

# Instalar dependencias
pip install -r requirements.txt

# Migrar base de datos
python manage.py makemigrations
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver


🔹 Frontend (React)

cd ../frontend

# Instalar dependencias
npm install

# Ejecutar proyecto
npm start

git clone https://github.com/tuusuario/zeus-gym.git
cd zeus-gym
