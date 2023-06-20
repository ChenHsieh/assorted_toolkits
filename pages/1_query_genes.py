import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Query 717 genes from Phytozome without bamboozlement", page_icon="📈")

st.markdown("# Query 717 genes from Phytozome without bamboozlement")
st.write(
    """input"""
)

hap_option = st.radio(
    "hap1 or hap2",
    ('1','2')
)

gene_id = st.text_input('gene id', 'PtXaTreH.10G046700')

components.iframe(f"https://phytozome-next.jgi.doe.gov/report/gene/PtremulaxPopulusalbaHAP{hap_option}_v5_1/{gene_id}")

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")