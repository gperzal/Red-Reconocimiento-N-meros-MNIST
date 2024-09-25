# 🧠 Reconocimiento de Números con Red Neuronal Convolucional (CNN) 📊

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)
![Keras](https://img.shields.io/badge/Keras-2.x-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![MNIST](https://img.shields.io/badge/Dataset-MNIST-lightgrey.svg)
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

Este proyecto utiliza una **Red Neuronal Convolucional (CNN)** 🕸️ para reconocer números escritos a mano del dataset MNIST. El objetivo es predecir correctamente los dígitos de 0 a 9 a partir de imágenes de 28x28 píxeles. El proyecto incluye una implementación interactiva que muestra las predicciones del modelo utilizando una interfaz gráfica con `tkinter`. Además, se ofrece una alternativa visual con `matplotlib` para su ejecución en Google Colab. 🚀

## ✨ Funcionalidades

- 🔢 Reconocimiento de números escritos a mano utilizando un modelo CNN.
- 🖼️ Visualización interactiva de predicciones mediante `tkinter`.
- 🌐 Ejecución alternativa en Google Colab con `matplotlib`.
- 💻 Código adaptado para entornos locales y web.

## 📚 Requisitos

Para ejecutar este proyecto, necesitas tener instalado:

- Python 3.8 o superior 🐍
- TensorFlow 2.x 🧠
- Keras 2.x 🔧
- Pillow (para manejo de imágenes en `tkinter`) 🖼️
- matplotlib (para visualización alternativa en Colab) 📊

## 🛠️ Creación del Ambiente Virtual

1. Clona el repositorio y navega al directorio del proyecto:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   ```

2. Crea y activa un ambiente virtual:
   ```bash
   python -m venv venv
   # En Windows
   .\venv\Scripts\activate
   # En macOS/Linux
   source venv/bin/activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## 📋 Archivo `requirements.txt`

Crea un archivo `requirements.txt` con las siguientes dependencias:

```plaintext
tensorflow>=2.0
keras>=2.0
pillow
matplotlib
```

## 🚀 Ejecución del Código con tkinter

Este script muestra 9 imágenes de dígitos aleatorios en una ventana emergente utilizando tkinter. Asegúrate de que el modelo `modelo_mnist.keras` esté en el mismo directorio antes de ejecutar.

## 🚀 Instrucciones de Ejecución

Para ejecutar correctamente este proyecto, sigue estos pasos en orden:

1. **Crear el modelo:**
   Primero, ejecuta el script `modelo.py` para crear y entrenar el modelo. Este script generará el archivo `modelo_mnist.keras`.

   ```bash
   python modelo.py
   ```

   Este proceso puede tardar varios minutos dependiendo de tu hardware.

2. **Ejecutar la aplicación principal:**
   Una vez que el modelo esté entrenado y guardado, ejecuta el script `main.py` para iniciar la aplicación de predicción interactiva.

   ```bash
   python main.py
   ```

   Esto abrirá una ventana de Tkinter mostrando 9 imágenes de dígitos aleatorios con sus predicciones.

⚠️ **Importante:** Asegúrate de ejecutar `modelo.py` antes de `main.py`, ya que `main.py` depende del archivo `modelo_mnist.keras` generado por `modelo.py`.



## 🌐 Ejecución en Google Colab

Para ver y probar el proyecto en Google Colab, incluyendo el entrenamiento del modelo y la visualización de predicciones, visita el siguiente enlace:

🔗 [Google Colab - Entrenamiento y Predicción de Números](https://colab.research.google.com/drive/1ZwXMnNQJYu4Qc1DAb9mRnnuNMFaY6epf?usp=sharing)

## 📈 Resultados

El modelo alcanza una precisión del XX% en el conjunto de prueba del MNIST. 

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir qué te gustaría cambiar.

## 📞 Contacto

Si tienes alguna pregunta, no dudes en contactarme:

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/guido-perez-zelaya/)](https://www.linkedin.com/in/guido-perez-zelaya/)
[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&link=https://github.com/gperzal)](https://github.com/gperzal)

---

⭐️ Si te ha gustado este proyecto, ¡no olvides darle una estrella en GitHub! ⭐️
