import streamlit as st

import numpy as np
import pandas as pd
import streamlit as st

my_key = st.secrets['api_key']

st.markdown("""# This is a header
## This is a sub header
This is text""")

st.write(my_key)

df = pd.DataFrame({
    'first column': list(range(1, 101)),
    'second column': np.arange(10, 1001, 10)
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 100, 3)

# and used to select the displayed lines
head_df = df.head(line_count)

head_df
