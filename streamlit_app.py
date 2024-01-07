import streamlit as st

from borges_game import BorgesGame


if "chatbot" not in st.session_state:
    st.session_state.chatbot = BorgesGame()

def reset_values():
    st.session_state.messages = []
    st.session_state.chatbot.clean()

def finalize():
    st.session_state.messages = []
    assistant_text = "Mira lo que hemos escrito: \n\n"
    final_generated_text = st.session_state.chatbot.get_total_text()
    st.session_state.chatbot.clean()
    st.session_state.messages.append({"role": "assistant", "content": assistant_text + final_generated_text})


def handle_chat_input(prompt):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        response = st.session_state.chatbot.predict(prompt)
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})



def print_all_messages(messages):
    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def main():
    st.header(st.session_state.chatbot.get_initial_message())

    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    with st.sidebar:
        if st.sidebar.button("Finalizar"):
            finalize()
        if st.sidebar.button("Reiniciar"):
            reset_values()



    print_all_messages(st.session_state.messages)

    prompt = st.chat_input("Ayúdame a continuar escribiendo")
    if prompt:
        handle_chat_input(prompt)


if __name__ == "__main__":
    main()
