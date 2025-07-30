import streamlit as st
import math

# -------- Rail Fence Cipher (Encryption with N Rails) --------
def rail_fence_encrypt(message, num_rails):
    cleaned = message.replace(" ", "").lower()
    rails = ['' for _ in range(num_rails)]
    rail_index = 0
    direction = 1

    for char in cleaned:
        rails[rail_index] += char
        rail_index += direction
        if rail_index == 0 or rail_index == num_rails - 1:
            direction *= -1

    encrypted = ''.join(rails)
    return encrypted, rails

# -------- Row Transposition Cipher (Supports Alphabetic Key) --------
def row_transposition_encrypt(key, message):
    message = ''.join(ch.lower() for ch in message if ch.isalpha())
    key = key.lower()
    len_key = len(key)
    rows = math.ceil(len(message) / len_key)

    # Fill message into a matrix row-wise
    matrix = [['' for _ in range(len_key)] for _ in range(rows)]
    idx = 0
    for r in range(rows):
        for c in range(len_key):
            if idx < len(message):
                matrix[r][c] = message[idx]
                idx += 1

    # Generate column order based on sorted key
    order = sorted(list(enumerate(key)), key=lambda x: (x[1], x[0]))  # Stable sort
    col_order = [i for i, _ in order]

    # Read matrix column-wise according to col_order
    cipher_text = ''
    for c in col_order:
        for r in range(rows):
            if matrix[r][c]:
                cipher_text += matrix[r][c]

    return cipher_text

# -------- Streamlit UI --------
st.set_page_config(page_title="Encryption Tool", page_icon="🔐", layout="centered")
st.title("🔐 Encryption Ciphers: Row Transposition & Rail Fence")

# Input Section
st.subheader("📝 Enter your message and select the cipher")
message = st.text_area("Original Message", height=100)
cipher_type = st.selectbox("🔧 Choose Cipher Type", ["Row Transposition Cipher", "Rail Fence Cipher (N Rails)"])

# Key input based on cipher
if cipher_type == "Row Transposition Cipher":
    key = st.text_input("Enter alphabetic key (e.g., HACK, CIPHER1):")
else:
    rail_key = st.text_input("Enter number of rails (e.g., 3):")

# Encrypt button
if st.button("Encrypt"):
    if not message.strip():
        st.warning("Please enter a message.")
    elif cipher_type == "Row Transposition Cipher":
        if not key.strip():
            st.warning("Please enter a key.")
        elif not key.isalnum():
            st.error("Key must be alphabetic or alphanumeric (no spaces/symbols).")
        else:
            encrypted = row_transposition_encrypt(key, message)
            st.success("🔐 Encrypted Message (Row Transposition):")
            st.code(encrypted, language='text')
    else:
        if not rail_key.strip():
            st.warning("Please enter the number of rails.")
        elif not rail_key.isdigit() or int(rail_key) < 2:
            st.error("Number of rails must be a number ≥ 2.")
        else:
            num_rails = int(rail_key)
            encrypted, rails = rail_fence_encrypt(message, num_rails)
            st.success(f"🔐 Encrypted Message (Rail Fence with {num_rails} Rails):")
            st.code(encrypted, language='text')

            for i, rail in enumerate(rails):
                st.write(f" Rail {i+1}:", ' '.join(rail))
