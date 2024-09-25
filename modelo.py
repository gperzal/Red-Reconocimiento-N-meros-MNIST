# Importaciones necesarias
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam

# Cargar el dataset MNIST directamente desde TensorFlow
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocesamiento de los datos
x_train = x_train.reshape(-1, 28, 28, 1).astype('float32') / 255  # Redimensionar y normalizar las imágenes de entrenamiento
x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255    # Redimensionar y normalizar las imágenes de prueba

# Convertir las etiquetas a formato categórico (one-hot encoding)
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Definir el modelo secuencial
model = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),  # Capa convolucional
    MaxPooling2D(pool_size=(2, 2)),                                              # Capa de max pooling
    Flatten(),                                                                   # Aplanar los datos para la capa densa
    Dense(128, activation='relu'),                                               # Capa densa
    Dense(10, activation='softmax')                                              # Capa de salida con 10 neuronas para 10 clases (0-9)
])

# Compilar el modelo
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
print("Entrenando el modelo, esto puede tardar unos minutos...")
history = model.fit(x_train, y_train, validation_split=0.2, epochs=10, batch_size=32, verbose=2)

# Evaluar el modelo en el conjunto de prueba
test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)
print(f'Precisión en el conjunto de prueba: {test_accuracy:.2f}')

# Guardar el modelo en el formato moderno de Keras
model.save('modelo_mnist.keras')  # Guardar el modelo entrenado
print("Modelo guardado como 'modelo_mnist.keras'.")
