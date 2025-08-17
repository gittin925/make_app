import streamlit as st
import pandas as pd

st.title("CSVファイル可視化アプリ")

# ファイルアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])

if uploaded_file is not None:
    # CSVを読み込む
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 データプレビュー")
    st.write(df.head())  # 先頭5行を表示

    # 数値列を選んでグラフ化
    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if numeric_cols:
        st.subheader("📈 グラフ表示")
        selected_col = st.selectbox("数値列を選択してください", numeric_cols)
        st.line_chart(df[selected_col])
    else:
        st.warning("数値データが含まれていないため、グラフを表示できません。")