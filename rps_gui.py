import tkinter as tk
import rockpaperscissor as rps


class MyFrame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.value = tk.StringVar()
        self.result = tk.StringVar()
        self.choice = ('rock', 'paper', 'scissor')
        self.rps = rps.RockPaperScissor()
        for i in self.choice:
            self.radio = tk.Radiobutton(self,
                                        text=i,
                                        variable=self.value,
                                        value=i).pack()
        self.button = tk.Button(self,
                                text='play',
                                command=self.play).pack()
        self.label = tk.Label(self,
                              text=self.result).pack()

    def play(self):
        playerA = self.value.get()
        playerB = rps.computer()
        self.rps.play(playerA, playerB)
        self.result.set('result: {0}'.format(self.result))

if __name__ == '__main__':
    MyFrame().mainloop()