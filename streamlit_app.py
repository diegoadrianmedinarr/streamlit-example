import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf

st.title('Presupuesto 2023 - León')

st.write("""A continuación se muestra el presupuesto anual del año 2023 para la unidad de negocio de León""")

st.subheader('Gastos por mes')

data = {'Enero': [100], 'Febrero': [80]}

df = pd.DataFrame(data=data)

st.line_chart(data)


