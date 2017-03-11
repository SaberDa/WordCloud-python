基于python实现的词云表示
---

引入的库有：

- PIL
- wordcloud
- matplotlib

基础设置
---

**字体**：

font=os.path.join(os.path.dirname(__file__), "DroidSansFallbackFull.ttf")

**图片**：

mask = np.array(Image.open(path.join(d, "saber.png")))

ps：图片背景一定要为纯白色

**文本**：

text = open(u"ubw.txt").read().decode('gbk')


