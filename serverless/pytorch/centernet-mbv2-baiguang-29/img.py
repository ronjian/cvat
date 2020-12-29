from PIL import Image
import random
from io import BytesIO
import base64
import numpy as np

# def generate_image_file(filename):
#     f = BytesIO()
#     gen = random.SystemRandom()
#     width = gen.randint(100, 800)
#     height = gen.randint(100, 800)
#     image = Image.new('RGB', size=(width, height))
#     image.save(f, 'jpeg')
#     f.name = filename
#     f.seek(0)

#     return (width, height), f


# size, buf1 = generate_image_file('test.jpg')

original_image = Image.open('/home/jiangrong/dataset/coco/val2017/000000000139.jpg')
in_buf = BytesIO()
original_image.save(in_buf, 'jpeg') # compress here!!

request_data = base64.b64encode(in_buf.getvalue()).decode('utf-8')

######################################

out_buf = BytesIO(base64.b64decode(request_data.encode('utf-8')))

# print(buf1.getvalue())
# print('==============')
# print(buf2.getvalue())
assert in_buf.getvalue() == out_buf.getvalue()

pil_img2 = Image.open(out_buf)

# image_np = np.array(pil_img2.getdata()).reshape((pil_img2.height, pil_img2.width, 3)).astype(np.uint8)

pil_img2.save('000000000139.jpg', 'jpeg')


# pil_img3 = Image.open('000000000139.jpg')
# buf3 = BytesIO()
# pil_img3.save(buf3, 'jpeg')

# print(buf3.getvalue())
# print("=================")
# print(buf1.getvalue())
# assert buf3.getvalue() == buf1.getvalue()