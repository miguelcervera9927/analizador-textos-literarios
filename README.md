# Analizador Literario en Python 📖

Esta es una aplicación web interactiva construida con Python y Streamlit, diseñada para ayudar a escritores a analizar sus borradores en formato Word (.docx).

## Características
* **Extracción de texto:** Lee documentos `.docx` automáticamente.
* **Métricas clave:** Calcula el total de palabras, caracteres y el promedio de palabras por oración.
* **Filtro dinámico:** Permite al usuario excluir palabras específicas (stopwords) en tiempo real.
* **Visualización de datos:** Genera un Top 10 de las palabras más utilizadas y las grafica usando Pandas.

## Cómo ejecutarlo localmente
1. Clona este repositorio o descarga los archivos.
2. Instala las dependencias necesarias:
   `pip install -r requirements.txt`
3. Ejecuta la aplicación:
   `streamlit run app_cuentos.py`
