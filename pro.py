# 将deepL Pro翻译除中文html文档（book_name_zh.html）
# 与英文原文档（book_name_en.html）合并
# 做成左右中英对照格式的文档（book_name_bi_en_zh.html）/Users/tangqiang/books/e33_identity

import os
import shutil
from bs4 import BeautifulSoup

# 复制所有
def copy_allfiles(src, dest):
    '''
    复制文件夹内所有文件：src:原文件夹；dest:目标文件夹
    '''
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)

# Python基础路径设置及待复制：
python_path = r"/Users/tangqiang/PycharmProjects/pythonProject/deepL_pro/"
css_file = r"style.css"

book_no = "j09"
book_name = "on_grand_strategy"

# 第一步：读取英文和中文文档，设置输出双语文件名
path = '/Users/tangqiang/books/{}_{}/'.format(book_no,book_name)
file_en = '{}_en.html'.format(book_name)
file_zh = '{}_zh.html'.format(book_name)
file_bi = '{}_bi_en_zh.html'.format(book_name)

# ===2022-10-25 调试代码：复制广告图片文件和style.css文件
copy_allfiles(python_path+"ad_img", path+"images")              # 复制广告图片
shutil.copyfile(python_path+"style.css", path+"style.css")      # 复制css文件





# ===


html_en = open(path + file_en, 'r', encoding='utf-8').read()    # 读取英文文件
html_zh = open(path + file_zh, 'r', encoding='utf-8').read()    # 读取中文文件

# 第二步：将英文和中文文件按段落排列好，
soup_en = BeautifulSoup(html_en, 'lxml')
raw_en = soup_en.get_text(separator=" ")
lst_en = raw_en.split("\n")

soup_zh = BeautifulSoup(html_zh, 'lxml')
raw_zh = soup_zh.get_text(separator=" ")
lst_zh = raw_zh.split("\n")

# 创建双语一一对应切按序的列表，吧lst_en和lst_zh中的元素逐一列入：
lst_bi = []
for i, el_en in enumerate(lst_en):
    if len(el_en.strip())!=0 and len(lst_zh[i])!=0:
        lst_bi.append((el_en, lst_zh[i]))
    else:
        pass

# 输出book_name_bi_en_zh.html文档

# .1）输出标题头
html_head = """
<html>
<head>
<meta content="text/html;charset=utf-8" http-equiv="Content-Type"/>
<link href="style.css" rel="stylesheet" type="text/css"/>
<title>{0} | {1}</title>
</head>
<body>

<div class ="bottom">
<div class ="top left">
<p class ="en"><img src="cover.jpg"></p></div>
<div class="top right">
<p class ="cn"><h2>{0}</h2><br /><h2>{1}</h2><br /><br /><h4>libmind.com</h4></p></div>
</div>

<div class ="bottom" style="text-align: center">
<div class ="top left">
<p class ="en">外文书中译对照5分钟机器翻译<br />基于DeepL<br />支持多语互译：英德法中俄日西等<br />支持多种格式：Epub、Mobi、PDF等<br />支持支付：国际信用卡、PayPal、MixPay<br /><a target="blank" href="https://libmind.com/zh/">上传</a></p></div>
<div class="top right">
<p class ="cn">创建完全属于你的私人图书馆<br /><a target="blank" href="https://libmind.github.io">参观样馆</a><br />藏书千本 · 独立掌控<br />全文搜索 · 多语秒切<br />听书读书 · 掌控自如<br /><a target="blank" href="https://libmind.com/zh/personal-library/">购买</a></p></div>
</div>

<div class ="bottom">
<div class ="top left">
<p><img src="images/libmind.com-1.png"></p></div>
<div class="top right">
<p><img src="images/libmind.com-2.png"></p></div>
</div>
""".format(soup_en.title.string, soup_zh.title.string)

with open(path + file_bi, "a") as f:
    f.write(f"{html_head}\n")

