import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from io import BytesIO

st.set_page_config(page_title="SalesProfit Analytics", page_icon="📈", layout="wide")

st.title("📊 SalesProfit Analytics – Dashboard Penjualan & Laba")
st.write("Aplikasi ini berjalan tanpa upload file dan menggunakan dummy data realistis.")

# -------------------------------------------------------
# GENERATE DUMMY DATA
# -------------------------------------------------------
def dummy_data():
    produk = ["Produk A", "Produk B", "Produk C", "Produk D", "Produk E"]
    margin = {"Produk A":0.29, "Produk B":0.29, "Produk C":0.42, "Produk D":0.27, "Produk E":0.25}
    base_sales = [435_000_000, 310_000_000, 250_000_000, 150_000_000, 100_000_000]
    bulan = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

    rows = []
    for p, base in zip(produk, base_sales):
        monthly = (base / 12) * (1 + np.random.normal(0, 0.08, 12))
        monthly = np.clip(monthly, 1000, None)

        for b, v in zip(bulan, monthly):
            revenue = int(v)
            cogs = int(revenue * (1 - margin[p]))
            rows.append([p, b, revenue, cogs, revenue - cogs])

    return pd.DataFrame(rows, columns=["Produ]()
