# 🏋️ Zeus Gym - Sistema de Gestión de Gimnasio

![React](https://img.shields.io/badge/Frontend-React-61DAFB?logo=react&logoColor=white)    ![Django](https://img.shields.io/badge/Backend-Django-092E20?logo=django&logoColor=white)    ![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-4169E1?logo=postgresql&logoColor=white)    ![Railway](https://img.shields.io/badge/Deploy-Railway-0B0D0E?logo=railway&logoColor=white)    ![License: MIT](https://img.shields.io/badge/License-MIT-green)  

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
<img width="600" height="400" alt="Captura de pantalla 2025-07-24 190825" src="https://github.com/user-attachments/assets/cb856019-a2e9-4f55-b32b-080caf48c6ce" />

<img width="600" height="400" alt="Captura de pantalla 2025-07-25 001422" src="https://github.com/user-attachments/assets/89ca702f-c7b2-4df7-bea1-105d1f2a463d" />

---

## ⚙️ Instalación y uso local

Requisitos previos
 
- Python 3.10+
- Node.js 18+
- PostgreSQL
- Git

### Backend (Django)

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/GuadalupePorra/zeus-gym.git
   cd zeus-gym/backend
2. Crear y activar entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # En Linux/Mac
   venv\Scripts\activate      # En Windows
3. Instalar dependencias:
    ```bash
    pip install -r requirements.txt

4. Migrar base de datos:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
5. Crear superusuario:
   ```bash
   python manage.py createsuperuser
6. Ejecutar servidor:
   ```bash
   python manage.py runserver
## Frontend (React)
1. Navegar al directorio del frontend:
   ```bash
   cd ../gym-frontend
2. Instalar dependencias:
   ```bash
   npm install
3. Ejecutar proyecto:
   ```bash
   npm start

## 🤝 Contribución

1. Haz un fork del proyecto
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`)
3. Realiza tus cambios y haz commit (`git commit -m 'Agrega nueva funcionalidad'`)
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

