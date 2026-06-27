# QR Generator — Guía para el agente

## Propósito

Script CLI en Python que genera códigos QR estáticos con logo opcional en el centro. Pensado para uso local (branding de consultorios, enlaces, etc.).

## Stack

- Python 3 (entorno Conda: `qrgenerator`)
- `qrcode` — generación del código QR
- `Pillow` — composición de imagen y logo

## Ejecución

```bash
# Con entorno activo
python qrgenerator.py "https://ejemplo.com"
python qrgenerator.py "https://ejemplo.com" consultorioscanelones.jpeg
```

Dependencias: `pip install -r requirements.txt`

## Convenciones del código

- Mensajes de log en español con prefijos `[INFO]`, `[WARN]`, `[SUCCESS]`, `[ERROR]`
- Función principal: `generate_qr_pro(url, filename="qrcode_pro.png", logo_path=None)`
- Corrección de errores `ERROR_CORRECT_H` cuando hay logo (≈30% recuperación)
- Logo centrado, máximo ~25% del ancho del QR (`qr_width // 4`)
- Salida por defecto: `qrcode_pro.png` (ignorada en git)

## Qué evitar

- No cambiar la corrección de errores a un nivel bajo si se usa logo
- No commitear PNG generados ni el entorno Conda
- Mantener el script como CLI simple; no añadir frameworks web sin que se pida

## Archivos clave

| Archivo | Rol |
|---------|-----|
| `qrgenerator.py` | Lógica de generación |
| `requirements.txt` | Dependencias |
| `consultorioscanelones.jpeg` | Logo de ejemplo (asset del repo) |
