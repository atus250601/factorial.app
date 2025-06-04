import streamlit as st
import math
 # Đặt tiêu đề cho ứng dụng
st.title("Ứng dụng Tính Toán Cơ Bản")
 # Đặt tiêu đề phụ
st.header("Tính Giai Thừa của Một Số Tự Nhiên")
# Đoạn mô tả
st.write("Ứng dụng này cho phép bạn tính giai thừa của một số tự nhiên. Vui lòng nhập số cần tính giai thừa vào ô dưới đây và nhấn nút ’Caculate’.")
# Tạo một ô nhập số
number = st.number_input("Nhập một số tự nhiên: ", min_value=0, max_value=1000,value=0, step=1)
# Tạo button calculate
if st.button("Calculate"):
    result = math.factorial(number)
    st.success(f"Giai thừa của {number} là: {result}")