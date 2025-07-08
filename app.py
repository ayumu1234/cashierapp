import streamlit as st
import datetime as dt

# CSSでボタンとサイドバーを装飾
st.markdown("""
<style>
/* ボタンの装飾 */
.stButton > button {
    width: 100% !important;
    height: 60px !important;
    font-size: 24px !important;
    font-weight: bold !important;
    border-radius: 15px !important;
    border: 3px solid #ddd !important;
    background: linear-gradient(145deg, #4CAF50, #45a049) !important;
    color: white !important;
    box-shadow: none !important;
    transition: all 0.3s ease !important;
    margin: 5px 0 !important;
    outline: none !important;
}

.stButton > button:hover,
.stButton > button:active,
.stButton > button:focus,
.stButton > button:focus-visible,
.stButton > button:focus-within {
    box-shadow: none !important;
    outline: none !important;
}

/* 機能ボタンの装飾 */
.stButton > button:contains("クリア") {
    background: linear-gradient(145deg, #f44336, #d32f2f) !important;
    color: white !important;
    border-color: #f44336 !important;
}

.stButton > button:contains("支払い") {
    background: linear-gradient(145deg, #2196F3, #1976D2) !important;
    color: white !important;
    border-color: #2196F3 !important;
}

.stButton > button:contains("＋") {
    background: linear-gradient(145deg, #FF9800, #F57C00) !important;
    color: white !important;
    border-color: #FF9800 !important;
}

.stButton > button:contains("利用開始") {
    background: linear-gradient(145deg, #9C27B0, #7B1FA2) !important;
    color: white !important;
    border-color: #9C27B0 !important;
}

.stButton > button:contains("総額表示画面") {
    background: linear-gradient(145deg, #607D8B, #455A64) !important;
    color: white !important;
    border-color: #607D8B !important;
}

.stButton > button:contains("戻る") {
    background: linear-gradient(145deg, #795548, #5D4037) !important;
    color: white !important;
    border-color: #795548 !important;
}

/* サイドバーの装飾 */
.sidebar .sidebar-content {
    background: linear-gradient(180deg, #f8f9fa, #e9ecef) !important;
}

/* サイドバーの金額表示を装飾 */
.sidebar .subheader {
    background: #fff !important;
    padding: 15px !important;
    border-radius: 10px !important;
    border: 2px solid #007bff !important;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1) !important;
    font-size: 18px !important;
    font-weight: bold !important;
    color: #007bff !important;
    text-align: center !important;
    margin: 10px 0 !important;
}

/* タイトルの装飾 */
h1 {
    text-align: center !important;
    color: white !important;
    font-size: 2.5em !important;
    font-weight: bold !important;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1) !important;
    margin-bottom: 30px !important;
}

/* メインコンテンツエリアの装飾 */
.main .block-container {
    padding: 2rem !important;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%) !important;
    min-height: 100vh !important;
}

/* カラム間のスペース調整 */
.row-widget.stHorizontal {
    gap: 10px !important;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #23272f 0%, #3a3f4b 100%) !important;
    color: #fff !important;
    padding-top: 30px !important;
    min-width: 400px !important;
    max-width: 400px !important;
    width: 400px !important;
}

/* サイドバー内の見出し・金額表示 */
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] .subheader,
section[data-testid="stSidebar"] div[role="heading"] {
    background: #222c3a !important;
    padding: 28px 12px !important;
    border-radius: 16px !important;
    border: 2px solid #00bfff !important;
    box-shadow: 0 6px 16px rgba(0,0,0,0.25) !important;
    font-size: 2.7em !important;
    font-weight: bold !important;
    color: #00e6ff !important;
    text-align: center !important;
    margin: 18px 0 !important;
    letter-spacing: 2px;
}

.big-red-clear button {
    width: 100% !important;
    height: 100px !important;
    font-size: 2.5em !important;
    font-weight: bold !important;
    background: linear-gradient(145deg, #f44336, #d32f2f) !important;
    color: white !important;
    border-radius: 20px !important;
    border: 4px solid #b71c1c !important;
    margin: 30px 0 !important;
    box-shadow: 0 8px 24px rgba(0,0,0,0.2) !important;
}
</style>
""", unsafe_allow_html=True)

# サイドバーの金額表示をHTMLで装飾
def sidebar_amount(text):
    st.sidebar.markdown(f'''
    <div style="
        background: #222c3a;
        padding: 20px 10px;
        border-radius: 16px;
        border: 2px solid #00bfff;
        box-shadow: 0 6px 16px rgba(0,0,0,0.25);
        font-size: 2em;
        font-weight: bold;
        color: #00e6ff;
        text-align: center;
        margin: 18px 0;
        letter-spacing: 2px;">
        {text}
    </div>
    ''', unsafe_allow_html=True)

# フラグの初期化

