import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import load_model
from tkinter import Tk, Label, Button, Frame
from PIL import Image, ImageTk

# Cargar el dataset MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizar los datos
x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255

# Cargar el modelo previamente guardado
model = load_model('modelo_mnist.keras')

# Función para predecir 9 números aleatorios del conjunto de prueba
def predict_9_numbers():
    # Seleccionar 9 índices aleatorios
    indices = np.random.choice(len(x_test), 9, replace=False)
    images = x_test[indices]

    # Hacer las predicciones para las 9 imágenes
    predictions = model.predict(images)
    predicted_numbers = np.argmax(predictions, axis=1)
    confidences = np.max(predictions, axis=1) * 100  # Convertir a porcentaje

    # Mostrar las imágenes y las predicciones en un popup
    show_popup(images, predicted_numbers, confidences)

# Función para mostrar el popup con las predicciones
def show_popup(images, numbers, confidences):
    # Crear ventana principal
    root = Tk()
    root.title("Predicción de Números")

    # Crear un frame para organizar las imágenes en una cuadrícula
    frame = Frame(root)
    frame.pack()

    # Mostrar cada imagen con su predicción y confianza
    for i in range(9):
        # Convertir la imagen a un formato compatible con tkinter
        img = Image.fromarray((images[i].squeeze() * 255).astype(np.uint8))  # Convertir de float a uint8
        img = img.resize((100, 100))  # Redimensionar para una mejor visualización
        img = ImageTk.PhotoImage(img)

        # Crear un label para la imagen
        img_label = Label(frame, image=img)
        img_label.image = img  # Mantener una referencia para evitar que sea recolectado por el GC
        img_label.grid(row=i // 3 * 2, column=i % 3)  # Colocar en una cuadrícula de 3x3, filas pares para las imágenes

        # Crear un label para la predicción y la confianza, justo debajo de la imagen
        pred_label = Label(frame, text=f"Número: {numbers[i]}\nPrecisión: {confidences[i]:.2f}%")
        pred_label.grid(row=i // 3 * 2 + 1, column=i % 3)  # Colocar debajo de la imagen en filas impares

    # Botón para cerrar
    close_button = Button(root, text="Cerrar", command=root.destroy)
    close_button.pack()

    # Ejecutar la ventana
    root.mainloop()

# Ejecutar la predicción para 9 números
predict_9_numbers()
