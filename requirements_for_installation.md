## Requirements for installation, OS X (10.9)

 1. XQuartz. http://xquartz.macosforge.org/landing/, on 20140125. Required for Matplolib.
 1. Create symbolic link to freetype2: `sudo ln -s /usr/local/opt/freetype/include/freetype2 /usr/local/include/freetype`; following http://stackoverflow.com/a/20576003/621762 on 20140125. Required for Matplolib, otherwise installation fails when some freetype contents are not found.
 1. For all others, installed via pip, see requirements.txt
 2. Ruby Childs recommends [ScipySuperpack](http://fonnesbeck.github.io/ScipySuperpack/) (accessed 20140125). The risk is that one is going outside of virtualenv with ScipySuperpack. Sergey Karayev discusses symlinking system-wide installations (which I guess include ScipySuperpack) into a virtualenv at http://sergeykarayev.com/setting-up-mountain-lion/. It seems to defeat the purpose of virtualenv, though, and I am staying with pip (20140125).

[end]
