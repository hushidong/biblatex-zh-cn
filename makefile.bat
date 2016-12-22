:: Copyright (c) 2012-2016 hzz

@echo off

:: compile the tex file

call gbtclear

xelatex.exe --synctex=-1 biblatex-zh-cn.tex

xelatex.exe --synctex=-1 biblatex-zh-cn.tex

::call gbtclear



