import streamlit as st
import utils
import time


st.set_page_config(page_title="LangChain: Model Comparison", layout="wide")
st.title("LangChain: Model Comparison")
st.divider()

col_prompt, col_settings = st.columns([2,3])

with col_prompt:
    prompt = st.text_input(label="Ask me a question...")
    st.divider()
    submit_btn = st.button("Submit")

with col_settings:
    temperature = st.slider(label="Temperature", min_value=0.0, max_value=1.0, value=0.7)
    max_tokens = st.slider(label="Maximum Tokens", min_value=100, max_value=500, value=200, step=100)

st.divider()

col_gpt, col_gemini, col_claude, col_command = st.columns(4)

with col_gpt:
    if submit_btn:
        with st.spinner("GPT Thinking..."):
            st.success("GPT-4 Turbo")
            start_time = time.perf_counter()
            st.write(utils.ask_gpt(prompt=prompt, temperature=temperature, max_tokens=max_tokens))
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            st.caption(f"| :hourglass: {round(elapsed_time)} seconds")


with col_gemini:
    if submit_btn:
        with st.spinner("Gemini Thinking..."):
            st.info("Gemini Pro")
            start_time = time.perf_counter()
            st.write(utils.ask_gemini(prompt=prompt, temperature=temperature))
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            st.caption(f"| :hourglass: {round(elapsed_time)} seconds")


with col_claude:
    if submit_btn:
        with st.spinner("Claude Thinking..."):
            st.error("Claude 2.1")
            start_time = time.perf_counter()
            st.write(utils.ask_claude(prompt=prompt, temperature=temperature, max_tokens=max_tokens))
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            st.caption(f"| :hourglass: {round(elapsed_time)} seconds")


with col_command:
    if submit_btn:
        with st.spinner("Command Thinking..."):
            st.warning("Command")
            start_time = time.perf_counter()
            st.write(utils.ask_command(prompt=prompt, temperature=temperature, max_tokens=max_tokens))
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            st.caption(f"| :hourglass: {round(elapsed_time)} seconds")