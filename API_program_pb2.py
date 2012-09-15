# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import ref_pb2
import API_request_pb2
import API_response_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='API-program.proto',
  package='MustarAPI',
  serialized_pb='\n\x11\x41PI-program.proto\x12\tMustarAPI\x1a\tref.proto\x1a\x11\x41PI-request.proto\x1a\x12\x41PI-response.proto\"\x94\x02\n\x0e\x43ommandMessage\x12$\n\x04type\x18\x01 \x02(\x0e\x32\x16.MustarAPI.CommandType\x12\x33\n\x13init_command_fields\x18\x02 \x01(\x0b\x32\x16.MustarAPI.InitCommand\x12\x39\n\x16\x65xecute_command_fields\x18\x03 \x01(\x0b\x32\x19.MustarAPI.ExecuteCommand\x12\x33\n\x13kill_command_fields\x18\x04 \x01(\x0b\x32\x16.MustarAPI.KillCommand\x12\x37\n\x15signal_command_fields\x18\x05 \x01(\x0b\x32\x18.MustarAPI.SignalCommand\"(\n\ndictionary\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"\xfd\x02\n\x0bInitCommand\x12\x10\n\x08raw_code\x18\x01 \x02(\t\x12\x0b\n\x03pid\x18\x02 \x02(\x05\x12\x0f\n\x07site_id\x18\x03 \x02(\x05\x12\x13\n\x0binstr_limit\x18\x04 \x01(\x05\x12\x1f\n\x02me\x18\x05 \x02(\x0b\x32\x13.MuStarDatabase.Ref\x12 \n\x03loc\x18\x06 \x02(\x0b\x32\x13.MuStarDatabase.Ref\x12$\n\x07trigger\x18\x07 \x02(\x0b\x32\x13.MuStarDatabase.Ref\x12\x0f\n\x07\x63ommand\x18\x08 \x02(\t\x12\x0f\n\x07m_level\x18\t \x02(\x05\x12!\n\x04prog\x18\n \x02(\x0b\x32\x13.MuStarDatabase.Ref\x12!\n\x04room\x18\x0b \x02(\x0b\x32\x13.MuStarDatabase.Ref\x12!\n\x04user\x18\x0c \x02(\x0b\x32\x13.MuStarDatabase.Ref\x12&\n\tpriv_user\x18\r \x02(\x0b\x32\x13.MuStarDatabase.Ref\x12\r\n\x05\x64\x65\x62ug\x18\x0e \x01(\x05\"8\n\x0e\x45xecuteCommand\x12\x0b\n\x03pid\x18\x01 \x02(\x05\x12\x19\n\x11instruction_count\x18\x02 \x02(\x05\"\x1a\n\x0bKillCommand\x12\x0b\n\x03pid\x18\x01 \x02(\x05\"-\n\rSignalCommand\x12\x0e\n\x06signal\x18\x01 \x02(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\"\x9e\x01\n\x0eResponseStatus\x12\x13\n\x0bstatus_code\x18\x01 \x02(\x05\x12\x16\n\x0estatus_message\x18\x02 \x01(\t\x12\x32\n\x0frequest_message\x18\x03 \x01(\x0b\x32\x19.MustarAPI.RequestMessage\x12+\n\x0b\x61pi_reponse\x18\x04 \x01(\x0b\x32\x16.MustarAPI.APIResponse*O\n\x0b\x43ommandType\x12\x08\n\x04INIT\x10\x00\x12\x0b\n\x07\x45XECUTE\x10\x01\x12\x08\n\x04KILL\x10\x02\x12\n\n\x06SIGNAL\x10\x03\x12\x07\n\x03\x44IE\x10\x04\x12\n\n\x06STATUS\x10\x05')

_COMMANDTYPE = descriptor.EnumDescriptor(
  name='CommandType',
  full_name='MustarAPI.CommandType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='INIT', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EXECUTE', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='KILL', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='SIGNAL', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DIE', index=4, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='STATUS', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1081,
  serialized_end=1160,
)


INIT = 0
EXECUTE = 1
KILL = 2
SIGNAL = 3
DIE = 4
STATUS = 5



_COMMANDMESSAGE = descriptor.Descriptor(
  name='CommandMessage',
  full_name='MustarAPI.CommandMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='MustarAPI.CommandMessage.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='init_command_fields', full_name='MustarAPI.CommandMessage.init_command_fields', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='execute_command_fields', full_name='MustarAPI.CommandMessage.execute_command_fields', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='kill_command_fields', full_name='MustarAPI.CommandMessage.kill_command_fields', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='signal_command_fields', full_name='MustarAPI.CommandMessage.signal_command_fields', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=83,
  serialized_end=359,
)


_DICTIONARY = descriptor.Descriptor(
  name='dictionary',
  full_name='MustarAPI.dictionary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='key', full_name='MustarAPI.dictionary.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='MustarAPI.dictionary.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=361,
  serialized_end=401,
)


