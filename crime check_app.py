import streamlit as st

st.set_page_config(page_title="Go'aami Dambiile", layout="centered")

st.title("🔍 Kala Saar Qofka Dambiilaha ah iyo qofka aan danbiga lehen")

# --- Inputs ---
name = st.text_input("Magaca:")
age = st.text_input("Da'da:")
crime_type = st.text_input("Nooca Falka:")
score = st.text_input("Dhibcaha (1–10):")

# --- Natiijada ---
def check_criminal_status(name, age, crime_type, score):
    try:
        age = int(age)
        score = int(score)
    except ValueError:
        return "❌ Fadlan geli da'da iyo dhibcaha si sax ah."

    if score >= 7 or crime_type.lower() in ["tuugo", "dil", "burcadnimo"]:
        return f"🚨 {name} waa dambile!"
    else:
        return f"✅ {name} ma leh wax danbi ah."

# --- Tijaabi Button ---
if st.button("Tijaabi"):
    result = check_criminal_status(name, age, crime_type, score)
    if "dambile" in result:
        st.error(result)
    elif "Fadlan" in result:
        st.warning(result)
    else:
        st.success(result)

# --- Footer ---
st.markdown("---")
st.caption("Appkan waxaa sameeyey: Faid Qaliif Ahmed © 2025")
