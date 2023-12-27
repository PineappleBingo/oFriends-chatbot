import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import HuggingFaceHub
from html_Templates import css, bot_template, user_template


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def text_correction(text):
    # 11-26-23
    text.replace("Grok", "Craig")
    text.replace("O routers", "oRouters")
    # 12-7-23
    text.replace("O router", "oRouter")

    # 9-9-23
    text.replace("몭", "fl")


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=1000, chunk_overlap=150, length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorStore(text_chunk):
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunk, embedding=embeddings)
    return vectorstore


def get_converstaion_chain(vectorstore):
    # llm = ChatOpenAI()
    llm = HuggingFaceHub(
        repo_id="google/flan-t5-xxl",
        model_kwargs={"temperature": 0.5, "max_length": 1024},
    )
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm, retriever=vectorstore.as_retriever(), memory=memory
    )
    return conversation_chain


def handle_userInput(user_question):
    response = st.session_state.conversation({"question": user_question})
    # st.write(response)
    st.session_state.chat_history = response["chat_history"]

    for i, message in enumerate(st.session_state.chat_history):
        # odd number
        if i & 2 == 0:
            st.write(
                user_template.replace("{{MSG}}", message.content),
                unsafe_allow_html=True,
            )
        else:
            st.write(
                bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True
            )


def main():
    load_dotenv()
    st.set_page_config(page_title="oFriends ChatBot", page_icon=":books:")
    # load CSS
    st.write(css, unsafe_allow_html=True)

    # Check if conversation session is already in
    # if "conversation" not in st.session_state:
    #     st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat with oFriend#10420 ChatBot")
    user_question = st.text_input("Ask anything about Overline Network")

    if user_question:
        handle_userInput(user_question)

    st.write(user_template.replace("{{MSG}}", "Hello oFriend"), unsafe_allow_html=True)
    st.write(bot_template.replace("{{MSG}}", "Hello There"), unsafe_allow_html=True)

    with st.sidebar:
        st.subheader("Your document")
        pdf_docs = st.file_uploader(
            "Upload your PDFs and click on 'Process'", accept_multiple_files=True
        )
        if st.button("Process"):
            with st.spinner("Processing"):
                # get pdf text
                raw_text = get_pdf_text(pdf_docs)
                st.write(raw_text)
                # get text chunk
                # text_chunks = get_text_chunks(raw_text)
                # st.write(text_chunks)
                # # create vector store
                # vectorstore = get_vectorStore(text_chunks)
                # # create conversation chain
                # st.session_state.conversation = get_converstaion_chain(vectorstore)


if __name__ == "__main__":
    main()
