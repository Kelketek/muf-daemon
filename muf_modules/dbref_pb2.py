# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='Dbref.proto',
  package='ProtobufMustarDatabase',
  serialized_pb='\n\x0b\x64\x62ref.proto\x12\x16ProtobufMustarDatabase\"+\n\x05\x44\x62ref\x12\x0f\n\x07site_id\x18\x01 \x02(\x05\x12\x11\n\tobject_id\x18\x02 \x02(\x05')




_DBREF = descriptor.Descriptor(
  name='Dbref',
  full_name='ProtobufMustarDatabase.Dbref',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='site_id', full_name='ProtobufMustarDatabase.Dbref.site_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='object_id', full_name='ProtobufMustarDatabase.Dbref.object_id', index=1,
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
  serialized_start=39,
  serialized_end=82,
)

DESCRIPTOR.message_types_by_name['Dbref'] = _DBREF

class Dbref(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DBREF
  
  # @@protoc_insertion_point(class_scope:ProtobufMustarDatabase.Dbref)

# @@protoc_insertion_point(module_scope)
