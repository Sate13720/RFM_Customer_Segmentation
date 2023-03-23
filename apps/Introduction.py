import streamlit as st

def app():
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader(':blue[FREQUENCY:]')
        st.markdown("""
            <p style='font-size:20px'>
            How often did this customer make a purchase in a given period?
            Customers who purchased once are often are more likely to purchase again.
            Additionally, first time customers may be good targets for follow-up advertising to convert
            them into more frequent customers.
            </p>
        """, unsafe_allow_html=True)
        
    with col2:
        st.subheader(':blue[RECENCY:]')
        st.markdown("""
            <p style='font-size:20px'>
            How recent was the customer's last purchase?
            Customers who recently made a purchase will still have the product on their mind 
            and are more likely to purchase or use the product again. 
            Businesses often measure recency in days. 
            But, depending on the product, they may measure it in years, weeks or even hours.
            </p>
        """, unsafe_allow_html=True)
        
    with col3:
        st.subheader(':blue[MONETARY:]')
        st.markdown("""
            <p style='font-size:20px'>
            How much money did the customer spend in a given period?
            Customers who spend a lot of money are more likely to spend money in the future 
            and have a high value to a business.
            </p>
        """, unsafe_allow_html=True)
