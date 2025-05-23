import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

def set_korean_font():
    # 폰트 파일 경로 설정
    font_path = os.path.join(os.getcwd(), "NanumGothic-Regular.ttf")
    
    # 폰트 파일이 존재하는지 확인
    if not os.path.exists(font_path):
        raise FileNotFoundError(f"폰트 파일이 {font_path}에 존재하지 않습니다. 다운로드 후 해당 위치에 저장해주세요.")
    
    # 폰트 등록
    fm.fontManager.addfont(font_path)
    plt.rcParams["font.family"] = "NanumGothic"
    plt.rcParams["axes.unicode_minus"] = False
