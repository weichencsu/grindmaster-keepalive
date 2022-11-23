import pytz
import time
import logging
import requests
import streamlit as st
from datetime import datetime, date




def main():
    MAGE_EMOJI_URL = "streamlitBKN.png"
    st.set_page_config(page_title='BRADKEN OPTIGRIND',page_icon=MAGE_EMOJI_URL, initial_sidebar_state = 'collapsed', layout="centered")
    #page_icon = favicon,
    st.markdown(
            f'''
            <style>
                .reportview-container .sidebar-content {{
                    padding-top: {0}rem;
                }}
                .appview-container .main .block-container {{
                    {f'max-width: 1000;'}
                    padding-top: {0}rem;
                    padding-right: {1}rem;
                    padding-left: {1}rem;
                    padding-bottom: {0}rem;
                    overflow: auto;
                }}
            </style>
            ''',
            unsafe_allow_html=True,
        )

    st.markdown("Reached here ")

    visitor_clicked = st.button("🚀  Hit Page")

    cnt = 1
    if visitor_clicked:
        logging.basicConfig(level=logging.DEBUG)
        s = requests.Session()

        r1 = s.get('https://weichencsu-grindmaster-kbl-app-0-0-1-ktda3w.streamlit.app')
        st.markdown('visited ' + 'https://weichencsu-grindmaster-kbl-app-0-0-1-ktda3w.streamlit.app')
        r2 = s.get('https://weichencsu-6772696e646d61737465722d6268706f64-app-0-0-1-qhx0kj.streamlit.app')
        st.markdown('visited ' + 'https://weichencsu-6772696e646d61737465722d6268706f64-app-0-0-1-qhx0kj.streamlit.app')
        r3 = s.get('https://weichencsu-grind-master-kal-app-0-0-1-iyw8gj.streamlit.app')
        st.markdown('visited ' + 'https://weichencsu-grind-master-kal-app-0-0-1-iyw8gj.streamlit.app')
        r4 = s.get('https://weichencsu-grind-master-app-0-0-1-history-page-dgnc5a.streamlit.app')
        st.markdown('visited ' + 'https://weichencsu-grind-master-app-0-0-1-history-page-dgnc5a.streamlit.app')
        r5 = s.get('https://weichencsu-grind-master-app-0-0-1-6f96e8.streamlit.app')
        st.markdown('visited ' + 'https://weichencsu-grind-master-app-0-0-1-6f96e8.streamlit.app')
        r6 = s.get('https://weichencsu-grind-master-prfi-app-0-0-1-ptfi-lnpthk.streamlit.app')
        st.markdown('visited ' + 'https://weichencsu-grind-master-prfi-app-0-0-1-ptfi-lnpthk.streamlit.app')
        r7 = s.get('https://weichencsu-grindmaster-global-app-0-0-1-bkn-wc2buh.streamlit.app')
        st.markdown('visited ' + 'https://weichencsu-grindmaster-global-app-0-0-1-bkn-wc2buh.streamlit.app')
        r8 = s.get('https://weichencsu-grindmaster-trident-app-0-0-1-byn8qc.streamlit.app')
        st.markdown('visited ' + 'https://weichencsu-grindmaster-trident-app-0-0-1-byn8qc.streamlit.app')
        r9 = s.get('https://weichencsu-sossego--736f737365676f5f736d6172746c696e6572-y6moed.streamlit.app')
        st.markdown('visited ' + 'https://weichencsu-sossego--736f737365676f5f736d6172746c696e6572-y6moed.streamlit.app')
        r10 = s.get('https://bk-milligan-grindmaster.streamlit.app')
        st.markdown('visited ' + 'https://bk-milligan-grindmaster.streamlit.app')

        hktimez = pytz.timezone("Asia/Hong_Kong") 
        timenowhk = datetime.now(hktimez)
        st.markdown("App has been visited " + str(cnt))
        cnt += 1
        st.markdown("App has been visited at " + timenowhk.strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == "__main__":
    main()

