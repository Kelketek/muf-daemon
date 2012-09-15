#!/usr/bin/env python
import sys
sys.path.append("muf_modules")
import time

from twisted.internet import reactor, defer
from twisted.internet.protocol import ClientCreator
from twisted.protocols import amp
from command_amp import ProtoMsg

import muf_pbuff_pb2

def decode(status):
    data=muf_pbuff_pb2.ResponseStatus()
    data.ParseFromString(status)
    return [ data.status_code, data.status_message ]

def refize(field, site, id):
    field.site_id=site
    field.object_id=id

def testkill():
    testmessage=muf_pbuff_pb2.CommandMessage()
    testmessage.type=muf_pbuff_pb2.KILL
    testmessage.kill_command_fields.pid=100
    return testmessage.SerializeToString()

def testexecution():
    testmessage=muf_pbuff_pb2.CommandMessage()
    testmessage.type=muf_pbuff_pb2.EXECUTE
    fields=testmessage.execute_command_fields
    fields.pid=100
    fields.instruction_count=10
    return testmessage.SerializeToString()

def testprogram():
    testmessage=muf_pbuff_pb2.CommandMessage()
    testmessage.type=muf_pbuff_pb2.INIT
    fields=testmessage.init_command_fields
    fields.raw_code=open('example.muf', 'r').read()
    fields.pid=100
    fields.site_id=1
    refize(fields.user, 1, 2)
    refize(fields.prog, 1, 4)
    refize(fields.priv_user, 1, 2)
    refize(fields.room, 1, 0)
    refize(fields.me, 1, 2)
    refize(fields.loc, 1, 0)
    refize(fields.trigger, 1, 3)
    fields.command=""
    #fields.instrlimit=10
    fields.m_level=2
    return testmessage.SerializeToString()

def get_proto(response):
    status=decode(response['response'])
    print "Daemon reported: " + str(status)

def exec_proto(deferred_proto, message):
    return deferred_proto.callRemote(ProtoMsg, message = message)

def do_proto(message):
    client = ClientCreator(reactor, amp.AMP).connectTCP('127.0.0.1', 1234)
    client.addCallback(exec_proto, (message))
    client.addCallback(get_proto)
    client.message = message

if __name__ == "__main__":
    do_proto(testprogram())
    do_proto(testexecution())
    do_proto(testkill())
    do_proto(testkill())
    reactor.run()
