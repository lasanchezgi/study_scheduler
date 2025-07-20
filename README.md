# 📚⏰ | Study Scheduler

![Python](https://img.shields.io/badge/python-v3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**Study Scheduler** es una herramienta diseñada para eliminar la fricción al momento de estudiar. Abre automáticamente las plataformas educativas en tu navegador según rangos de tiempo específicos que configures.

## 🎯 Motivación

¿Cuántas veces has pospuesto estudiar porque simplemente abrir la plataforma educativa se siente como una barrera? Study Scheduler elimina esa fricción abriendo automáticamente tus plataformas de estudio favoritas en los horarios que designes.

## ✨ Características

- 🕐 **Apertura automática por horarios**: Define rangos de tiempo específicos para cada plataforma
- 🌐 **Múltiples plataformas**: Soporta cualquier plataforma educativa online
- ⚡ **Configuración simple**: Archivo JSON fácil de modificar
- 🔄 **Prevención de duplicados**: Evita abrir la misma plataforma múltiples veces en el día
- 🎛️ **Modo forzado**: Opción para abrir todas las plataformas independientemente del horario

## 🚀 Instalación

### Requisitos

- Python 3.10 o superior
- Poetry (recomendado) o pip

### Con Poetry (recomendado)

```bash
# Clona el repositorio
git clone <tu-repositorio>
cd study_scheduler

# Instala las dependencias
poetry install

# Activa el entorno virtual
poetry shell
```

### Con pip

```bash
# Clona el repositorio
git clone <tu-repositorio>
cd study_scheduler

# Crea un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instala las dependencias
pip install schedule
```

## ⚙️ Configuración

Edita el archivo `app/config/platforms_config.json` para añadir tus plataformas de estudio:

```json
[
    {
        "name": "Coursera",
        "url": "https://www.coursera.org",
        "start_time": "08:00",
        "end_time": "09:00"
    },
    {
        "name": "DataCamp",
        "url": "https://www.datacamp.com",
        "start_time": "12:00",
        "end_time": "14:00"
    },
    {
        "name": "Platzi",
        "url": "https://platzi.com",
        "start_time": "19:00",
        "end_time": "21:00"
    }
]
```

### Parámetros de configuración

- **name**: Nombre descriptivo de la plataforma
- **url**: URL completa de la plataforma educativa
- **start_time**: Hora de inicio del rango (formato HH:MM)
- **end_time**: Hora de fin del rango (formato HH:MM)

## 🎮 Uso

### Modo automático (respeta horarios)

```bash
cd app
python main.py
```

### Modo forzado (abre todas las plataformas)

```bash
cd app
python main.py --force
```

### Desde el directorio raíz

```bash
# Opción 1: Usar módulo
python -m app.main

# Opción 2: Con PYTHONPATH
export PYTHONPATH="./app:$PYTHONPATH"
python app/main.py
```

## 📁 Estructura del Proyecto

```bash
study_scheduler/
├── app/
│   ├── main.py                    # Punto de entrada principal
│   ├── config/
│   │   └── platforms_config.json  # Configuración de plataformas
│   ├── domain/
│   │   └── study_platform.py      # Modelo de dominio
│   ├── infrastructure/
│   │   ├── browser_opener.py      # Abre URLs en el navegador
│   │   └── platform_repository.py # Carga configuración
│   ├── interface/
│   │   └── cli_runner.py          # Interfaz de línea de comandos
│   └── use_cases/
│       └── open_platforms_in_time_range.py  # Lógica principal
├── pyproject.toml                 # Configuración de Poetry
└── README.md                      # Este archivo
```

## 🏗️ Arquitectura

El proyecto sigue los principios de **Clean Architecture**:

- **Domain**: Entidades y reglas de negocio (`StudyPlatform`)
- **Use Cases**: Lógica de aplicación (`OpenPlatformsInTimeRange`)
- **Infrastructure**: Adaptadores externos (`BrowserOpener`, `PlatformRepository`)
- **Interface**: Puntos de entrada (`cli_runner`)

## 💡 Ejemplos de Uso

### Rutina de estudio matutina

```json
{
    "name": "Duolingo",
    "url": "https://www.duolingo.com",
    "start_time": "07:00",
    "end_time": "07:30"
}
```

### Sesión de programación vespertina

```json
{
    "name": "FreeCodeCamp",
    "url": "https://www.freecodecamp.org",
    "start_time": "20:00",
    "end_time": "22:00"
}
```

## 🔧 Desarrollo

### Ejecutar en modo debug

El sistema incluye logs debug que muestran la hora actual y las evaluaciones:

```text
[DEBUG] Hora actual: 14:30:00
[DEBUG] Evaluando Coursera entre 08:00:00 y 09:00:00
[DEBUG] Evaluando DataCamp entre 12:00:00 y 14:00:00
```

### Añadir nuevas funcionalidades

El diseño modular permite fácil extensión:

- **Nuevos tipos de notificaciones**: Extiende `BrowserOpener`
- **Diferentes fuentes de configuración**: Implementa nuevos repositories
- **Lógica de horarios compleja**: Modifica `StudyPlatform`

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Añade nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## ✨ Inspiración

> "La disciplina es elegir entre lo que quieres ahora y lo que quieres más."

Study Scheduler te ayuda a elegir lo que quieres más: **tu crecimiento personal y profesional**.

---

## 💡 Autor y agradecimientos

[Laura Sánchez Giraldo](mailto:laurasanchezgiraldo@outlook.es)  

Hecho con ❤️ para eliminar las excusas y maximizar el aprendizaje.
