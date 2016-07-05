#encoding: utf-8

from annoy import AnnoyIndex
import random

f = 40 # 事例サンプルのベクトル次元
t = AnnoyIndex(f)
for i in xrange(1000):
    # 40次元のベクトルを生成
    v = [random.gauss(0, 1) for z in xrange(f)]
    t.add_item(i, v)

t.build(10) # 10個のtreeを作成
t.save('test.ann')

# ...

u = AnnoyIndex(f)
u.load('test.ann') # 超高速にmmapファイルができる
print(u.get_nns_by_item(0, 1000)) # 1000個の最近傍を見つける処理
for index in u.get_nns_by_item(0,1000):
    print u.get_item_vector(index)
