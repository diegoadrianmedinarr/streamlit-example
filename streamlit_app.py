import streamlit as st
import pandas as pd
import numpy as np

st.title('Presupuesto 2023 - León')

gasto_Mensual = {
                  "Enero": 1200,
                  "Febrero": 1400,
                  "Marzo": 1900
                }

st.bar_chart(gasto_Mensual)

