import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import re
import os

st.set_page_config(page_title="isoelectric point plotting", page_icon="📈")

st.markdown("# isoelectric point per amino acid position")

amino_acid_sequence = st.text_input('input amino acid sequence', "MGGGKDKDKNGDEQEKGLFGHGFGHGAPGYPPQPGAYPPQGYPPQGYPPQGYPPQGYPPAGYPPGAYPPSGYPPGPSAPHQPGHSGGGLGDIVVGALGAAAAYGAHALQGVGRGGYGGGHGGYGGGHGGYGGGGYGGGHGGYGGGHGGYGGDGGGHGKFKHGGKHGGGKFKRGKFKRGKFGKKHGGGKFKKWK")
figure_size = st.slider('figure size', 1, 5, 2)

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')
def validate(seq, alphabet='dna'):
    
    alphabets = {'dna': re.compile('^[acgtn]*$', re.I), 
             'protein': re.compile('^[acdefghiklmnpqrstvwy]*$', re.I)}

    if alphabets[alphabet].search(seq) is not None:
         return True
    else:
         return False

pI_dict = {
  "A":6.00,
  "R":10.76,
  "N":5.41,
  "D":2.77,
  "C":5.07,
  "E":3.22,
  "Q":5.65,
  "G":5.97,
  "H":7.59,
  "I":6.02,
  "L":5.98,
  "K":9.74,
  "M":5.74,
  "F":5.48,
  "P":6.30,
  "U":5.68,
  "S":5.68,
  "T":5.60,
  "W":5.89,
  "Y":5.66,
  "V":5.96
}

if validate(str(amino_acid_sequence), 'protein'):
    pI_list = [pI_dict[aa] for aa in amino_acid_sequence]
    if st.checkbox('Show and download raw data'):
        st.markdown("## Raw data")
            
        pI_table = pd.DataFrame({"amino acid position":list(range(len(amino_acid_sequence))),
                        "amino acid":list(amino_acid_sequence),
                        "pI":pI_list})
        pI_table["amino acid position"] = pI_table["amino acid position"] + 1
        st.write(pI_table)
        csv = convert_df(pI_table.transpose())
        gene_name = st.text_input('input a gene name for the file', "gene_name")
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name=f'{gene_name}_pI.csv',
            mime='text/csv',
        )

    
  
    st.markdown("## Plot")
    fig = plt.figure(figsize=(8*figure_size, 6*figure_size))
    plt.plot(pI_list, 'go--')
    plt.xlabel("amino acid position")
    st.pyplot(fig)


  
else:
    print("the input seems not an amino acid sequence")
st.button("Re-run")


