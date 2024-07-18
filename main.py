import streamlit as st
import pandas as pd
import random
import time
import base64

# ドラムロールの効果音のファイルパス
DRUMROLL_SOUND_PATH = "drumroll.mp3"

def get_audio_base64(file_path):
    with open(file_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
        base64_audio = base64.b64encode(audio_bytes).decode()
    return base64_audio

def load_csv(file_path):
    return pd.read_csv(file_path)

def draw_lottery(items):
    return random.choice(items)

# CSVファイルの読み込み
csv_file_path = "items.csv"
df = load_csv(csv_file_path)

# Streamlitアプリのレイアウト
st.title("くじ引きアプリ")

if st.button("くじを引く"):
    # ドラムロールの音を再生するJavaScriptコードを埋め込む
    audio_base64 = get_audio_base64(DRUMROLL_SOUND_PATH)
    audio_html = f"""
    <audio id="drumroll_audio" autoplay>
        <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
    </audio>
    <script>
    var audio = document.getElementById('drumroll_audio');
    audio.play();
    </script>
    """
    st.markdown(audio_html, unsafe_allow_html=True)
    
    # 1秒間の待機
    time.sleep(3)
    
    # くじを引く
    result = draw_lottery(df.to_dict(orient='records'))
    
    # 結果の表示
    st.write(f"結果: {result['prize']}")
    st.image(result['image_path'], use_column_width=True)

    # アンケートリンクの表示
    st.markdown("### アンケートにご協力ください")
    st.markdown("[アンケートに答える](https://example.com/survey)")