_INITCOMMAND = descriptor.Descriptor(
  name='InitCommand',
  full_name='MustarAPI.InitCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='raw_code', full_name='MustarAPI.InitCommand.raw_code', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pid', full_name='MustarAPI.InitCommand.pid', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='site_id', full_name='MustarAPI.InitCommand.site_id', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='instr_limit', full_name='MustarAPI.InitCommand.instr_limit', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='me', full_name='MustarAPI.InitCommand.me', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='loc', full_name='MustarAPI.InitCommand.loc', index=5,
      number=6, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='trigger', full_name='MustarAPI.InitCommand.trigger', index=6,
      number=7, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='command', full_name='MustarAPI.InitCommand.command', index=7,
      number=8, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='m_level', full_name='MustarAPI.InitCommand.m_level', index=8,
      number=9, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='prog', full_name='MustarAPI.InitCommand.prog', index=9,
      number=10, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='room', full_name='MustarAPI.InitCommand.room', index=10,
      number=11, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user', full_name='MustarAPI.InitCommand.user', index=11,
      number=12, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='priv_user', full_name='MustarAPI.InitCommand.priv_user', index=12,
      number=13, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='debug', full_name='MustarAPI.InitCommand.debug', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=404,
  serialized_end=785,
)


_EXECUTECOMMAND = descriptor.Descriptor(
  name='ExecuteCommand',
  full_name='MustarAPI.ExecuteCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='pid', full_name='MustarAPI.ExecuteCommand.pid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='instruction_count', full_name='MustarAPI.ExecuteCommand.instruction_count', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=787,
  serialized_end=843,
)


_KILLCOMMAND = descriptor.Descriptor(
  name='KillCommand',
  full_name='MustarAPI.KillCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='pid', full_name='MustarAPI.KillCommand.pid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=845,
  serialized_end=871,
)


_SIGNALCOMMAND = descriptor.Descriptor(
  name='SignalCommand',
  full_name='MustarAPI.SignalCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='signal', full_name='MustarAPI.SignalCommand.signal', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='MustarAPI.SignalCommand.data', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=873,
  serialized_end=918,
)


_RESPONSESTATUS = descriptor.Descriptor(
  name='ResponseStatus',
  full_name='MustarAPI.ResponseStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='status_code', full_name='MustarAPI.ResponseStatus.status_code', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='status_message', full_name='MustarAPI.ResponseStatus.status_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='request_message', full_name='MustarAPI.ResponseStatus.request_message', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='api_reponse', full_name='MustarAPI.ResponseStatus.api_reponse', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=921,
  serialized_end=1079,
)

_COMMANDMESSAGE.fields_by_name['type'].enum_type = _COMMANDTYPE
_COMMANDMESSAGE.fields_by_name['init_command_fields'].message_type = _INITCOMMAND
_COMMANDMESSAGE.fields_by_name['execute_command_fields'].message_type = _EXECUTECOMMAND
_COMMANDMESSAGE.fields_by_name['kill_command_fields'].message_type = _KILLCOMMAND
_COMMANDMESSAGE.fields_by_name['signal_command_fields'].message_type = _SIGNALCOMMAND
_INITCOMMAND.fields_by_name['me'].message_type = ref_pb2._REF
_INITCOMMAND.fields_by_name['loc'].message_type = ref_pb2._REF
_INITCOMMAND.fields_by_name['trigger'].message_type = ref_pb2._REF
_INITCOMMAND.fields_by_name['prog'].message_type = ref_pb2._REF
_INITCOMMAND.fields_by_name['room'].message_type = ref_pb2._REF
_INITCOMMAND.fields_by_name['user'].message_type = ref_pb2._REF
_INITCOMMAND.fields_by_name['priv_user'].message_type = ref_pb2._REF
_RESPONSESTATUS.fields_by_name['request_message'].message_type = API_request_pb2._REQUESTMESSAGE
_RESPONSESTATUS.fields_by_name['api_reponse'].message_type = API_response_pb2._APIRESPONSE
DESCRIPTOR.message_types_by_name['CommandMessage'] = _COMMANDMESSAGE
DESCRIPTOR.message_types_by_name['dictionary'] = _DICTIONARY
DESCRIPTOR.message_types_by_name['InitCommand'] = _INITCOMMAND
DESCRIPTOR.message_types_by_name['ExecuteCommand'] = _EXECUTECOMMAND
DESCRIPTOR.message_types_by_name['KillCommand'] = _KILLCOMMAND
DESCRIPTOR.message_types_by_name['SignalCommand'] = _SIGNALCOMMAND
DESCRIPTOR.message_types_by_name['ResponseStatus'] = _RESPONSESTATUS

class CommandMessage(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COMMANDMESSAGE
  
  # @@protoc_insertion_point(class_scope:MustarAPI.CommandMessage)

class dictionary(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DICTIONARY
  
  # @@protoc_insertion_point(class_scope:MustarAPI.dictionary)

class InitCommand(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INITCOMMAND
  
  # @@protoc_insertion_point(class_scope:MustarAPI.InitCommand)

class ExecuteCommand(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EXECUTECOMMAND
  
  # @@protoc_insertion_point(class_scope:MustarAPI.ExecuteCommand)

class KillCommand(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _KILLCOMMAND
  
  # @@protoc_insertion_point(class_scope:MustarAPI.KillCommand)

class SignalCommand(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SIGNALCOMMAND
  
  # @@protoc_insertion_point(class_scope:MustarAPI.SignalCommand)

class ResponseStatus(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSESTATUS
  
  # @@protoc_insertion_point(class_scope:MustarAPI.ResponseStatus)

# @@protoc_insertion_point(module_scope)