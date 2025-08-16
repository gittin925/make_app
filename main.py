# import streamlit as st

# # 表示したいPythonファイルのパス
# file_path = "sample.py"  # ここに表示したいファイル名を指定

# st.title("コード共有")
# filename="test.py"
# st.write(f"ファイル名：{filename}")

# try:
#     with open(file_path, "r", encoding="utf-8") as f:
#         code = f.read()
#     st.code(code, language="python")  # シンタックスハイライト付きで表示
# except FileNotFoundError:
#     st.error(f"{file_path} が見つかりません")

import os
import streamlit as st

files = [f for f in os.listdir() if f.endswith(".py")]
files.remove("main.py")
selected_file = st.selectbox("表示するPythonファイルを選択", files)

try:
    with open(selected_file, "r", encoding="utf-8") as f:
        code = f.read()
    st.code(code, language="python")
except FileNotFoundError:
    st.error(f"{selected_file} が見つかりません")