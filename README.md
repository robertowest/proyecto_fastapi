# 🚀 FastAPI Project Template

Plantilla lista para producción usando **FastAPI**, **SQLAlchemy Async**, **Alembic**, **JWT Auth** y buenas prácticas de estructura de proyecto.

---

## Qué incluye
- FastAPI modular con versionamiento (/api/v1/).
- SQLAlchemy async + pool de conexiones.
- CRUD básico con hashing seguro.
- JWT Auth listo para implementar en services/auth.py.
- Configuración limpia con Pydantic y .env.
- Alembic para migraciones.

---

## 📁 Estructura del proyecto
```text
app/
│   ├── __init__.py
│   ├── main.py           # Punto de entrada FastAPI
│   ├── api/              # Rutas y endpoints organizados por versión o módulo
│   │   ├── __init__.py
│   │   ├── v1/           
│   │   │   ├── __init__.py
│   │   │   ├── routes_user.py
│   │   │   ├── routes_items.py
│   ├── core/             # Configuración central (settings, seguridad, middlewares)
│   │   ├── __init__.py
│   │   ├── config.py     # Configuración (pydantic BaseSettings)
│   │   ├── security.py   # JWT, OAuth, hashing
│   ├── db/               # Conexión y modelos de base de datos
│   │   ├── __init__.py
│   │   ├── base.py       # Declarative base
│   │   ├── models/       
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── item.py
│   │   ├── session.py    # Engine, SessionLocal
│   │   ├── crud.py       # Operaciones de BD
│   ├── schemas/          # Pydantic models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── item.py
│   ├── services/         # Lógica de negocio compleja
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── user.py
│   ├── dependencies/     # Dependencias reutilizables
│   │   ├── __init__.py
│   │   ├── db.py
│   │   ├── auth.py
│   ├── utils/            # Utilidades auxiliares
│   │   ├── __init__.py
│   │   ├── email.py
│   │   ├── hash.py
├── alembic/              # Si usas migraciones con Alembic
├── tests/                # Tests unitarios y de integración
│   ├── __init__.py
│   ├── test_users.py
│   ├── test_items.py
├── requirements.txt      # Dependencias
├── .env                  # Variables de entorno
├── .gitignore
```

### Separación de capas
- api/: organiza tus rutas (APIRouter) por versión o dominio funcional.
- core/: código común.
- db/: define tus modelos SQLAlchemy, sesión y operaciones CRUD.
- dependencies/: dependencias reutilizables con Depends.
- schemas/: define Pydantic models para validar entrada/salida (Request/Response).
- services/: lógica de negocio (envío de correos, pagos, procesamientos).
- utils/: funciones útiles.
- tests/: pruebas unitarias.
- main.py: punto de entrada de tu aplicación.

### Tips extras
- Usa APIRouter para modularidad.
- Define tus dependencias reutilizables, por ejemplo: obtener usuario autenticado.
- Mantén la lógica de negocio fuera de las rutas → colócala en services/.
- Versiona tu API desde el principio (/api/v1/).
- Documenta bien con docstrings y summary/description en tus endpoints.

---

## ⚙️ **Requisitos previos**

- Python 3.11+
- PostgreSQL o tu base de datos preferida
- Virtualenv o poetry

---

## ✅ **Instalación**

1. **Clonar el repositorio**

```bash
git clone <tu-repo-url> fastapi_app
cd fastapi_app
```

2. **Crear entorno virtual**

```bash
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

4. **Configurar .env**

Edita el archivo .env:

```bash
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/dbname
SECRET_KEY=un_secret_key_seguro
```

## 🗃️ Migraciones con Alembic
1. **Inicializar Alembic**
```bash
alembic init alembic
```
Configura `alembic/env.py` para usar `app.db.base.Base` y tu **DATABASE_URL**.

2. **Crear una migración**
```bash
alembic revision --autogenerate -m "Initial migration"
```

3. **Aplicar migraciones**
```bash
alembic upgrade head
```

## 🚀 Correr la API
```bash
uvicorn app.main:app --reload
```

- Documentación interactiva: http://127.0.0.1:8000/docs
- Documentación ReDoc: http://127.0.0.1:8000/redoc


## 🔐 Autenticación JWT
- Manejo de tokens JWT en `core/security.py`.
- Hash de contraseñas con passlib en `utils/hash.py`.

## 🧪 Pruebas
Agrega tus tests en la carpeta `/tests` (opcional).

Usa **pytest** para ejecutarlos.

## ❤️ Créditos
Esta plantilla fue generada con buenas prácticas recomendadas para FastAPI, Pydantic, SQLAlchemy y Alembic.

## ✨ Extensiones sugeridas
- 🚦 Validar linting con flake8 o ruff
- 🧪 Cobertura de tests con pytest-cov
- 🐳 Dockerizar para despliegues
- 🔐 Añadir OAuth2/JWT completo
