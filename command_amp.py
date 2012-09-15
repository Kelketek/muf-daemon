#!/usr/bin/env python
from twisted.protocols import amp
class ProtoMsg(amp.Command):
    arguments = [('message', amp.String())]
    response = [('response', amp.String())] 
