# -*- coding: utf-8 -*-
print "类的基础知识"
import base64

s1 = base64.encodestring('hello world')
s2 = base64.decodestring(s1)
print s1,s2


