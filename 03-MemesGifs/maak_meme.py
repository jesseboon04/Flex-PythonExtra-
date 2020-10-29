from PIL import Image, ImageFont, ImageDraw

# Afbeelding openen en oplsaan in de variabele met de naam: afbeelding
afbeelding = Image.open("meme_background.jpg")

# De afbeelding tonen in de standaard image viewer van jouw systeem
afbeelding.show()

# De breedte en hoogte van de afbeelding lezen en tonen 
breedte = afbeelding.width
hoogte = afbeelding.height

tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=lettertype) 

# Tekst positie berekenen
tekst_x = (breedte - tekst_breedte) / 2
tekst_y = (hoogte - tekst_hoogte) / 2

lettertype = ImageFont.truetype("impact.ttf",50)

# Vraag aan de ImageDraw module om een tekengebied te maken op de achtergrond afbeelding
tekengebied = ImageDraw.Draw(afbeelding)

# Tekst schrijven
tekst = "RAINBOW\n\n\n\n\n\n\nDOG"
tekengebied.multiline_text((tekst_x,tekst_y), tekst, font=lettertype, fill=(0,0,0))

# Het resultaat tonen
afbeelding.show()

# En opslaan onder een andere naam
afbeelding.save("meme_met_tekst.jpg")
