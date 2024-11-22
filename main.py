import streamlit as st
import re

user_data = {}

st.title("Đăng ký tài khoản")

username = st.text_input("Tên tài khoản (bắt đầu với @)", key="register_username")
password = st.text_input("Mật khẩu", type="password", key="register_password")
confirm_password = st.text_input("Nhập lại mật khẩu", type="password", key="confirm_password")
name = st.text_input("Tên người dùng", key="register_name")
email = st.text_input("Email", key="register_email")

progress = 0
if username.startswith("@"):
    progress += 20
if password:
    progress += 20
if confirm_password:
    progress += 20
if name:
    progress += 20
if email:
    progress += 20

st.progress(progress / 100)

if st.button("Đăng ký"):
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    if not re.match(email_regex, email):
        st.error("Email không hợp lệ. Vui lòng nhập lại (ví dụ: user@example.com).")
    elif not username.startswith("@"):
        st.error("Tên tài khoản phải bắt đầu với '@'.")
    elif password != confirm_password:
        st.error("Mật khẩu không khớp. Vui lòng thử lại.")
    elif username in user_data:
        st.error("Tên tài khoản đã tồn tại. Vui lòng chọn tài khoản khác.")
    else:
        user_data[username] = {
            "password": password,
            "name": name,
            "email": email,
        }
        st.success("Đăng ký thành công!")