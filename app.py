import streamlit as st
from supabase import create_client

# Configuração que busca no cofre do Streamlit
try:
    URL = st.secrets["SUPABASE_URL"]
    KEY = st.secrets["SUPABASE_SERVICE_KEY"]
except:
    st.error("❌ O cofre está vazio! Configure os Secrets no Streamlit.")
    st.stop()

st.set_page_config(page_title="Sistema Devasta AI", layout="wide")
st.title("🚀 Sistema Devasta - QG de Inteligência")

try:
    supabase = create_client(URL, KEY)
    # Puxa o seu nome direto do banco de dados
    res = supabase.table("configuracoes_payout").select("titular").execute()
    
    if res.data:
        st.balloons()
        st.success(f"✅ COMANDO LIBERADO: BEM-VINDO, {res.data[0]['titular'].upper()}!")
        st.divider()
        if st.button("🔥 ATIVAR AGENTE SNIPER AGORA"):
            st.snow()
            st.info("Varredura global iniciada! IA caçando produtos...")
    else:
        st.warning("Conectado, mas não encontrei seu cadastro na tabela.")
except Exception as e:
    st.error("🛰️ Sintonizando sinal... Dê um 'Reboot app' no Streamlit.")
