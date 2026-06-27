# QR Generator

CLI en Python para generar códigos QR estáticos con logo opcional en el centro. Útil para enlaces web, tarjetas o material impreso con branding.

## Requisitos

- Python 3.9 o superior
- `pip`

## Configuración del entorno

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

## Uso

Con el entorno activado:

### Modo interactivo

```bash
python qrgenerator.py
```

El script pedirá la URL y, opcionalmente, la ruta del logo.

### Modo CLI

```bash
# Solo URL
python qrgenerator.py "https://ejemplo.com"

# URL + logo
python qrgenerator.py "https://ejemplo.com" consultorioscanelones.jpeg
```

### Desde Python

```python
from qrgenerator import generate_qr_pro

generate_qr_pro("https://ejemplo.com")
generate_qr_pro("https://ejemplo.com", filename="mi_qr.png", logo_path="logo.png")
```

## Salida

- Por defecto guarda `qrcode_pro.png` en el directorio actual.
- Los archivos `.png` generados están en `.gitignore` y no se versionan.

## Logo central

- El logo se redimensiona automáticamente (~25% del ancho del QR).
- Se coloca centrado sobre el código.
- Se usa corrección de errores alta (`ERROR_CORRECT_H`, ~30%) para que el QR siga siendo escaneable con logo.
- Formatos soportados: PNG, JPEG, etc. (vía Pillow). PNG con transparencia (`RGBA`) respeta el canal alpha.

Si la ruta del logo no existe, se genera un QR estándar y se muestra un aviso `[WARN]`.

## Estructura del proyecto

```
qrgenerator/
├── qrgenerator.py          # Script principal
├── requirements.txt        # Dependencias
├── consultorioscanelones.jpeg  # Logo de ejemplo
├── AGENTS.md                 # Contexto para agentes de IA
└── .cursor/rules/            # Reglas de Cursor
```

## Mensajes de consola

| Prefijo | Significado |
|---------|-------------|
| `[INFO]` | Información (p. ej. logo integrado) |
| `[WARN]` | Advertencia (p. ej. logo no encontrado) |
| `[SUCCESS]` | QR generado correctamente |
| `[ERROR]` | Fallo en la generación |

## Licencia

Consultar el repositorio en GitHub: [thesadic/qrgenerator](https://github.com/thesadic/qrgenerator).
