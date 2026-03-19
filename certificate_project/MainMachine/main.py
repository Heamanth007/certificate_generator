from PIL import Image, ImageDraw, ImageFont
import os
import qrcode
import uuid

'''names=[
    "Heamanthraj.S",
    "Natarajan.V",
    "Sabarinathan.V",
    "Girinath.K",
    "Navinkumar.M",
    "Kumaravel.T",
    "Sudharsan.S", 
    "Aravinth Kumar.P"
]'''

def generate(names):
    os.makedirs("Generated", exist_ok=True)

    for index, name in enumerate(names, start=1):
        certificate_template=Image.open('template.png')
        draw = ImageDraw.Draw(certificate_template)
        font = ImageFont.truetype('DS-Regular.ttf', 75)
        cert_id = str(uuid.uuid4())[:8]
        qr_data=f"Name:{name} | ID:{cert_id}"
        qr = qrcode.make(qr_data)
        qr = qr.resize((150, 150))
        text_position = (268,622)
        draw.text(text_position, name, fill='black', font=font)
        certificate_template.paste(qr, (1622, 1080))
        safe_filename = f"{name}.png"

        output_path = os.path.join("Generated", safe_filename)

        certificate_template.save(output_path)

        print(f"Certificate Generated for {name}")  
      
                              