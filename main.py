import tkinter as tk
import random
import time
pos= 300
mult=4
class AplicativoPixelArt:
    def __init__(self, root):
        self.root = root
        self.root.title("Pixel Art")
        self.root.geometry("640x300+1500+50")
        self.canvas = tk.Canvas(root, width=750, height=540, bg="#343434")
        self.canvas.pack(expand=tk.NO, fill=tk.BOTH)

        self.canvas.create_rectangle(40, 50, 555, pos-50, outline="white")  # Cria o retângulo
        self.geracao = 0
        self.resultado = [0] * 120

        # for i in range(9, 110):
        #     cor = "black" if i % 2 == 0 else "red"
        #     self.desenha_pixel(i + (mult * i), pos-50, cor)
        
        text_item = self.canvas.create_text(50, 250, text=self.somar_resultado(), font=("Helvetica", 15), fill="white", tags="title", anchor="nw")
        btn_plot = tk.Button(root, text="plotar", command=self.plotar)
        btn_plot.place(x=560, y=90)
        btn_cl = tk.Button(root, text="Limpar", command=self.Limpar)
        btn_cl.place(x=560, y=135)
        btn_gerar = tk.Button(root, text="Gerar", command=self.regerar)
        btn_gerar.place(x=560, y=45)

    def desenha_proximo_pixel(self):
        if self.geracao > 0:
            self.geracao -= 1
            self.ram_a = random.randint(10, 110)
            self.resultado[self.ram_a] += 1
            self.root.after(1, self.desenha_proximo_pixel)


    def desenha_pixel(self, x, y, cor, tag=None):
        tamanho_pixel = 4
        x1, y1 = x - tamanho_pixel // 2, y - tamanho_pixel // 2
        x2, y2 = x + tamanho_pixel // 2, y + tamanho_pixel // 2
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=cor, outline=cor, tags=tag)

    def plotar(self):
        if hasattr(self, 'ram_a'):  # Verifica se self.ram_a está definido
            for i in range(120):
                for j in range(self.resultado[i]):
                    x = i + (i * mult)
                    y = (pos-50) - (mult * j)
                    self.canvas.create_rectangle(x, y, x+mult, y-mult, fill="yellow", outline="yellow", tags="graf")
                    print(i)
        print(self.resultado)
        self.canvas.delete("title")
        text_item = self.canvas.create_text(50, 250, text=self.somar_resultado(), font=("Helvetica", 15), fill="white", tags="title", anchor="nw")


    def Limpar(self):
        self.resultado = [0] * 120
        self.canvas.delete("graf")
        self.canvas.delete("title")
        text_item = self.canvas.create_text(50, 250, text=self.somar_resultado(), font=("Helvetica", 15), fill="white", tags="title", anchor="nw")


    def regerar(self):
        self.geracao = 1000
        self.desenha_proximo_pixel()

    def somar_resultado(self):
        total = sum(self.resultado)
        return total


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicativoPixelArt(root)
    root.mainloop()
