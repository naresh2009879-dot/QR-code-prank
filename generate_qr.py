#!/usr/bin/env python3
"""QR Code Generator for Prank Wallpaper"""

import qrcode
from PIL import Image

def generate_qr_code(url, output_filename='qr_code.png', size=10):
    """Generate a QR code image from a URL"""
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=size, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_filename)
    print(f"✅ QR code: {output_filename} ({img.size[0]}x{img.size[1]}px)")
    return img

def create_wallpaper(qr_image, wallpaper_width=1920, wallpaper_height=1080, output_filename='wallpaper.png'):
    """Create a wallpaper with the QR code"""
    wallpaper = Image.new('RGB', (wallpaper_width, wallpaper_height), color='white')
    qr_size = 400
    qr_resized = qr_image.resize((qr_size, qr_size), Image.Resampling.LANCZOS)
    x = (wallpaper_width - qr_size) // 2
    y = (wallpaper_height - qr_size) // 2
    wallpaper.paste(qr_resized, (x, y))
    wallpaper.save(output_filename)
    print(f"✅ Wallpaper: {output_filename} ({wallpaper_width}x{wallpaper_height}px)")
    return wallpaper

def main():
    url = 'https://naresh2009879-dot.github.io/QR-code-prank/'
    print("🎉 QR Code Prank Wallpaper Generator")
    print("=" * 50)
    
    qr_img = generate_qr_code(url, output_filename='qr_code.png', size=15)
    
    resolutions = {
        'desktop_1080p': (1920, 1080),
        'desktop_1440p': (2560, 1440),
        'mobile_portrait': (1080, 1920),
        'mobile_landscape': (1920, 1080),
    }
    
    print("\n📱 Creating wallpapers...")
    for name, (width, height) in resolutions.items():
        output_file = f'wallpaper_{name}.png'
        create_wallpaper(qr_img, width, height, output_file)
    
    print("\n" + "=" * 50)
    print("✨ All files generated!")
    print(f"\n📍 URL in QR: {url}")
    print("\n💡 Set a wallpaper and share the prank! 😂")

if __name__ == "__main__":
    main()