#rockpaperscissor_gui.py
import tkinter as tk
import random as rn
import rockpaperscissor as rps


class RockPaperScissor:
    def __init__(self):
        self.rps = rps.RockPaperScissor()
        self.root = tk.Tk()
        self.playerA = tk.StringVar()
        self.playerA.set('Pick your answer')
        self.playerB = tk.StringVar()
        self.playerB.set('Pick your answer')
        self.result = tk.StringVar()
        self.rps.playerA_score = tk.StringVar()
        self.rps.playerB_score = tk.StringVar()
        self.choices = ('rock', 'paper', 'scissor')
        self.label_choices = (self.playerA, self.playerB, self.result)

        for item in self.label_choices:
            self.label = tk.Label(self.root, textvariable=item)
            self.label.pack()
        for item in self.choices:
            self.radiobutton = tk.Radiobutton(self.root, text=item,
                                              variable=self.playerA,
                                              value=item)
            self.radiobutton.pack()

        self.button = tk.Button(self.root,
                                text='update',
                                command=self.update).pack()
        self.root.mainloop()

    def update(self):
        self.playerB_answer = rn.choice(self.choices)
        self.playerB.set(self.playerB_answer)
        player = self.playerA.get()
        computer = self.playerB.get()
        self.rps.play(player, computer)
        answer = self.rps.get_result()
        self.result.set(answer)


if __name__ == '__main__':
    RockPaperScissor()