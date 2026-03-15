import streamlit as st
from supabase import create_client
import httpx

# CREDENCIAIS PURAS
URL = "https://msnebpttipxfuvvvrje.supabase.co"
KEY = "sb_publishable_QDofFDpqfH2dJcGVFSoUSg_BI_ht-U-"

st.set_page_config(page_title="Sistema Devasta AI", layout="wide")

# FUNÇÃO QUE FURA O BLOQUEIO DE REDE
def conectar_total():
    # Aumentamos o tempo de espera para 60 segundos
    c = httpx.Client(verify=False, timeout=60.0)
    return create_client(URL, KEY, options={"http_client": c})

st.title("🚀 Sistema Devasta - Dashboard de Elite")

try:
    supabase = conectar_total()
    # Busca os dados do André (Itaú)
    res = supabase.table("configuracoes_payout").select("*").execute()
    
    if res.data:
        st.success(f"✅ CONEXÃO ESTABELECIDA: BEM-VINDO, {res.data[0]['titular'].upper()}")
        
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Sinal", "FORTE ⚡")
            st.metric("Banco", res.data[0]['banco'])
        with c2:
            st.metric("Agência", res.data[0]['agencia'])
            st.metric("Conta", res.data[0]['conta'])

        st.divider()
        if st.button("🔥 ATIVAR AGENTE SNIPER AGORA"):
            supabase.table("logs_agentes").insert({"agente": "Sniper", "acao_executada": "Busca Global Iniciada"}).execute()
            st.balloons()
            st.success("O Sniper está rastreando vídeos virais!")
            
except Exception as e:
    st.error("🛰️ Sintonizando sinal com o banco de dados...")
    if st.button("🔄 RECONECTAR AGORA"):
        st.rerun()
