# QR Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Issues](https://img.shields.io/github/issues/thesadic/qrgenerator)](https://github.com/thesadic/qrgenerator/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![CI](https://github.com/thesadic/qrgenerator/actions/workflows/ci.yml/badge.svg)](https://github.com/thesadic/qrgenerator/actions/workflows/ci.yml)

CLI en Python para generar códigos QR estáticos con logo opcional en el centro. Útil para enlaces web, tarjetas o material impreso con branding.

> **English summary:** see [English](#english) below.

## Qué problema resuelve

Generar QR con branding (logo centrado) suele requerir herramientas online o editores gráficos. Este proyecto lo hace en local, con un comando, sin subir URLs ni logos a terceros: ideal para material impreso, tarjetas y enlaces con identidad visual.

## Requisitos

- Python 3.9 o superior
- `pip`

## Instalación

### Opción A: venv (recomendado)

Desde la raíz del proyecto:

```bash
cd qrgenerator

# Crear entorno virtual
python3 -m venv .venv

# Activar (macOS / Linux)
source .venv/bin/activate

# Activar (Windows)
# .venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### Opción B: Conda

Si usás Anaconda o Miniconda:

```bash
conda create -n qrgenerator python=3.11 -y
conda activate qrgenerator
pip install -r requirements.txt
```

## Dependencias

| Paquete | Uso |
|---------|-----|
| [qrcode](https://pypi.org/project/qrcode/) | Generación del código QR |
| [Pillow](https://pypi.org/project/Pillow/) | Composición de imagen y logo |

## Ejemplo rápido

Con el entorno activado:

```bash
# Solo URL
python qrgenerator.py "https://ejemplo.com"

# URL + logo
python qrgenerator.py "https://ejemplo.com" logo.png
```

Salida por defecto: `qrcode_pro.png` en el directorio actual.

### Modo interactivo

```bash
python qrgenerator.py
```

El script pedirá la URL y, opcionalmente, la ruta del logo.

### Desde Python

```python
from qrgenerator import generate_qr_pro

generate_qr_pro("https://ejemplo.com")
generate_qr_pro("https://ejemplo.com", filename="mi_qr.png", logo_path="logo.png")
```

## Salida

- Por defecto guarda `qrcode_pro.png` en el directorio actual.
- Los archivos de imagen generados están en `.gitignore` y no se versionan.

## Logo central

- El logo se redimensiona automáticamente (~25% del ancho del QR).
- Se coloca centrado sobre el código.
- Se usa corrección de errores alta (`ERROR_CORRECT_H`, ~30%) para que el QR siga siendo escaneable con logo.
- Formatos soportados: PNG, JPEG, etc. (vía Pillow). PNG con transparencia (`RGBA`) respeta el canal alpha.

Si la ruta del logo no existe, se genera un QR estándar y se muestra un aviso `[WARN]`.

## Estructura del proyecto

```
qrgenerator/
├── qrgenerator.py              # Script principal
├── requirements.txt            # Dependencias
├── LICENSE                     # MIT
├── CONTRIBUTING.md             # Guía de contribución
├── CODE_OF_CONDUCT.md          # Código de conducta
├── AGENTS.md                   # Contexto para agentes de IA
├── .github/                    # Plantillas de issues/PRs y CI
└── .cursor/rules/              # Reglas de Cursor
```

## Mensajes de consola

| Prefijo | Significado |
|---------|-------------|
| `[INFO]` | Información (p. ej. logo integrado) |
| `[WARN]` | Advertencia (p. ej. logo no encontrado) |
| `[SUCCESS]` | QR generado correctamente |
| `[ERROR]` | Fallo en la generación |

## Contribuir

Las contribuciones son bienvenidas. Antes de abrir un pull request, leé:

- [CONTRIBUTING.md](CONTRIBUTING.md) — flujo de trabajo, estilo de código y reglas de revisión
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) — normas de la comunidad

**Importante:** ningún cambio se fusiona en `main` sin revisión y aprobación previa del maintainer.

## Licencia

Este proyecto se distribuye bajo la licencia [MIT](LICENSE).

---

## English

CLI in Python to generate static QR codes with an optional centered logo. Useful for web links, business cards, or printed material with branding.

### Problem it solves

Branded QR codes (logo in the center) often need online tools or image editors. This project does it locally with one command—no uploading URLs or logos to third parties.

### Install

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Or with Conda:

```bash
conda create -n qrgenerator python=3.11 -y
conda activate qrgenerator
pip install -r requirements.txt
```

### Quick start

```bash
python qrgenerator.py "https://example.com"
python qrgenerator.py "https://example.com" logo.png
```

Default output: `qrcode_pro.png`. High error correction (`ERROR_CORRECT_H`) keeps the code scannable when a logo is present.

### Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Nothing is merged into `main` without prior maintainer review and approval.

### License

[MIT](LICENSE).
