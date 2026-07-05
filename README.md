# 🎉 QR Code Prank Wallpaper

A hilarious prank project that generates a QR code wallpaper. When someone scans it, they get pranked with funny jokes displayed on their screen!

## 🎭 How It Works

1. Generate a QR code that encodes a URL
2. Create a wallpaper image with the QR code
3. Set it as your desktop/mobile wallpaper
4. When someone scans the QR code, they see a fun joke prank page
5. They get annoyed (or amused) with random jokes! 😂

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/naresh2009879-dot/QR-code-prank.git
cd QR-code-prank
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Generate QR codes and wallpapers:
```bash
python generate_qr.py
```

This will create:
- `qr_code.png` - The QR code image
- `wallpaper_desktop_1080p.png` - 1920x1080 wallpaper
- `wallpaper_desktop_1440p.png` - 2560x1440 wallpaper
- `wallpaper_mobile_portrait.png` - 1080x1920 wallpaper
- `wallpaper_mobile_landscape.png` - 1920x1080 wallpaper

## 📱 Setting Up the Wallpaper

### Windows
1. Right-click on a wallpaper image
2. Select "Set as desktop background"
3. Choose "Fill" or "Fit" option

### macOS
1. System Preferences → Desktop & Screen Saver
2. Click the "+" button to add the wallpaper
3. Select and apply

### Linux
Right-click desktop → Set as Wallpaper

### Mobile (iPhone)
1. Open Photos app
2. Select the wallpaper image
3. Tap Share → Use as Wallpaper
4. Choose Lock Screen or Home Screen

### Mobile (Android)
1. Long-press on home screen
2. Select "Wallpapers"
3. Choose the image and apply

## 🃏 How the Prank Works

When someone scans the QR code:
1. It opens the `index.html` prank page
2. They see a fun message: "YOU GOT PRANKED!"
3. A random joke setup is displayed
4. They click to reveal the punchline (if they dare 😆)
5. Confetti animation plays!
6. They can get more jokes by clicking the button

## 🎯 Customization

### Change the URL in QR Code

Edit `generate_qr.py` and modify the `url` variable:

```python
url = 'https://your-custom-url.com/index.html'
```

### Add More Jokes

Edit `index.html` and add more jokes to the `jokes` array:

```javascript
{
    setup: "Your joke setup?",
    punchline: "Your punchline! 😂"
}
```

### Deploy to GitHub Pages

1. Go to your repository settings
2. Enable GitHub Pages
3. Select the `main` branch as source
4. The prank page will be available at: `https://naresh2009879-dot.github.io/QR-code-prank/`

## 📸 Wallpaper Resolutions

- **Desktop 1080p**: 1920x1080 (Most common)
- **Desktop 1440p**: 2560x1440 (Higher quality)
- **Mobile Portrait**: 1080x1920 (Vertical phones)
- **Mobile Landscape**: 1920x1080 (Horizontal phones)

## ⚙️ How to Generate Custom Wallpapers

```python
from PIL import Image
import qrcode

# Generate QR code
qr = qrcode.QRCode(version=1, box_size=15, border=4)
qr.add_data('your-url-here')
qr.make()
img = qr.make_image()

# Create wallpaper with custom size
wallpaper = Image.new('RGB', (1920, 1080), color='white')
# ... position and paste QR code
wallpaper.save('custom_wallpaper.png')
```

## 🎪 Examples of Wallpapers

The generated wallpapers have:
- Clean white background
- Centered QR code
- Proper sizing for easy scanning
- Suitable for desktop and mobile use

## 🔒 Safety & Responsible Use

This is a harmless prank! The prank page:
- ✅ Contains only jokes and fun content
- ✅ No malware or harmful code
- ✅ No tracking or data collection
- ✅ No redirects to malicious sites
- ✅ Works offline in the browser

## 🎨 Features

- 🎯 Beautiful UI with gradient backgrounds
- 🎉 Confetti animation on punchline reveal
- 📱 Fully responsive design
- 🎲 Random joke selection
- 🎬 Smooth animations and transitions
- 💾 No external dependencies in the prank page

## 📝 License

This project is open source and free to use for pranks and fun!

## 🤝 Contributing

Want to add more jokes or features?
1. Fork this repository
2. Create a feature branch
3. Add your changes
4. Submit a pull request

## 🎉 Have Fun!

Remember:
- Use this responsibly (it's just jokes!)
- Share with friends who have a good sense of humor
- Add more funny jokes to make it even better
- Take a screenshot of their reaction! 📸

---

**Made with ❤️ for pranks and laughs** 😂
