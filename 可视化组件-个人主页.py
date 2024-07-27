import pandas as pd
import streamlit as st
import os
from pygwalker.api.streamlit import StreamlitRenderer

# 上传文件
uploaded_file = st.file_uploader("上传csv或xlsx文件")

# 如果上传到文件不为空
if uploaded_file is not None:
    # 将xlsx格式转变成csv格式
    file_extension = os.path.splitext(uploaded_file.name)[1].lower()

    if file_extension == ".xlsx":
        # 读取 xlsx 文件为 DataFrame
        df = pd.read_excel(uploaded_file, engine='openpyxl')
    elif file_extension == ".csv":
        # 直接读取 csv 文件为 DataFrame
        df = pd.read_csv(uploaded_file)
    else:
        st.error("请上传有效的 csv 或 xlsx 文件")  # 添加无效文件类型的处理
        df = None  # 确保 df 在无效文件类型时为 None

    if df is not None:  # 确保 df 不为 None
        pyg_app = StreamlitRenderer(df)
        pyg_app.explorer()

# 在 terminal 中输入 streamlit run 可视化软件.py
