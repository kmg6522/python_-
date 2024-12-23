"""
Python Advanced - 나만의 패키지 만들기 - PyPI 배포
Keyword - PyPI, build, package deploy

"""

# py_ad_4_3 : 완성된 패키지 임포트
from py_ad_4_3 import GifConverter as gfc

# 클래스 선정
c = gfc('./project/images/*.png', './project/image_out/result.gif',(320,240))

# 실행
c.convert_gif()

"""
패키지 배포 순서(PyPI)

1. https://pypi.org 회원가입
2. 프로젝트 구조 확인
3. __init__.py
4. 프로젝트 Root 필수 파일 작성
    - README.md
    - setup.py
    - setup.cfg(optional)
    - LICENSE
    - MANIFEST.in

5. pip install setuptools wheel 설치 후 빌드 업 -> 설치판 생성
    -> 설치1 : python -m pip install 
    -> 설치2 : python -m pip install --user --upgrade setuptools wheel
    -> 빌드 : python setup.py sdist bdist_wheel    # 파일 수정할 것들 있으면 수정 후에 setup.py 와서 버전만 바꾸고 다시 이과정부터 진행하면됨.

6. PyPI 배포
    -> 설치 : pip install twine
    -> 업로드 : python -m twine upload dist/*

7. 설치 확인 (pip install pygifconvt_mg)
    from pygifconvt_mg.converter import GifConverter as gc

"""
