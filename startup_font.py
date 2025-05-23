import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os
import requests

def set_korean_font():
    if os.name == 'nt':  # Windows
        font_path = os.path.join(os.getcwd(), "NanumGothic.ttf")
    else:
        font_path = "/tmp/NanumGothic.ttf"

    if not os.path.exists(font_path):
        url = "https://github.com/naver/nanumfont/releases/download/VER2.5/NanumGothic.ttf"
        r = requests.get(url)
        with open(font_path, "wb") as f:
            f.write(r.content)

    if not font_path.endswith(".ttf") or os.path.getsize(font_path) < 10000:
        raise RuntimeError("폰트 다운로드 실패 또는 잘못된 파일 형식입니다.")

    fm.fontManager.addfont(font_path)
    plt.rcParams["font.family"] = "NanumGothic"
    plt.rcParams["axes.unicode_minus"] = False
