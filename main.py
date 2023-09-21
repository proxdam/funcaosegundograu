from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

import matplotlib.pyplot as plt
import numpy as np
window = (300,600)
class FuncApp(App):
    def build(self):
        self.title = "Função do Segundo Grau"
        layout = BoxLayout(orientation="vertical")

        a_label = Label(text="Informe o coeficiente 'a':")
        layout.add_widget(a_label)
        self.a_input = TextInput(multiline=False)
        layout.add_widget(self.a_input)

        b_label = Label(text="Informe o coeficiente 'b':")
        layout.add_widget(b_label)
        self.b_input = TextInput(multiline=False)
        layout.add_widget(self.b_input)

        c_label = Label(text="Informe o coeficiente 'c':")
        layout.add_widget(c_label)
        self.c_input = TextInput(multiline=False)
        layout.add_widget(self.c_input)

        plot_button = Button(text="Plotar Função")
        plot_button.bind(on_press=self.plot_func)
        layout.add_widget(plot_button)

        return layout

    def plot_func(self, instance):
        a = float(self.a_input.text)
        b = float(self.b_input.text)
        c = float(self.c_input.text)

        def func(x, a, b, c):
            return a * x**2 + b * x + c

        x = np.linspace(-10, 10, 100)
        y = func(x, a, b, c)

        plt.plot(x, y)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(f'Função do Segundo Grau: {a}x^2 + {b}x + {c}')
        plt.grid()
        plt.show()

if __name__ == '__main__':
    FuncApp().run()
