import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
st.set_option('deprecation.showPyplotGlobalUse', False)
from t2 import max_un_st,max_un_mon,min_un_st,max_lpr,min_lpr,urb_vs_urd_r,urb_vs_urd_s,ewb_vs_ewd_s
single={
    "Maximum Unemployement Rate State":max_un_st,
    "Maximum Unemployement by Month":max_un_mon,
    "Minimum Unemployement Rate State":min_un_st,
    "Maximum Labour Participation Rate":max_lpr,
    "Minimum Labour Participation Rate":min_lpr
}
graph_functions={
    "Estimated Unemployement Rate Before vs During Lockdown Region Wise":urb_vs_urd_r,
    "Estimated Unemployement Rate Before vs During Lockdown State Wise":urb_vs_urd_s,
    "Estimated Employeed Work Force by State":ewb_vs_ewd_s
}
st.title("Covid-19 Unemployement Analysis")
choice=st.selectbox("Select",list(["Graph Findings","Max or Min Findings"]))

if choice=="Max or Min Findings":
    selected_text=st.selectbox("Select to display",list(single.keys()))
    if selected_text=='Maximum Unemployement by Month':
        st.write(f"Displaying:{selected_text}")
        ot=single[selected_text]()
        b=["Time","State"]
        st.subheader(b)
        for key in ot.keys():
            a=[key,ot[key]]
            st.subheader(a)
    else:
        st.write(f"Displaying:{selected_text}")
        ot=single[selected_text]()
        st.subheader(ot)
elif choice=="Graph Findings":
    selected_graph=st.selectbox("Select to display",list(graph_functions.keys()))
    if selected_graph:
        st.write(f"Displaying:{selected_graph}")
        fig=graph_functions[selected_graph]()
        st.pyplot(fig)


