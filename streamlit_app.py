import openai
import streamlit as st
import os

# Autenticación de OpenAI (oculta la clave en una variable de entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")



# Mostrar el título de la app
st.title('GPT-3 Text-Davinci-003')

# Mostrar una imagen
# st.image('https://i.imgur.com/3TfTl8A.png')

# Mostrar una descripción
st.markdown("Esta aplicación usa GPT-3 Text-Davinci-003 de OpenAI para producir artículos.")

# Obtener la búsqueda del usuario
query = st.text_input('Introduzca el título de su artículo:')

# Generar el artículo
if query:
    article = openai.Completion.create(
        engine="text-davinci-003",
        prompt=query,
        max_tokens=2500,
        temperature=0.7,
        top_p=0.9
    )
    st.write(article['choices'][0]['text'])

# Mostrar un botón de créditos
if st.button('Créditos'):
    st.markdown('Creado por [Moris Polanco] usando [OpenAI](https://openai.com/) y [Streamlit](https://www.streamlit.io/).')
