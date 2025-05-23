import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os
import requests


# 나눔고딕 다운로드 및 등록 (최초 실행 시)
def set_korean_font():
    font_path = "/tmp/NanumGothic.ttf"
    if not os.path.exists(font_path):
        url = "https://github.com/naver/nanumfont/raw/master/ttf/NanumGothic.ttf"
        r = requests.get(url)
        with open(font_path, "wb") as f:
            f.write(r.content)

    # 폰트 설정
    fm.fontManager.addfont(font_path)
    plt.rcParams["font.family"] = "NanumGothic"
    plt.rcParams["axes.unicode_minus"] = False
