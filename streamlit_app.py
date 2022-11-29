import streamlit as st
import pandas as pd
import numpy as np

st.title('Presupuesto 2023 - León')

data = {'Enero': [100], 'Febrero': [80]}

df = pd.DataFrame(data=data)

df.head()
