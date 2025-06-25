# Burnoff Manager

Burnoff Manager es una aplicación web diseñada para gestionar y monitorear membresias del Box de Crossfit BurnoffBox, facilitando la administración tanto para usuarios como para administradores. Este proyecto está pensado para ser utilizado en entornos reales

## Tecnologías utilizadas

### Backend
- Python 3
- Flask
- Flask SQLAlchemy
- Flask-Migrate (Alembic)
- Flask-JWT-Extended (autenticación JWT)
- Base de datos relacional (configurable)

### Frontend
- React 18
- Vite
- Context API para autenticación
- Axios para consumo de API

### Otros
- Docker 

## Estructura del proyecto

```
burnoff-manager/
├── burnoff-manager-backend/   # API REST con Flask
├── burnoff-manager-frontend/  # Aplicación web en React
├── docker-compose.yml         # Orquestación de servicios
```

## Funcionamiento

- Los usuarios pueden autenticarse y acceder a funcionalidades según su rol. 
- Los administradores pueden gestionar membresias, usuarios y citas.
- El frontend consume la API del backend para mostrar y manipular datos en tiempo real.

## Configuración

Cada parte (backend y frontend) requiere su propio archivo `.env` con las variables de entorno necesarias. Ejemplo de variables:

### Backend (`burnoff-manager-backend/.env`)
```
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/basededatos
SECRET_KEY=tu_clave_secreta
ALGORITHM=HS256
```

### Frontend (`burnoff-manager-frontend/.env`)
```
VITE_API_URL=http://localhost:8000
```

**No subas los archivos `.env` al repositorio.**

## Instalación y uso rápido

1. Clona el repositorio:
   ```sh
   git clone https://github.com/tuusuario/burnoff-manager.git
   cd burnoff-manager
   ```
2. Configura los archivos `.env` en backend y frontend.
3. Levanta los servicios con Docker Compose:
   ```sh
   docker-compose up --build
   ```
4. Accede a la app en `http://localhost:5173` (frontend) y la API en `http://localhost:8000/docs` (backend).

## Estado actual

- [x] Autenticación de usuarios
- [x] Interfaz de login
- [ ] Panel de administración avanzado
- [ ] Reportes y estadísticas

## Autor

Juan Sebastián

---
¡Este proyecto está en desarrollo y abierto a sugerencias y contribuciones!
