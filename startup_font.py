import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

def set_korean_font():
    font_path = os.path.join(os.path.dirname(__file__), "NanumGothic-Regular.ttf")

    if not os.path.exists(font_path):
        raise FileNotFoundError("NanumGothic-Regular.ttf 폰트 파일이 존재하지 않습니다.")

    fm.fontManager.addfont(font_path)
    plt.rcParams["font.family"] = "NanumGothic"
    plt.rcParams["axes.unicode_minus"] = False
