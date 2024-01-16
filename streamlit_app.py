import streamlit as st

def main():
    if "fullText" not in st.session_state:
        st.session_state.fullText = ""

    st.title("Cuadro de Diálogo con Botón")

    # Establecer la altura del área de texto a 200 píxeles y el formato a 'markdown'
    user_input = st.text_area("Escribe algo aquí:", st.session_state.fullText, height=200, format='markdown')

    if st.button("Enviar"):
        st.session_state.fullText = user_input.strip()

    # Mostrar el contenido del área de texto con formato Markdown
    st.markdown(f"**Contenido del Área de Texto:**\n{user_input}")

if __name__ == "__main__":
    main()
