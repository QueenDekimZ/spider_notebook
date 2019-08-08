from urllib import request
from urllib import parse
import json
import wx

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
Form_Data = {}

Form_Data['from']='AUTO'
Form_Data['to']='AUTO'
Form_Data['smartresult']='dict'
Form_Data['client']='fanyideskweb'
Form_Data['salt']='15652418986679'
Form_Data['sign']='472613a0e2c5a3251a394c09329381e8'
Form_Data['ts']='1565241898667'
Form_Data['bv']='05435bfabe443fca9224e64675e06aab'
Form_Data['doctype']='json'
Form_Data['version']='2.1'
Form_Data['keyfrom']='fanyi.web'
Form_Data['action']='FY_BY_REALTIME'

def request_translate(event):
    try:
        content = path_text.GetValue()
        Form_Data['i']=str(content)
        data = parse.urlencode(Form_Data).encode('utf-8')
        response = request.urlopen(url, data)
        html = response.read().decode('utf-8')
        translate_results = json.loads(html)
        temp = str(translate_results['translateResult'][0][0]['tgt'])
        #with open(temp,'r',encoding='utf-8') as f:
        content_trans.SetValue(temp)
    except:
        dlg = wx.MessageDialog(frame,"输入内容为空，请重新输入。","提示",wx.OK) #语法是(self, 内容, 标题, ID)
        dlg.ShowModal() #显示对话框
        dlg.Destroy()   #当结束之后关闭对话框

    #print("翻译结果：",translate_results['translateResult'][0][0]['tgt'])

def text_clear(event):
    if path_text.GetValue():
        path_text.Clear()
        content_trans.Clear()
    else:
        dlg = wx.MessageDialog(frame,"显示内容为空。","提示",wx.OK)
        dlg.ShowModal() 
        dlg.Destroy()   
    #frame.Close()
    
app = wx.App()

frame = wx.Frame(None,title = "DogB Translation",pos = (1000,200),size = (700,400))
path_text = wx.TextCtrl(frame,pos = (5,5),size = (290,355),style = wx.TE_MULTILINE)
tran_button = wx.Button(frame,label = "翻译",pos = (300,10),size = (85,170))
clear_button = wx.Button(frame,label = "清空",pos = (300,185),size = (85,170))
content_trans= wx.TextCtrl(frame,pos = (390,5),size = (290,355),style = wx.TE_MULTILINE)

tran_button.Bind(wx.EVT_BUTTON,request_translate)
clear_button.Bind(wx.EVT_BUTTON,text_clear)

frame.Show()
app.MainLoop()






    


