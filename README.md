# 🏋️‍♂️ Burnoff Manager

**Burnoff Manager** es una aplicación web  diseñada para el control administrativo de **Burnoff Box**. El sistema permite al administrador gestionar membresías,usuarios, citas  y enviar notificaciones automáticas a los usuarios mediante **WhatsApp**, sin que estos deban ingresar a la plataforma.

> ⚠️ Este proyecto se encuentra en desarrollo activo. Todas las funcionalidades descritas a continuación están siendo construidas progresivamente.

## 🎯 Propósito del proyecto

Burnoff Manager busca automatizar la gestión operativa del box, centralizando tareas clave en una única interfaz para el administrador:

- 🕒 Seguimiento de membresías y vencimientos  
- 🔁 Renovaciones de planes  
- 📥 Agendamiento de citas solicitadas por los usuarios  
- 📊 Organización de información operativa diaria

## 🧱 Tecnologías utilizadas

### Backend
- 🐍 Python 3  
- 🔥 Flask (incluye autenticación JWT y ORM)  
- 🗄️ PostgreSQL
  
### Frontend
- ⚛️ React 18  
- ⚡ Vite  
- 🧠 Context API  
- 🔗 Axios  
- 🧭 React Router  
- 🎨Tailwind CSS

**Infraestructura**  
- 🐳 Docker & Docker Compose  
- ⚙️ Archivos `.env` para configuración de entorno


**Integración WhatsApp (planificada)**  
- 💬 WhatsApp Business API o Twilio WhatsApp API  
- 🤖 Bots para interacción automática con el cliente  
- 📅 Manejo de horarios y disponibilidad de citas  
- 🔁 Comunicación entre backend y usuarios por WhatsApp

 **Sincronización de calendarios (futuro)**  
- 📆 Google Calendar API o Microsoft Outlook Calendar API
- 🔒 OAuth 2.0 para autorización segura 
- 📤 Envío de eventos desde el sistema al calendario del administrador/fisioterapeuta



## ⚙️ Para desarrolladores

Esta sección detalla la estructura técnica del proyecto, el flujo de integración entre backend y frontend, así como los pasos para instalarlo y levantarlo en entorno local.

## 📁 Estructura del proyecto
```
burnoff-manager/
├── burnoff-manager-backend/   # API REST con Flask
├── burnoff-manager-frontend/  # Aplicación web en React
├── docker-compose.yml         # Orquestación de servicios
```

### 🔗 Integración entre backend y frontend

- El backend expone una API RESTful desarrollada en Flask y protegida con autenticación JWT.  
- El frontend en React consume dicha API utilizando Axios y gestiona el estado global con Context API.  
- Ambos servicios están conectados mediante variables de entorno y se ejecutan con Docker Compose para facilitar el desarrollo local.

### 💻 Instalación y ejecución

1. Clona el repositorio:
   ```sh
   git clone https://github.com/tuusuario/burnoff-manager.git
   cd burnoff-manager
   ```
2. Crea los archivos `.env` en las carpetas `burnoff-manager-backend` y `burnoff-manager-frontend` según los ejemplos y variables necesarias para tu entorno.
3. Construye y levanta los servicios con Docker Compose:
   ```sh
   docker-compose up --build
   ```
4. Accede a la aplicación web en `http://localhost:5173` (frontend) y a la documentación de la API en `http://localhost:8000/docs` (si tienes Swagger habilitado) o en el puerto configurado para el backend.

> Si prefieres ejecutar los servicios por separado:
>
> - Backend:
>   ```sh
>   cd burnoff-manager-backend
>   # Recomendado: usa entorno virtual con pipenv
>   pipenv shell
>   pipenv install
>   # O si prefieres requirements.txt:
>   # pip install -r requirements.txt
>   flask db migrate -m "Mensaje de migración"  # Genera migraciones (solo si hay cambios en modelos)
>   flask db upgrade  # Aplica migraciones
>   flask run
>   ```
> - Frontend:
>   ```sh
>   cd burnoff-manager-frontend
>   npm install
>   npm run dev
>   ```

---

## 👨‍💻 Autor

**Juan Sebastián Orejuela**  
Multimedia Engineer and Full Developer – 🇨🇴 Colombia  

[🔗 LinkedIn](https://www.linkedin.com/in/juan-sebastian-orejuela-fullstack-developer/)  
[🐙 GitHub](https://github.com/JuanSeDelgado)

> 💡 *Este proyecto está en desarrollo activo. Sugerencias, ideas y contribuciones son bienvenidas.*


