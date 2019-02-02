#!/usr/bin/env python3
#_*_coding: utf-8 _*_

"""
将biblatex.TEX文件分成多个子文件，方便与中译版进行比较
"""

import os
import sys
import subprocess
import re


def splittexfile(inputfile):
    print('default encoding is:',sys.getdefaultencoding())
    print('split file:',inputfile)
    f=open(inputfile,'r',encoding="utf-8")
    print(f)
    if f:
        print('file read successful')
    else:
        print('file read failed,please check the encoding of the file')
        print('encoding of the input file should be utf-8, other than utf08-bom')

    if 0:
        while True:
            line = f.readline()
            print(line)
            if not line: # EOF
                break

    regxplist=[r'\\documentclass\{ltxdockit\}',r'\\begin\{document\}',
               r'\\section\{Introduction\}',r'\\section\{Database Guide\}',
               r'\\section\{User Guide\}',r'\\section\{Author Guide\}',r'\\appendix']
    filelist=["new0-preamble.tex","new1-beforeintro.tex","new2-Introduction.tex",
               "new3-DatabaseGuide.tex","new4-UserGuide.tex",
               "new5-AuthorGuide.tex","new6-Appendix.tex"]

    if 1:
        ftow=open("temp.tex",'w',encoding="utf-8")
        k=0
        j=0
        i=-1
        filecontents=f.readlines()
        for fileline in filecontents:
            k=k+1
            #print(k,fileline)
            stridx=-1
            res=re.match(regxplist[j],fileline)
            if res:
                stridx=1
                i=j
                j=j+1
                if j>6:#最后一段不用再判断，避免超出列表范围
                    j=j-1
                print("stridx=",stridx)
                print("i     =",i)
                print("j     =",j)
                print(fileline)

            
            if stridx>=0 :
                if i==0: #if条件选择,elif,else共用
                    if ftow.closed:
                        ftow=open(filelist[0],'w',encoding="utf-8")
                    else:
                        ftow.close()
                        ftow=open(filelist[0],'w',encoding="utf-8")
                elif i==1:
                    if ftow.closed:
                        ftow=open(filelist[1],'w',encoding="utf-8")
                    else:
                        ftow.close()
                        ftow=open(filelist[1],'w',encoding="utf-8")
                elif i==2:
                    if ftow.closed:
                        ftow=open(filelist[2],'w',encoding="utf-8")
                    else:
                        ftow.close()
                        ftow=open(filelist[2],'w',encoding="utf-8")
                elif i==3:
                    if ftow.closed:
                        ftow=open(filelist[3],'w',encoding="utf-8")
                    else:
                        ftow.close()
                        ftow=open(filelist[3],'w',encoding="utf-8")
                elif i==4:
                    if ftow.closed:
                        ftow=open(filelist[4],'w',encoding="utf-8")
                    else:
                        ftow.close()
                        ftow=open(filelist[4],'w',encoding="utf-8")
                elif i==5:
                    if ftow.closed:
                        ftow=open(filelist[5],'w',encoding="utf-8")
                    else:
                        ftow.close()
                        ftow=open(filelist[5],'w',encoding="utf-8")
                elif i==6:
                    if ftow.closed:
                        ftow=open(filelist[6],'w',encoding="utf-8")
                    else:
                        ftow.close()
                        ftow=open(filelist[6],'w',encoding="utf-8")
                    
                ftow.write(fileline)
            else:
                ftow.write(fileline)
        ftow.close()
    
    f.close()


def main():
    print("开始分割!")
    print(os.getcwd())#路径问题
    splittexfile('biblatex.tex')
    pass
    print("分割结束!")

if __name__ == "__main__":
    main()