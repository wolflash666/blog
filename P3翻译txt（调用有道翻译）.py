from urllib import request, parse
import re
import json
import changeip

#有道翻译接口
def fanyi(content):
    req_url = 'http://fanyi.youdao.com/translate'  # 创建连接接口
    # 创建要提交的数据
    Form_Date = {}
    Form_Date['i'] = content  # 要翻译的内容可以更改
    Form_Date['doctype'] = 'json'

    data = parse.urlencode(Form_Date).encode('utf-8') #数据转换
    response = request.urlopen(req_url, data) #提交数据并解析
    html = response.read().decode('utf-8')  #服务器返回结果读取
    #print(html)
    translate_results = json.loads(html)  #以json格式载入
    translate_results = translate_results['translateResult'][0][0]['tgt']  # json格式调取
    return translate_results #输出结果


# 写TXT文档
def write_txt(path, content):
    with open(path, 'a+') as f:
        f.write(content + "\n")

# 翻译txt文档
def fanyi_txt(path):
    i = 0
    with open(path, 'r') as f1:
        list1 = f1.readlines(10000000)
    for s in list1:
        if s.find("="):
            try:
                ens = s[s.find("="):len(s)]
                chs = fanyi(ens)
                s = s[0:s.find("=")] + chs
                print("写入%s", s)
                write_txt("cn.txt", s)
            except Exception as err:
                print(err)
        else:
            print("写入%s", s)
            write_txt("cn.txt", s)
        #有道翻译接口调用达到一定的数量会禁IP，因此需要进路由器拨号重连换IP，调用“P2登陆路由管理页面换IP.py”，文件名改为“changeip.py”
    	i = i + 1
        while i > 700:
            changeip.reconn('http://admin:password@192.168.1.1/RST_st_poe.htm')
            print("改变IP成功，继续翻译")
            i=0
            continue

if __name__ == '__main__':
    fanyi_txt("en.txt")
