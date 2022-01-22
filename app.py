import streamlit as st
from egoboostr719.lib import get_quote, get_gh_user_info


query_params = st.experimental_get_query_params()

if query_params:
    username = query_params["gh"][0]
    user = get_gh_user_info(username)
    col1, col2 = st.columns([1, 4])
    col1.image(user["avatar_url"])
    col2.header(get_quote(user["name"]))
else:
    st.write(get_quote())
