import requests
import itchat

KEY = 'fd2e7ed85a1c4d7a9ac3c8407ee0d153'

# 向api发送请求


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'pth-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

# 注册方法


@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    defaultReply = 'I received: ' + msg['Text']
    # 如果图灵Key出现问题，那么reply将会是None
    reply = get_response(msg['Text'])
    return reply or defaultReply


itchat.auto_login(hotReload=True)
itchat.run()
