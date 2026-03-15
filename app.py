import streamlit as st
from supabase import create_client

# DADOS CORRIGIDOS E VALIDADOS (Removido o 'v' extra)
URL = "https://msnebpttipxfuvvvrje.supabase.co"
KEY = "sb_publishable_QDofFDpqfH2dJcGVFSoUSg_BI_ht-U-"

# Inicialização segura do cliente
try:
    supabase = create_client(URL, KEY)
except Exception as e:
    st.error(f"Erro ao configurar cliente: {e}")

st.set_page_config(page_title="Sistema Devasta AI", layout="wide", page_icon="🚀")
st.title("🚀 Sistema Devasta - Dashboard de Elite")

try:
    # Teste de conexão buscando o seu nome do banco de dados
    payout = supabase.table("configuracoes_payout").select("*").execute()
    
    if payout.data:
        st.sidebar.success(f"Conectado: {payout.data[0]['titular']}")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Status do Sistema", "ONLINE", delta="Pronto")
        with col2:
            st.metric("Titular do Payout", payout.data[0]['titular'])
        with col3:
            st.metric("Banco", payout.data[0]['banco'])
            
        st.divider()
        
        # BOTÃO DE AÇÃO DO SNIPER
        st.subheader("🕵️‍♂️ Agente Sniper")
        if st.button("🔥 DISPARAR VARREDURA GLOBAL"):
            with st.spinner("IA vasculhando tendências..."):
                supabase.table("logs_agentes").insert({
                    "agente": "Sniper", 
                    "acao_executada": "Varredura iniciada via Dashboard"
                }).execute()
                st.balloons()
                st.success("Comando enviado com sucesso ao banco de dados!")
    else:
        st.warning("Conectado, mas as tabelas parecem vazias.")

except Exception as e:
    st.error(f"🛰️ Aguardando sinal do Supabase... Detalhe: {e}")
    st.info("Se o erro persistir, verifique se o projeto no Supabase está 'Active' (Bolinha verde).")
