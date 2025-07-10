# Estructura de un proyecto de FastAPI
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

# Separación de capas
api/: organiza tus rutas (APIRouter) por versión o dominio funcional.
core/: código común.
db/: define tus modelos SQLAlchemy, sesión y operaciones CRUD.
dependencies/: dependencias reutilizables con Depends.
schemas/: define Pydantic models para validar entrada/salida (Request/Response).
services/: lógica de negocio (envío de correos, pagos, procesamientos).
utils/: funciones útiles.
tests/: pruebas unitarias.
main.py: punto de entrada de tu aplicación.

# Tips extras
✔️ Usa APIRouter para modularidad.
✔️ Define tus dependencias reutilizables, por ejemplo: obtener usuario autenticado.
✔️ Mantén la lógica de negocio fuera de las rutas → colócala en services/.
✔️ Versiona tu API desde el principio (/api/v1/).
✔️ Documenta bien con docstrings y summary/description en tus endpoints.

