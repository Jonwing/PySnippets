#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 用docker进行Django开发时，需要开启django debug toolbar,
# 如果你用 INTARNAL_IPS = ('xxx.xxx.xxx.xxx',)这种方式, 里面的IP一旦变化，又需要更改。
# 因此，你需要这个。


def show_toolbar(request):
    if request.is_ajax():
        return False
    return True


# 在settings 文件中加入以下配置。
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'path.to.show_toolbar',
}
