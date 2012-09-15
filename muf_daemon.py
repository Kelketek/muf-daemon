#!/usr/bin/env python
import sys
sys.path.append("muf_modules")
sys.path.append("../../prototype")
import traceback

from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
from twisted.protocols import amp

from muf_data_types import *
from command_amp import ProtoMsg
import muf_object
import API_program_pb2

"""MUF interpreter. Provides a compatibility layer for Fuzzball and other MUCK server softcode."""

parser = API_program_pb2.CommandMessage()
ptable = {}
INTERNAL_ERROR=6

def reftrans(fields):
    return Dbref(fields.site_id, fields.object_id)

def execute_prog(fields):
    try:
        ptable[fields.pid]
    except KeyError:
        return 1, "No such process."
    try:
        code, message = ptable[fields.pid].execute(fields.instruction_count)
        if code != 0:
            del ptable[fields.pid]
    except:
        code = INTERNAL_ERROR
        message = str("\n!!! MUF INTERPRETER INTERNAL ERROR: \n" 
                  + traceback.format_exc()
                  + "\nPlease report this bug at https://projects.vulpinetheory.net")
        del ptable[fields.pid]
    return code, message

def kill_prog(fields):
    try:
        ptable[fields.pid]
    except KeyError:
        return 1, "No such process."
    del ptable[fields.pid]
    return 0, "Killed."

def compile_prog(fields):
    environment={ 'raw_code' : fields.raw_code, 
                  'prog' : reftrans(fields.prog),
                  'site_id' : fields.site_id,
                  'm_level' : fields.m_level, 
                  'priv_user' : reftrans(fields.priv_user),
                  'user' : reftrans(fields.user), 
                  'instr_limit' : fields.instr_limit,
                  'v_table' : [
                              reftrans(fields.me),
                              reftrans(fields.room),
                              reftrans(fields.trigger),
                              fields.command
                             ],
                  'api' : pf,
                  'v_list' :  ["me", "loc", "trigger", "command"],
                  'debug' : fields.debug
                }
    ptable[fields.pid] = muf_object.muf_program(environment)
    code, message = ptable[fields.pid].compiler()
    if code != 0:
        del ptable[fields.pid]
    return code, message


def run_command(message):
    if message.type == API_program_pb2.INIT:
        return compile_prog(message.init_command_fields)
    elif message.type == API_program_pb2.EXECUTE:
        return execute_prog(message.execute_command_fields)
    elif message.type == API_program_pb2.KILL:
        return kill_prog(message.kill_command_fields)
    else:
        return (3, "Unknown command sent from core.")

class Muf(amp.AMP):
    def data_received(self, message):
        parser.ParseFromString(message)
        code, message = run_command(parser)
        status = API_program_pb2.ResponseStatus()
        status.status_code = code
        status.status_message = message
        return {'response' : status.SerializeToString() }
    ProtoMsg.responder(data_received) 

if __name__ == "__main__":
    pf = Factory()
    pf.protocol = Muf
    reactor.listenTCP(1234, pf)
    reactor.run()
