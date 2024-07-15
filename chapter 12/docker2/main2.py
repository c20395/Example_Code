# Example 12.12c
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.title('Streamlit Plotting')
selectbox = st.sidebar.selectbox(
    "What you do like to plot?",
    ("Sin", "Cos")
)
x = np.linspace(-np.pi, np.pi, 50) 
if selectbox == "Sin":
    y1 = np.sin(x)
    plt.plot(x, y1, color = 'blue', marker = "s", label='Sin') 
else:
    y1 = np.cos(x)
    plt.plot(x, y1, color = 'red', marker = "d", label='Cos') 
plt.legend()
plt.show()
st.pyplot()
