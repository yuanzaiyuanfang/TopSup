
import requests
import json

while True:
    resptext = requests.get('http://htpmsg.jiecaojingxuan.com/msg/current',timeout=5).text
    print(resptext)
    ccc = json.loads(resptext )
    #print(ccc)
    ccc = {'code':0,'msg':'成功','data':{'event':{'answerTime':10,'desc':'7.娃娃鱼？','options':['蝾螈','大鲵','小鲵']},'type':'showQuestion'}}
    #print(ccc)
    #print(json.dumps(ccc, sort_keys=True, indent=2))

    try:
        print('状态：',ccc["msg"],'\n')
        print('题目：',ccc["data"]["event"]["desc"],'\n')
        list = ccc["data"]["event"]["options"]
        for i in list:  
            print('选项：',i,)
    except KeyError as e:
        print('Error')

    print('\n\n')
    go = input('输入回车继续运行,输入 n 回车结束运行: ')
    if go == 'n':
        break

    print('\n------------------------\n')