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


