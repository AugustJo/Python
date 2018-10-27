#encoding=utf-8
import wx
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

app = wx.App()
win = wx.Frame(None, title="TXT Editor", size=(1000,666))

bkg = wx.Panel(win)

def openFile(evt):
    dlg = wx.FileDialog(
        win,
        "Open",
        "",
        "",
        "All files (*.*)|*.*",
        wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    )
    filepath = ''
    if dlg.ShowModal() == wx.ID_OK:
        filepath = dlg.GetPath()
    else:
        return
    filename.SetValue(filepath)
    fopen = open(filepath)
    fcontent = fopen.read()
    contents.SetValue(fcontent)
    fopen.close()

def saveFile(evt):
    fcontent = contents.GetValue()
    print fcontent.encode("utf-8")
    fopen = open(filename.GetValue(), 'w')
    fopen.write(fcontent)
    fopen.close()
    win = wx.Frame(None, title='TXT Editor')
    button = wx.Button(win, label='保存成功')
    win.Show()

def saveAsFile(evt):
    dlg = wx.FileDialog(
        win,
        "Open",
        "",
        "",
        "All files (*.*)|*.*",
        wx.FD_OPEN
    )
    filepath = ''
    if dlg.ShowModal() == wx.ID_OK:
        filepath = dlg.GetPath()
    else:
        return
    filename.SetValue(filepath)
    fcontent = contents.GetValue()
    fopen = open(filename.GetValue(), 'w')
    fopen.write(fcontent)
    fopen.close()
    winLocal = wx.Frame(None, title='TXT Editor')
    button = wx.Button(winLocal, label='保存成功')
    winLocal.Show()

openBtn = wx.Button(bkg, label='打开')
openBtn.Bind(wx.EVT_BUTTON, openFile)

saveBtn = wx.Button(bkg, label='保存')
saveBtn.Bind(wx.EVT_BUTTON, saveFile)

saveAsBtn = wx.Button(bkg, label='另存为')
saveAsBtn.Bind(wx.EVT_BUTTON, saveAsFile)

filename = wx.TextCtrl(bkg, style=wx.TE_READONLY)
contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE)

hbox = wx.BoxSizer()            # 布局管理 默认水平方向
hbox.Add(openBtn, proportion=0, flag=wx.LEFT | wx.ALL, border=5) # porportion=0，表示保持本身大小。border：调整控件的边框的宽度，此参数一般和flag参数配合使用。
hbox.Add(saveBtn, proportion=0, flag=wx.LEFT | wx.ALL, border=5)
hbox.Add(saveAsBtn, proportion=0, flag=wx.LEFT | wx.ALL, border=5)
hbox.Add(filename, proportion=1, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=5) # porportion=1，表示在水平方向上占三分之一的空间

bbox = wx.BoxSizer(wx.VERTICAL) # 垂直方向
bbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL)
bbox.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

if __name__=='__main__':
    bkg.SetSizer(bbox)
    win.Show()
    app.MainLoop()