# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/client_version.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/client_version.proto',
  package='pogoprotos.data',
  syntax='proto3',
  serialized_pb=_b('\n$pogoprotos/data/client_version.proto\x12\x0fpogoprotos.data\"$\n\rClientVersion\x12\x13\n\x0bmin_version\x18\x01 \x01(\tb\x06proto3')
)




_CLIENTVERSION = _descriptor.Descriptor(
  name='ClientVersion',
  full_name='pogoprotos.data.ClientVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_version', full_name='pogoprotos.data.ClientVersion.min_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=93,
)

DESCRIPTOR.message_types_by_name['ClientVersion'] = _CLIENTVERSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientVersion = _reflection.GeneratedProtocolMessageType('ClientVersion', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTVERSION,
  __module__ = 'pogoprotos.data.client_version_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.ClientVersion)
  ))
_sym_db.RegisterMessage(ClientVersion)


# @@protoc_insertion_point(module_scope)
