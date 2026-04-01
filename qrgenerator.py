import qrcode
from PIL import Image
import os
import sys

def generate_qr_pro(url, filename="qrcode_pro.png", logo_path=None):
    """
    Genera un QR estático con soporte opcional para branding central.
    """
    try:
        # Configuración del QR con corrección de errores alta (30% de recuperación)
        # Necesaria para que el logo no rompa la decodificación.
        qr = qrcode.QRCode(
            version=None, # Auto-size based on content
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        
        qr.add_data(url)
        qr.make(fit=True)

        # Generar imagen base en modo RGB para manipulación de color
        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

        if logo_path and os.path.exists(logo_path):
            logo = Image.open(logo_path)
            
            # Calcular dimensiones para que el logo ocupe aprox el 20% del QR
            qr_width, qr_height = img.size
            logo_max_size = qr_width // 4
            
            # Redimensionar logo manteniendo aspect ratio
            logo.thumbnail((logo_max_size, logo_max_size), Image.Resampling.LANCZOS)
            
            # Calcular posición central
            logo_width, logo_height = logo.size
            pos = ((qr_width - logo_width) // 2, (qr_height - logo_height) // 2)
            
            # Pegar logo (usando el mismo logo como máscara si tiene transparencia)
            mask = logo.split()[3] if logo.mode == 'RGBA' else None
            img.paste(logo, pos, mask)
            print(f"[INFO] Logo '{logo_path}' integrado correctamente.")
        else:
            if logo_path:
                print(f"[WARN] Logo '{logo_path}' no encontrado. Generando QR estándar.")

        img.save(filename)
        print(f"[SUCCESS] QR generado en: {os.path.abspath(filename)}")

    except Exception as e:
        print(f"[ERROR] Fallo en la generación: {e}")

if __name__ == "__main__":
    # Argumentos: 1: URL, 2: Logo (opcional)
    target_url = sys.argv[1] if len(sys.argv) > 1 else input("URL: ").strip()
    path_to_logo = sys.argv[2] if len(sys.argv) > 2 else None
    
    if not path_to_logo and len(sys.argv) == 1:
        # Preguntar solo si no se pasó por CLI
        opt_logo = input("¿Ruta del logo? (Dejar vacío para omitir): ").strip()
        path_to_logo = opt_logo if opt_logo else None

    if target_url:
        generate_qr_pro(target_url, logo_path=path_to_logo)
    else:
        print("Error: URL requerida.")