if "page" not in st.session_state:
    st.session_state.page = "home"
if st.session_state.page == "home":
    st.title("レジアプリ💰")
    if st.button("利用開始"):
        st.session_state.page = "page2"
        st.rerun()
elif st.session_state.page == "page2":
    st.title("会計機能💰")
    col1,col2,col3=st.columns(3)
    col4,col5,col6=st.columns(3)
    col7,col8,col9=st.columns(3)
    col10,col11,col12=st.columns(3)
    if "j" not in st.session_state:
        st.session_state.j=0
    if "i" not in st.session_state:
        st.session_state.i=0
    if "genzai" not in st.session_state:
        st.session_state.genzai=0
    if "list1" not in st.session_state:
        st.session_state.list1=[]
    if "list2" not in st.session_state:
        st.session_state.list2=[]
    if "siharai" not in st.session_state:
        st.session_state.siharai=0
    if "history" not in st.session_state:
        st.session_state.history=[]
    with col1:
        if st.button("1"):
            st.session_state.genzai=10*st.session_state.genzai+1;
            st.session_state.i+=1
    with col2:
        if st.button("2"):
            st.session_state.genzai=10*st.session_state.genzai+2;
            st.session_state.i+=1
    with col3:
        if st.button("3"):
            st.session_state.genzai=10*st.session_state.genzai+3;
            st.session_state.i+=1
    with col4:
        if st.button("4"):
            st.session_state.genzai=10*st.session_state.genzai+4;
            st.session_state.i+=1
    with col5:
        if st.button("5"):
            st.session_state.genzai=10*st.session_state.genzai+5;
            st.session_state.i+=1
    with col6:
        if st.button("6"):
            st.session_state.genzai=10*st.session_state.genzai+6;
            st.session_state.i+=1
    with col7:
        if st.button("7"):
            st.session_state.genzai=10*st.session_state.genzai+7;  
            st.session_state.i+=1
    with col8:
        if st.button("8"):
            st.session_state.genzai=10*st.session_state.genzai+8;
            st.session_state.i+=1
    with col9:
        if st.button("9"):
            st.session_state.genzai=10*st.session_state.genzai+9;  
            st.session_state.i+=1
    with col10:
        if st.button("0"):
            st.session_state.genzai=10*st.session_state.genzai;
            st.session_state.i+=1
    with col11:
        if st.button("クリア"):
            st.session_state.genzai=0
            st.session_state.i=0
            st.session_state.list1=[]
            st.session_state.j=0
            st.session_state.siharai=0
    with col12:
        if st.button("支払い"):
            st.session_state.list1.append(st.session_state.genzai)
            total=sum(st.session_state.list1)
            st.sidebar.subheader("合計金額:"+str(total)+"円")
            st.session_state.history.append(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+" "+str(total)+"円")
            st.session_state.siharai+=1
    if st.button("＋"):
        st.session_state.list1.append(st.session_state.genzai)
        st.session_state.genzai=0
        st.session_state.i=0
        st.session_state.j+=1
    if st.session_state.j>0 and st.session_state.siharai==0:
        st.sidebar.subheader("現在額："+"＋".join(str(k) for k in st.session_state.list1)+"＋"+str(st.session_state.genzai)+"円")
    elif st.session_state.j>0 and st.session_state.siharai==1:
        st.sidebar.subheader("現在額："+"＋".join(str(k) for k in st.session_state.list1)+"円")
    else:
        st.sidebar.subheader("現在額："+str(st.session_state.genzai)+"円")
    st.markdown("---")
    st.write("スマホに総額を表示するときなどにお使用ください↓")
    if st.button("総額表示画面📃📃"):
        st.session_state.page="page3"
        st.rerun()
    st.markdown("---")
    st.write("履歴を見るときなどにお使用ください↓")
    if st.button("履歴"):
        st.session_state.page="page4"
        st.rerun()
    st.markdown("---")
    if st.button("戻る"):
        st.session_state.page="home"
        st.rerun()
elif st.session_state.page=="page3":
    if st.session_state.j>0 and st.session_state.siharai==0:
        st.subheader("現在額："+"＋".join(str(k) for k in st.session_state.list1)+"＋"+str(st.session_state.genzai)+"円")
    elif st.session_state.j>0 and st.session_state.siharai==1:
        st.subheader("現在額："+"＋".join(str(k) for k in st.session_state.list1)+"円")
    else:
        st.subheader("現在額："+str(st.session_state.genzai)+"円")
    st.title(str(sum(st.session_state.list1))+"円")
    if st.button("戻る"):
        st.session_state.page="page2"
        st.rerun()
elif st.session_state.page=="page4":
    st.title("履歴⌛")
    for i in range(len(st.session_state.history)):
        st.write(st.session_state.history[i])
        st.markdown("---")

    if st.button("戻る"):
        st.session_state.page="page2"
        st.rerun()







