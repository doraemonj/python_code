# 将deepL Pro翻译除中文txt文档（book_name_zh.html）
# 与英文原文档（book_name_en.html）合并
# 做成左右中英对照格式的文档（book_name_bi_en_zh.html）/Users/tangqiang/books/e33_identity

from bs4 import BeautifulSoup

book_no = "j08"
book_name = "the_wonderful_wizard_of_oz"

# 第一步：读取英文和中文文档，设置输出双语文件名
path = '/Users/tangqiang/books/{}_{}/'.format(book_no,book_name)
file_en = '{}_en.txt'.format(book_name)
file_zh = '{}_zh.txt'.format(book_name)
file_bi = '{}_bi_txt_img_en_zh.html'.format(book_name)
txt_en = open(path + file_en, 'r', encoding='utf-8').read()    # 读取英文文件
txt_zh = open(path + file_zh, 'r', encoding='utf-8').read()    # 读取中文文件

# 第二步：将英文和中文文件按段落排列好，
lst_en=[]
lst_en=txt_en.split("\n")

lst_zh=[]
lst_zh=txt_zh.split("\n")

# 创建双语一一对应切按序的列表，吧lst_en和lst_zh中的元素逐一列入：
lst_bi = []
for i, el_en in enumerate(lst_en):
    lst_bi.append((el_en, lst_zh[i]))

# 输出book_name_bi_en_zh.html文档

# .1）输出标题头
html_head = """
<html>
<head>
<meta content="text/html;charset=utf-8" http-equiv="Content-Type"/>
<link href="style.css" rel="stylesheet" type="text/css"/>
<title>{} | {}</title>
</head>
<body>
""".format("The Wonderful Wizard of Oz", "绿野仙踪")

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
with open(path + file_bi, "a") as f:
    f.write(f"</body>\n</html>")