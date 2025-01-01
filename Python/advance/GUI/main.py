import tkinter as tk
import constant

class MusicsGUI:
    def __init__(self):
        self.screen = tk.Tk()


    def mainScreenTitle(self, title_name):
        self.screen.title(f"{title_name}")

    def setIcon(self, icon_path):
        self.screen.iconbitmap(icon_path)

    def setGeometry(self, width, height):
        self.screen.geometry(f"{width}x{height}")

    def mainPage(self):
        tk.Label(self.screen, text="Tops musics List").grid(row=0, column=0)
        # tk.Label(self.screen, text="Tops musics List").pack(side="top")
        # tk.Label(self.screen, text="Tops musics List", bg="lightblue").place(
        #     # x=50,
        #     # y=50,
        #     width=400,
        #     height=400
        # )

        for i in range(10):
            tk.Label(self.screen, text=f"Music {i+1}").grid(row=i+1, column=5)


    def holdScreen(self):
        self.screen.mainloop()

obj = MusicsGUI()
obj.mainScreenTitle(constant.APP_TITLE)
obj.setIcon(constant.APP_ICON)
obj.setGeometry(constant.APP_WIDTH, constant.APP_HEIGHT)
obj.mainPage() 
obj.holdScreen()