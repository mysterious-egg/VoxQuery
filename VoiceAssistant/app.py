
import streamlit as st
import sys
import os
import pandas as pd
# Add project root to path
current_dir = os.path.dirname(__file__)

parent_dir = os.path.abspath(
    os.path.join(current_dir, "..")
)

sys.path.insert(0, parent_dir)

# Imports
from AskQuery.data_handler import process_csv
from AskQuery import rag_engine
try:
    from speech_utils import recognize_speech
except Exception:
    recognize_speech = None


try:
    from VoiceAssistant.tts import speak
except Exception:
    speak = lambda x: None

generate_analysis = rag_engine.generate_analysis


# -----------------------------
# Page Config
# -----------------------------

st.set_page_config(
    page_title="VoxQuery",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# -----------------------------
# Session State Defaults
# -----------------------------

st.session_state.setdefault(
    "query",
    ""
)

st.session_state.setdefault(
    "response",
    "AI insights will appear here..."
)

st.session_state.setdefault(
    "last_spoken",
    ""
)

# -----------------------------
# CSS
# -----------------------------

st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}


.stApp{
background:linear-gradient(
180deg,
#0d0f14 0%,
#11141c 100%
);

color:white;
}


.block-container{
max-width:1000px;
padding-top:2rem;
margin:auto;
}


.title{

text-align:center;
font-size:58px;
font-weight:700;
margin-bottom:0px;
color:white;

}


.subtitle{

text-align:center;
font-size:18px;
color:#9aa4b2;
margin-bottom:40px;

}


.section-card{

background:rgba(255,255,255,.03);

padding:25px;

border-radius:20px;

margin-bottom:25px;

border:1px solid rgba(255,255,255,.05);

}


.section-title{

font-size:18px;
font-weight:600;
margin-bottom:15px;

}


.query-box,
.response-box{

background:#161a22;

padding:18px;

border-radius:15px;

border:1px solid rgba(255,255,255,.05);

}


.mic-btn button{

height:120px;

width:120px;

border-radius:50%;

background:linear-gradient(
135deg,
#5d5fef,
#7a54ff
);

font-size:40px;

color:white;

box-shadow:
0px 0px 30px rgba(122,84,255,.3);

}


.footer{

text-align:center;

margin-top:40px;

color:#727b86;

}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Header
# -----------------------------

def header():

    st.markdown(
        """
        <div class='title'>
        VoxQuery
        </div>

        <div class='subtitle'>
        Voice-Driven AI Data Analyst
        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------
# Upload Section
# -----------------------------

def upload_section():

    with st.container():

        st.markdown(
            """
            <div class='section-card'>
            <div class='section-title'>
            📂 Upload Dataset
            </div>
            """,
            unsafe_allow_html=True
        )

        uploaded_file = st.file_uploader(
            "",
            type=["csv"],
            label_visibility="collapsed"
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

        return uploaded_file


# -----------------------------
# Dataset Section
# -----------------------------

def dataset_section(dataset):

    st.success(
        "Dataset Loaded Successfully"
    )

    rows, cols = dataset["shape"]

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Rows",
            rows
        )

    with c2:

        st.metric(
            "Columns",
            cols
        )


    with st.expander(
        "Columns"
    ):

        for col in dataset["columns"]:

            st.write(
                f"• {col}"
            )


    with st.expander(
        "Data Types"
    ):

        for col, dtype in dataset["dtypes"].items():

            st.write(
                f"**{col}** → {dtype}"
            )


    with st.expander(
        "Missing Values"
    ):

        for col, value in dataset["missing"].items():

            st.write(
                f"**{col}** → {value}"
            )


    st.subheader(
        "Preview"
    )

    st.dataframe(
        dataset["preview"],
        use_container_width=True
    )


# -----------------------------
# Voice Section
# -----------------------------

def voice_section():

    with st.container():

        st.markdown(
            """
            <div class='section-card'>
            <div class='section-title'>
            🎤 Ask with your voice
            </div>
            """,
            unsafe_allow_html=True
        )

        c1,c2,c3=st.columns([1,2,1])

        with c2:

            st.markdown(
                '<div class="mic-btn">',
                unsafe_allow_html=True
            )

            mic_clicked=st.button(
                "🎙",
                key="mic_button",
                use_container_width=True
            )

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )

        if mic_clicked:

            status=st.info(
                "🎧 Listening..."
            )

            result=recognize_speech()

            status.empty()

            if result["success"]:

                st.session_state[
                    "query"
                ]=result["text"]

                st.success(
                    f"Recognized: {result['text']}"
                )

                st.rerun()

            else:

                st.error(
                    result["error"]
                )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


# -----------------------------
# Query Section
# -----------------------------

def query_section():

    with st.container():

        st.markdown(
            """
            <div class='section-card'>
            <div class='section-title'>
            💬 Query
            </div>
            """,
            unsafe_allow_html=True
        )

        query=st.text_input(
            "",
            value=st.session_state["query"],
            placeholder="Your question will appear here..."
        )

        st.session_state[
            "query"
        ]=query

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


# -----------------------------
# Response Section
# -----------------------------

def response_section():

    with st.container():

        st.markdown(
            """
            <div class='section-card'>
            <div class='section-title'>
            🤖 AI Response
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="response-box">',
            unsafe_allow_html=True
        )

        st.write(
            st.session_state[
                "response"
            ]
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )
# st.session_state.setdefault(
#     "last_spoken",
#     ""
# )

# current_response = st.session_state["response"]

# if (
#     current_response
#     and
#     current_response != "AI insights will appear here..."
#     and
#     current_response != st.session_state["last_spoken"]
# ):

#     speak(current_response)

#     st.session_state["last_spoken"] = current_response


# -----------------------------
# App
# -----------------------------

header()

uploaded_file=upload_section()
if uploaded_file:

    dataset = process_csv(
        uploaded_file
    )

    if "error" in dataset:

        st.error(
            dataset["error"]
        )

    else:

        # Reset file pointer
        uploaded_file.seek(0)

        # Read dataframe
        st.session_state["df"] = pd.read_csv(
            uploaded_file
        )

        # Reset vector database for new CSV
        from AskQuery.vector_store import vector_store

        vector_store.index = None
        vector_store.text_chunks = []

        dataset_section(
            dataset
        )
voice_section()

query_section()


# Gemini Analysis


if (

    st.session_state["query"]

    and

    "df" in st.session_state

):

    with st.spinner(
        "Analyzing dataset..."
    ):

        response = generate_analysis(

            st.session_state[
                "df"
            ],

            st.session_state[
                "query"
            ]
        )

        st.session_state[
            "response"
        ] = response


        # Speak only once
        if (

            response

            !=

            st.session_state[
                "last_spoken"
            ]

        ):

            speak(
                response
            )

            st.session_state[
                "last_spoken"
            ] = response

response_section()


st.markdown(
"""
<div class='footer'>
Powered by AI + Voice Intelligence
</div>
""",
unsafe_allow_html=True
)
