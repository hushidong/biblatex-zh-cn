:: Copyright (c) 2012-2016 hzz

@echo off

:: compile the tex file


copy new0-preamble.tex old0-preamble.tex /Y

copy new1-beforeintro.tex old1-beforeintro.tex /Y

copy new2-Introduction.tex old2-Introduction.tex /Y

copy new3-DatabaseGuide.tex old3-DatabaseGuide.tex /Y

copy new4-UserGuide.tex old4-UserGuide.tex /Y

copy new5-AuthorGuide.tex old5-AuthorGuide.tex /Y

copy new6-Appendix.tex old6-Appendix.tex /Y


::call makeclear

pause