# .2）输出主干部分（仅文字）
for el in (lst_bi):
    if lst_bi[0]=="" and lst_bi[1]=="":
        pass
    else:
        with open(path + file_bi, "a") as f:
            f.write(f'<div class ="bottom">\n<div class ="top left">\n')
            f.write(f'<p class ="en">{el[0]}</p>')
            f.write(f'</div>\n<div class="top right">\n')
            f.write(f'<p class ="cn">{el[1]}</p>')
            f.write(f'</div>\n</div>\n')

# .3)输出末尾部分
html_end = """
<h3>现在，你终于可以畅快阅读任何语言写的任何文字了</h3>
<h3>libmind.com</h3>
<h5 style="text-align: left">&nbsp;&nbsp;在互联网高速发展的过程中，英语在知识积累方面的垄断已经彻底无法超越了，巴别塔相当于早就建成了，英语就是世界语。</h5>
<h5 style="text-align: left">&nbsp;&nbsp;不懂英语，在任何一个领域里都直接落后一大截，无论什么东⻄都只能等翻译，还要等人家愿意翻译，而且人家错译、 漏译你也不知道。 </h5>
<h5 style="text-align: left">&nbsp;&nbsp;libmind.com可以让你在第一时间把所有外文资料(含英语、德语、法语等100多种语言)直接翻译成你指定的语言和 电子书格式，还可以制成中英双语对照格式，只要上传你想翻译的电子书即可。现在上传，还送5本经典热⻔的原版书 和译本。 </h5>
<h5 style="text-align: left">&nbsp;&nbsp;libmind.com使用当前公认最好的翻译引擎DeepL，经过无数次研究测试，独家完成了任何语种的电子书都可以在5分钟内完成翻译，信达雅快。还可以把所有你喜欢的书和译本都放进一个完全属于你自己的图书馆里</h5>
<div class ="bottom"  style="text-align: center">
<div class ="top right">
<p class ="cn"><img src="images/libmind.com-4.jpg"><br /><br />机器翻译 + 双语对照版极速定制<br />即刻<a target="blank" href="https://libmind.com/zh/">上传外文书</a>，定制读本</p></div>
<div class="top right">
<p class ="cn"><img src="images/libmind.com-3.png"><br /><br /><a target="blank" href = "https://libmind.github.io">私人图书馆 样馆参观</a><br /><a target="blank" href = "https://doraemonj.github.io/about">说明</a>  ·  <a target="blank" href = "https://libmind.com/zh/personal-library/">购买</a></p></div>
</div>
<h5 style="text-align: left">&nbsp;&nbsp;我们的代码均已开源，如果你不想折腾，也没有摆弄过代码，只想体验快速、低成本且完美的双语阅读体验，请访问libmind.com，即刻开始! </h5>
<h5 style="text-align: left">&nbsp;&nbsp;建议使用端对端加密即时通信工具Mixin Messenger，
官方下载：<a target="_blank" href="https://mixin.one/messenger">https://mixin.one/messenger</a></h5>
<h5 style="text-align: left">&nbsp;&nbsp;Mixin社群：7000104144（机器猫·译站），Mixin客服：29273（机器猫）</h5>
<h5 style="text-align: left">&nbsp;&nbsp;官网：libmind.com</h5>
<h5 style="text-align: left">&nbsp;&nbsp;关注Telegram（@libmind），接收最新双语书资讯：<a target="_blank" href="https://t.me/libmind">https://t.me/libmind</a></h5>
<h5 style="text-align: left">&nbsp;&nbsp;邮箱：libmind-admin@libmind.com</h5>
<h3 style="text-align: left">&nbsp;&nbsp;“No matter where you are or what you are going through always believe that there is a light at the end of your tunnel.”</h3>
<div style="text-align: center"><img src="images/libmind.com-6.jpg"></div>
<h3 style="text-align: center">Libmind AI作品：众人祈书</h3>
"""
with open(path + file_bi, "a") as f:
    f.write(f"{html_end}")
    f.write(f"</body>\n</html>")