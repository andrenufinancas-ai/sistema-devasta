import streamlit as st
from supabase import create_client

# O código busca as chaves no "Cofre" (Secrets) do Streamlit
URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_SERVICE_KEY"]

st.set_page_config(page_title="Sistema Devasta AI", layout="wide")
st.title("🚀 Sistema Devasta - QG de Inteligência")

try:
    supabase = create_client(URL, KEY)
    res = supabase.table("configuracoes_payout").select("*").execute()
    
    if res.data:
        st.balloons()
        st.success(f"✅ ACESSO TOTAL LIBERADO: BEM-VINDO, {res.data[0]['titular'].upper()}!")
        st.info(f"Conectado ao Banco: {res.data[0]['banco']} | Agência: {res.data[0]['agencia']}")
        
        st.divider()
        if st.button("🔥 DISPARAR AGENTE SNIPER AGORA"):
            supabase.table("logs_agentes").insert({"agente": "Sniper", "acao_executada": "Ataque Total"}).execute()
            st.snow()
            st.success("O Sniper está em campo!")
except Exception as e:
    st.error("🛰️ Aguardando configuração do Cofre de Chaves...")
    st.info("André, falta apenas colocar as chaves no painel do Streamlit (Advanced Settings).")
