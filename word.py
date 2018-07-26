#获取依赖
import win32com.client
import os
import os.path 
#定义常量
listTitle, listData = [], []
FileName = 'F:/word/'
#获取文件后缀
def file_extension(path): 
  return os.path.splitext(path)[1]
#循环路径文件获取内容
for parent, dirnames, filenames in os.walk(FileName):
    for filename in filenames:
        if file_extension(os.path.join(filename)) == '.html' or file_extension(os.path.join(filename)) == '.js':
            listTitle.append(os.path.join(filename))
            listData.append(open(os.path.join(parent, filename), 'r', encoding='utf-8').read())
#word操作
Word = win32com.client.Dispatch("Word.Application")
Word.Visible = True
doc = Word.Documents.Add()
for i in range(0, len(listData)):
    doc.Paragraphs.Last.Range.Text = '\n' + '<——————  文件分隔符  —————— >\n' + listTitle[i] +'\n' + listData[i] + '\n'
doc.save()
doc.Close()
Word.Quit()