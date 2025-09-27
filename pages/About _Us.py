import streamlit as st
from send_emails import send_email                              

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.title("About Us")
    st.image("images/v1_place_holder.jpeg")

with col2:
    st.info(" Lorem ipsum dolor sit amet, consectetur adipiscing elit." \
    " Proin ultricies enim ac nisl mollis vulputate. Aliquam sagittis fringilla est." \
    " Proin porta euismod metus nec accumsan. Ut tincidunt justo et lacinia tempor." \
    " Integer sapien ipsum, interdum id risus eget, viverra maximus magna. " \
    "Proin in interdum neque. Vestibulum cursus sollicitudin lacus id dictum. " \
    "Vestibulum turpis libero, elementum a dignissim sit amet, euismod at sapien." \
    " Nulla pharetra magna sed luctus vulputate." \
    " Aenean in dolor massa. " \
    "In hac habitasse platea dictumst. " \
    "Sed a diam vel urna venenatis vulputate id tristique velit. " \
    "Praesent dignissim et mauris eget pretium. Nullam interdum, dui nec facilisis mollis, metus nisi consequat mauris, sit amet tempus ipsum risus non libero. Sed at volutpat orci. ")




st.header("Socials")
st.write("[Instagram](https://www.instagram.com/4kt_kari/)")
st.write("+1242-447-1037")

#with st.expander("Send Emails.:"):
 #   with st.form(key="emailer"):
  #      user_email = st.text_input("Your email address:", placeholder="user@example.com...")
#
    #    user_message = st.text_area("Your message:")
    #    button = st.form_submit_button("Submit")
     #   message = "Subject: Customer" + "\n" + user_email + "\n" + user_message
     #   if button:
        
      #      send_email(user_message=message)