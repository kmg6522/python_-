"""
Python Advanced - 나만의 패키지 만들기
Keyword - png(jpg) to gif, pil, image

"""
"""
패키지 작성
-> 정적이미지(JPG, PNG) -> GIF(애니메이션) 이미지 변환 패키지
"""

import glob
from PIL import Image

# 이미지, 결과 생성 경로
path_in = './project/images/*.png'
path_out = './project/image_out/result.gif'

# 첫 번째 이미지 & 모든 이미지 리스트 팩킹
img, *images = [Image.open(f).resize((320,240), Image.LANCZOS).convert("P", palette=Image.ADAPTIVE) for f in sorted(glob.glob(path_in))]

# print(img)
# print(images)    # 첫 이미지 제외하곤 다 여기에 저장됨

# 이미지 저장
img.save(
    fp=path_out,
    format='GIF',
    append_images=images,
    save_all=True,
    duration=500,
    loop=0
)

