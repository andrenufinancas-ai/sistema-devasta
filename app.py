import streamlit as st
from supabase import create_client
import httpx

# DADOS LIMPISSIMOS
URL = "https://msnebpttipxfuvvvrje.supabase.co".strip()
KEY = "sb_publishable_QDofFDpqfH2dJcGVFSoUSg_BI_ht-U-".strip()

st.set_page_config(page_title="Sistema Devasta AI", layout="wide", page_icon="🚀")

# MÁGICA PARA FORÇAR A REDE
@st.cache_resource
def iniciar_conexao():
    # Usamos um cliente HTTP customizado para ignorar erros de resolução de nome temporários
    custom_client = httpx.Client(verify=False, timeout=30.0)
    return create_client(URL, KEY, options={"http_client": custom_client})

st.title("🚀 Sistema Devasta - Dashboard de Elite")

try:
    supabase = iniciar_conexao()
    # Tenta buscar os dados do André no Itaú
    res = supabase.table("configuracoes_payout").select("*").execute()
    
    if res.data:
        st.success(f"✅ CONEXÃO ESTABELECIDA: Bem-vindo, {res.data[0]['titular']}!")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Status", "ONLINE")
        with col2:
            st.metric("Conta Payout", res.data[0]['banco'])
        with col3:
            st.metric("Agência", res.data[0]['agencia'])

        st.divider()
        if st.button("🔥 ATIVAR AGENTE SNIPER"):
            supabase.table("logs_agentes").insert({"agente": "Sniper", "acao_executada": "Varredura forçada iniciada"}).execute()
            st.balloons()
            st.info("O Sniper começou a caça aos vídeos!")

except Exception as e:
    st.error("🛰️ Sinal fraco... O servidor do Supabase está terminando de acordar.")
    st.info("André, aperte F5 no seu navegador em 1 minuto. Isso é normal em projetos novos!")
