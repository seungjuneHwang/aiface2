print('얼굴인식 프로젝트')

import test
import face

url = 'https://entertainimg.kbsmedia.co.kr/cms/uploads/PERSON_20230425100142_a6929970038832dc461ad8ee40ef52e4.png'
# url = 'https://thumb.mt.co.kr/06/2023/01/2023010409310310068_1.jpg'
face.mk_aiface(url)
# test.web_img(url) # 함수 불러서 쓰기