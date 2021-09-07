# 関数の説明(novel.py)

```python
check(ncode)
```
### 内容
- ncodeが有効かを調べる

### 引数
- `ncode`調べるncode

### 戻り値
- `boolian`有効な場合`True`404Errorの場合`False`

```python
setup(ncode)
```
### 内容
- ディレクトリーを作成する

### 引数
- `ncode`作成するディレクトリー名

```python
part(ncode)
```
### 内容
- ページ数を取得する
- `全([0-9]+)部分`で`#pre_info`の中のページ数を取得

### 引数
- `ncode`ncodeを入力

### 戻り値
- `int`ページ数

```python
mode_all(ncode)
```

### 内容
- ncodeで取得してファイルを全て保存する

### 引数
- `ncode`ncodeを入力

