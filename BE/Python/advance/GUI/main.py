# # https://www.javatpoint.com/python-tkinter

# import tkinter as tk
# import constant
# import os
# import pygame

# pygame.mixer.init()

# class MusicsGUI:
#     def __init__(self):
#         self.screen = tk.Tk()


#     def mainScreenTitle(self, title_name):
#         self.screen.title(f"{title_name}")

#     def setIcon(self, icon_path):
#         self.screen.iconbitmap(icon_path)

#     def setGeometry(self, width, height):
#         self.screen.geometry(f"{width}x{height}")

#     def submitName(self):
#         name = self.name_entry.get()
#         print(name)

#     def mainPage(self):
#         tk.Label(self.screen, text="Tops musics List").grid(row=0, column=0)
#         # tk.Label(self.screen, text="Tops musics List").pack(side="top")
#         # tk.Label(self.screen, text="Tops musics List", bg="lightblue").place(
#         #     # x=50,
#         #     # y=50,
#         #     width=400,
#         #     height=400
#         # )

#         # musics = os.listdir('musics')
#         # for i, music in enumerate(musics):
#         #     tk.Label(self.screen, text=music).grid(row=i+1, column=1)
#         #     tk.Button(self.screen, text="Play", command=lambda i=i: self.playMusic(musics[i])).grid(row=i+1, column=2)

#         tk.Label(self.screen, text= "Enter your name: ").grid(row=1, column=0)
#         self.name_entry = tk.Entry(self.screen)
#         self.name_entry.grid(row=1, column=1)

#         self.submit_button = tk.Button(self.screen, text="Submit", command=self.submitName)
#         self.submit_button.grid(row=1, column=2)

#     def playMusic(self, music_name):
#         print(f"Playing {music_name}")
#         pygame.mixer.music.load(f"musics/{music_name}")
#         print("musics start")
#         pygame.mixer.music.play()
        

#         while pygame.mixer.music.get_busy():
#             pass
#         print("musics end")

           


#     def holdScreen(self):
#         self.screen.mainloop()

# obj = MusicsGUI()
# obj.mainScreenTitle(constant.APP_TITLE)
# obj.setIcon(constant.APP_ICON)
# obj.setGeometry(constant.APP_WIDTH, constant.APP_HEIGHT)
# obj.mainPage() 
# obj.holdScreen()


# import uuid

# print(uuid.uuid4())

# import barcode
# from barcode.writer import ImageWriter

# # Specify the data for the barcode
# data = "hi i am krishna"

# # Choose a barcode type (e.g., EAN13, Code128, etc.)
# barcode_type = barcode.get_barcode_class("code128")  # Example: Code128

# # Generate the barcode
# my_barcode = barcode_type(data, writer=ImageWriter())

# # Save the barcode as an image
# filename = my_barcode.save("my_barcode")

# print(f"Barcode saved as {filename}.png")


# import qrcode

# # Specify the data for the QR code
# data = "http://witzcode.pythonanywhere.com/"

# # Create a QR code object
# qr = qrcode.QRCode(
#     version=1,  # Controls the size of the QR Code
#     error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
#     box_size=10,  # Size of each box in the QR code grid
#     border=4,  # Thickness of the border (minimum is 4)
# )

# # Add data to the QR code
# qr.add_data(data)
# qr.make(fit=True)

# # Generate and save the QR code as an image
# img = qr.make_image(fill_color="red", back_color="white")
# img.save("my_qrcode.png")

# print("QR code saved as my_qrcode.png")

