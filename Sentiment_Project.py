import streamlit as st
print(1)
st.sidebar.title("About Us")
st.sidebar.text("""We are students at ducat &
learning machine learning.
""")

st.sidebar.title("contact us")
st.sidebar.text("""Sonu @ 1111
Monu @ 22222
Chintu @ 3333
""")
print(2)



st.title("Sentiment Analysis")
text=st.text_input("Enter text")
print(3)


from textblob import TextBlob

print(4)

if st.button("Predict"):
    blob=TextBlob(text)
    sent=blob.sentiment[0]
    if sent<0:
        st.error("Negative Sentiment")
        st.image("negative.png")
    elif sent>0:
        st.success("Positive Sentiment")
        st.image("positive.png")
    else:
        st.warning("Neutral Sentiment")
        st.image("neutral.png")
        
        
