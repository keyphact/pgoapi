# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Data/Avatar/AvatarItem.proto

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
  name='POGOProtos/Data/Avatar/AvatarItem.proto',
  package='POGOProtos.Data.Avatar',
  syntax='proto3',
  serialized_pb=_b('\n\'POGOProtos/Data/Avatar/AvatarItem.proto\x12\x16POGOProtos.Data.Avatar\"R\n\nAvatarItem\x12\x1a\n\x12\x61vatar_template_id\x18\x01 \x01(\t\x12\x18\n\x10new_timestamp_ms\x18\x02 \x01(\x03\x12\x0e\n\x06viewed\x18\x03 \x01(\x08\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_AVATARITEM = _descriptor.Descriptor(
  name='AvatarItem',
  full_name='POGOProtos.Data.Avatar.AvatarItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='avatar_template_id', full_name='POGOProtos.Data.Avatar.AvatarItem.avatar_template_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_timestamp_ms', full_name='POGOProtos.Data.Avatar.AvatarItem.new_timestamp_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='viewed', full_name='POGOProtos.Data.Avatar.AvatarItem.viewed', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=67,
  serialized_end=149,
)

DESCRIPTOR.message_types_by_name['AvatarItem'] = _AVATARITEM

AvatarItem = _reflection.GeneratedProtocolMessageType('AvatarItem', (_message.Message,), dict(
  DESCRIPTOR = _AVATARITEM,
  __module__ = 'POGOProtos.Data.Avatar.AvatarItem_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Avatar.AvatarItem)
  ))
_sym_db.RegisterMessage(AvatarItem)


# @@protoc_insertion_point(module_scope)
