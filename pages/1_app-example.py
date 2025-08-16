import streamlit as st
st.title("テキスト分析")

uploaded_file = st.file_uploader("テキストファイルをアップロード", type=["txt"])

if uploaded_file:
    content = uploaded_file.getvalue().decode("utf-8")

    new_content=st.text_area("テキスト",content)

    filename = st.text_input("保存するファイル名", "output.txt")

    if content:
        st.download_button(
            label="ダウンロード",
            data=new_content,
            file_name=filename,
            mime="text/plain"
        )