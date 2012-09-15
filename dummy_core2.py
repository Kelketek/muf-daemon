#!/usr/bin/env python
import sys
sys.path.append("muf_modules")
import time

from twisted.internet import reactor, defer
from twisted.internet.protocol import ClientCreator
from twisted.protocols import amp
from command_amp import ProtoMsg

import muf_pbuff_pb2

class Program:
    pids={}
    slice_size = 500 # This should probably be tunable somehow.

    def run(self):
        """This runs all programs in the PID list one after another."""
        for pid, process in pids.items():
            process.execution(Program.slice_size)

    def decode(self,status):
        data = API_program_pb2.ResponseStatus()
        data.ParseFromString(status)
        return [data.status_code, data.status_message]

    def kill(self):
        testmessage = API_program_pb2.CommandMessage()
        testmessage.type = API_program_pb2.KILL
        testmessage.kill_command_fields.pid = self.pid
        server.send(message.SerializeToString())
        del Program.pids[self.pid]
        # No reason this should ever fail. If it does, abandon the process 
        # anyway to make it effectively dead.
        server.recv() 
        del self

    FINISHED=0
    REQUEST=1
    EXIT=2

    def execution(self, instrslice = slice_size):
        message = API_program_pb2.CommandMessage()
        message.type = API_program_pb2.EXECUTE
        fields = message.execute_command_fields
        fields.pid = self.pid
        fields.instruction_count = Program.slice_size
        Program.server.send(message.SerializeToString())
        while self.pid in Program.pids:
            status = API_program_pb2.ResponseStatus()
            status.ParseFromString(Program.server.recv())
            # 0 is program finished slice. 1 is "API request." 
            if not status.status_code in [Program.FINISHED, Program.REQUEST]:  
                del Program.pids[self.pid]
                # '2' is a clean exit. Otherwise, send a status message.
                if status.status_code != Program.EXIT:
                    self.worker.send_line(self.initvars['user'], status.status_message)
                del self
                break
            elif status.status_code == Program.REQUEST:
                Program.server.send(self.api_handler(status))

    def set_props(self, buff):
        """Sets properties from an object and returns a protobuf."""
        usr = buff.player_ref
        obj = buff.request_set_props_fields.object_id
        for attrib in buff.request_set_props_fields.props: # Get each of the attributes specified.
            self.worker.db_client.set_props(usr, obj, {attrib.key : attrib.value})
        message = API_response_pb2.APIResponse()
        message.type = API_response_pb2.API_STATUS
        message.status_fields.success = True
        return message.SerializeToString()

    def get_props(self, buff):
        """Gets properties on an object and returns a protobuf."""
        usr = buff.player_ref
        obj = buff.request_get_props_fields.object_id
        message = API_response_pb2.APIResponse()
        message.type = API_response_pb2.LIST_OF_PROPS
        for attrib in reversed(buff.request_get_props_fields.propnames): # Get each of the attributes specified.
            prop_dict = self.worker.db_client.get_props(usr, obj, [attrib])
            if attrib in prop_dict:
                message.list_of_props_fields.props.append(prop_dict[attrib])
        return message.SerializeToString()

    def notify_objects(self, buff):
        for item in buff.request_notify_objects_fields.object_id:
             self.worker.send_line(item, buff.request_notify_objects_fields.message)
        message = API_response_pb2.APIResponse()
        message.type = API_response_pb2.API_STATUS
        message.status_fields.success = True
        return message.SerializeToString()

    # Yurei's note: It's better to import * from ____ than to commit this violence
    # in my opinion.
    # This is here to avoid some silly long chain of if statements.
    a = API_request_pb2 # Legibility.
    calls={ a.GET_PROPS : get_props, 
            a.SET_PROPS : set_props,
            a.NOTIFY_OBJECTS : notify_objects
          }
    #del a # Not really neccessary but I hate the idea of leaving a floating variable around.
    def api_handler(self, message):
        request=API_request_pb2.RequestMessage()
        request.CopyFrom(message.request_message)
        return Program.calls[request.type](self, request)

    def __init__(self, table):
        """Initializes a new program."""
        self.pid = len(Program.pids) + random.randint(50, 500)
        self.initvars=table # May be useful for getting process info later.
        while self.pid in Program.pids:
            self.pid += 1
        self.worker = table['worker']
        message = API_program_pb2.CommandMessage()
        message.type = API_program_pb2.INIT
        fields = message.init_command_fields
        fields.raw_code = table['source']
        fields.pid = self.pid
        fields.site_id = table['site_id']
        fields.user.CopyFrom(table['user'])
        fields.prog.CopyFrom(table['program_ref'])
        fields.priv_user.CopyFrom(table['euid'])
        fields.room.CopyFrom(table['room'])
        fields.me.CopyFrom(table['user'])
        fields.loc.CopyFrom(table['room'])
        fields.trigger.CopyFrom(table['trigger'])
        fields.command = table['command']
        fields.instr_limit = table['instr_limit']
        fields.m_level=table['m_level']
        fields.debug=table['debug']
        
        Program.server.send(message.SerializeToString())
        status = self.decode(Program.server.recv())
        if status[0] != 0:
            self.pid = 0
            self.worker.send_line(table['user'], status[1])
        else:
            Program.pids[self.pid] = self
                    
def exec_cmd(self, executor_id, args, table):
    prog = Program(table)
    if prog.pid != 0:
         prog.execution()
             

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
