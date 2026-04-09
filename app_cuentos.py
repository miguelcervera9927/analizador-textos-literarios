import streamlit as st
import docx
from collections import Counter
import pandas as pd

# --- INTERFAZ WEB ---
st.title("Analizador Literario 📖")
st.write("Sube tu borrador en formato Word para contar palabras, caracteres y ver cuáles son las palabras más usadas. Se excluyen automáticamente símbolos de interrogación, admiración, paréntesis, corchetes, guiones cortos y largos.")

# La caja de texto ahora es la única que dicta qué se excluye
st.markdown("**Filtro Personalizado:**")
palabras_extra_usuario = st.text_input("¿Qué palabras quieres excluir? (Escríbelas separadas por coma):")

archivo_subido = st.file_uploader("Elige un archivo .docx", type="docx")

# --- EL CEREBRO DE TU NOTEBOOK ---
if archivo_subido is not None:
    
    documento = docx.Document(archivo_subido)
    texto_completo = ""
    
    for parrafo in documento.paragraphs:
        texto_completo = texto_completo + parrafo.text + "\n"
        
    # NUEVO: Contamos los caracteres del texto original (incluyendo espacios)
    total_caracteres = len(texto_completo)
        
    # NUEVO: Una forma más profesional y limpia de borrar muchos símbolos
    simbolos_a_borrar = [",", ".", "—", "-", "!", "¡", "¿", "?", "(", ")", "[", "]"]
    texto_limpio = texto_completo.lower()
    
    for simbolo in simbolos_a_borrar:
        texto_limpio = texto_limpio.replace(simbolo, "")
    
    palabras_del_cuento = texto_limpio.split() 
    numero_de_palabras = len(palabras_del_cuento) 
    
    # NUEVO: La lista de palabras vacías ahora empieza 100% en blanco
    palabras_vacias = []
    
    # Solo agregamos palabras si el usuario escribió algo en la caja
    if palabras_extra_usuario != "": 
        lista_extras = palabras_extra_usuario.split(",") 
        for palabra in lista_extras:
            palabras_vacias.append(palabra.strip().lower())
            
    palabras_significativas = []
    
    for palabra in palabras_del_cuento:
        if palabra not in palabras_vacias:
            palabras_significativas.append(palabra)
            
    conteo = Counter(palabras_significativas)
    top_10 = conteo.most_common(10)
    
    lista_oraciones = texto_completo.split(".")
    total_oraciones = len(lista_oraciones)
    
    # Pequeña seguridad matemática para evitar dividir entre cero
    if total_oraciones > 0:
        promedio_palabras = (numero_de_palabras / total_oraciones)
    else:
        promedio_palabras = 0
    
    # --- MOSTRAR RESULTADOS EN PANTALLA ---
    st.divider() 
    st.success("¡Análisis completado!")
    
    # NUEVO: Dividimos la pantalla en 3 columnas en lugar de 2
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Total de Palabras", value=numero_de_palabras)
    col2.metric(label="Total de Caracteres", value=total_caracteres)
    col3.metric(label="Palabras por oración", value=round(promedio_palabras, 2))
    
    st.subheader("Top 10 palabras más usadas:")
    
    tabla_palabras = pd.DataFrame(top_10, columns=["Palabra", "Repeticiones"])
    st.dataframe(tabla_palabras, hide_index=True)
    
    st.caption("Visualización de frecuencias:")
    st.bar_chart(tabla_palabras.set_index("Palabra"))