# coding: utf-8
from tqdm import tqdm
import time

# 合計値(total)を設定
bar = tqdm(total = 1000)
for i in range(100):
    # 進捗を設定
    bar.update(10)
    time.sleep(1)