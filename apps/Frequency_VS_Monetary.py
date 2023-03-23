import streamlit as st
import plotly.express as px
from snowflake.snowpark.session import Session
from config import snowflake_conn_prop
session = Session.builder.configs(snowflake_conn_prop).create()

@st.cache_data
def get_data():
    df = session.table("RFM_Clusters")
    df_pd = df.to_pandas()
    df_pd["Cluster"] = df_pd["Cluster"].astype(str)
    return df_pd

def app():
      
    st.subheader(':blue[FREQUENCY VS MONETARY :]')
    st.write(
        """
       A :green[HIGH FREQUENCY] and :green[HIGH MONETRY] customer would be considered a valuable customer who makes frequent purchases 
       and spends a significant amount of money. On the other hand, a :red[LOW FREQUENCY] and :red[LOW MONETRY] customer would be 
       considered a less valuable customer who makes infrequent purchases and spends little money.
                                                                                                                                    
       
       """
    )
    df_pd = get_data()

    st.write("")
    st.subheader("Graph")
    fig = px.scatter(
                df_pd,
                x="FREQUENCY",
                y="MONETARY",
                color="Cluster",
                opacity=0.5
            )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    
    st.write("---")
    col1, col2= st.columns((1,1))
    with col1:
        st.subheader("Table")
        st.dataframe(df_pd,width=700)
    with col2:
        st.subheader("Inference")
        st.markdown("**:blue[Cluster 2]** are your Loyalists. They generally spend more money and more frequently.")
        st.markdown("**:red[Cluster 1]** spend less money and less frequently, but they spent in the last 5 months.")
        st.markdown("**:orange[Cluster 3]** spend less money and less frequently, but they spent beyond the last 5 months.")
        st.markdown("**Cluster** **0** sit somewhere in between.")

            