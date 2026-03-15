import streamlit as st
from supabase import create_client

# Usa o que você já salvou no "cofre" do Streamlit
URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_SERVICE_KEY"]

st.set_page_config(page_title="Sistema Devasta AI", layout="wide")
st.title("🚀 Sistema Devasta - QG de Inteligência")

try:
    supabase = create_client(URL, KEY)
    res = supabase.table("configuracoes_payout").select("titular").execute()
    if res.data:
        st.balloons()
        st.success(f"✅ COMANDO ATIVADO: {res.data[0]['titular'].upper()}")
        if st.button("🔥 ATIVAR AGENTE SNIPER"):
            st.snow()
            st.info("Varredura iniciada!")
except Exception as e:
    st.error("🛰️ Quase lá! Vá ao Streamlit e dê um 'Reboot app'.")
