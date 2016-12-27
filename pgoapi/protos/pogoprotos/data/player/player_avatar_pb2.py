# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/player/player_avatar.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import gender_pb2 as pogoprotos_dot_enums_dot_gender__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/player/player_avatar.proto',
  package='pogoprotos.data.player',
  syntax='proto3',
  serialized_pb=_b('\n*pogoprotos/data/player/player_avatar.proto\x12\x16pogoprotos.data.player\x1a\x1dpogoprotos/enums/gender.proto\"\xf4\x02\n\x0cPlayerAvatar\x12\x0c\n\x04skin\x18\x02 \x01(\x05\x12\x0c\n\x04hair\x18\x03 \x01(\x05\x12\r\n\x05shirt\x18\x04 \x01(\x05\x12\r\n\x05pants\x18\x05 \x01(\x05\x12\x0b\n\x03hat\x18\x06 \x01(\x05\x12\r\n\x05shoes\x18\x07 \x01(\x05\x12(\n\x06gender\x18\x08 \x01(\x0e\x32\x18.pogoprotos.enums.Gender\x12\x0c\n\x04\x65yes\x18\t \x01(\x05\x12\x10\n\x08\x62\x61\x63kpack\x18\n \x01(\x05\x12\x13\n\x0b\x61vatar_hair\x18\x0b \x01(\t\x12\x14\n\x0c\x61vatar_shirt\x18\x0c \x01(\t\x12\x14\n\x0c\x61vatar_pants\x18\r \x01(\t\x12\x12\n\navatar_hat\x18\x0e \x01(\t\x12\x14\n\x0c\x61vatar_shoes\x18\x0f \x01(\t\x12\x13\n\x0b\x61vatar_eyes\x18\x10 \x01(\t\x12\x17\n\x0f\x61vatar_backpack\x18\x11 \x01(\t\x12\x15\n\ravatar_gloves\x18\x12 \x01(\t\x12\x14\n\x0c\x61vatar_socks\x18\x13 \x01(\tb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_gender__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PLAYERAVATAR = _descriptor.Descriptor(
  name='PlayerAvatar',
  full_name='pogoprotos.data.player.PlayerAvatar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='skin', full_name='pogoprotos.data.player.PlayerAvatar.skin', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hair', full_name='pogoprotos.data.player.PlayerAvatar.hair', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shirt', full_name='pogoprotos.data.player.PlayerAvatar.shirt', index=2,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pants', full_name='pogoprotos.data.player.PlayerAvatar.pants', index=3,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hat', full_name='pogoprotos.data.player.PlayerAvatar.hat', index=4,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shoes', full_name='pogoprotos.data.player.PlayerAvatar.shoes', index=5,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gender', full_name='pogoprotos.data.player.PlayerAvatar.gender', index=6,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eyes', full_name='pogoprotos.data.player.PlayerAvatar.eyes', index=7,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backpack', full_name='pogoprotos.data.player.PlayerAvatar.backpack', index=8,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar_hair', full_name='pogoprotos.data.player.PlayerAvatar.avatar_hair', index=9,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar_shirt', full_name='pogoprotos.data.player.PlayerAvatar.avatar_shirt', index=10,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar_pants', full_name='pogoprotos.data.player.PlayerAvatar.avatar_pants', index=11,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar_hat', full_name='pogoprotos.data.player.PlayerAvatar.avatar_hat', index=12,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar_shoes', full_name='pogoprotos.data.player.PlayerAvatar.avatar_shoes', index=13,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar_eyes', full_name='pogoprotos.data.player.PlayerAvatar.avatar_eyes', index=14,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar_backpack', full_name='pogoprotos.data.player.PlayerAvatar.avatar_backpack', index=15,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar_gloves', full_name='pogoprotos.data.player.PlayerAvatar.avatar_gloves', index=16,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar_socks', full_name='pogoprotos.data.player.PlayerAvatar.avatar_socks', index=17,
      number=19, type=9, cpp_type=9, label=1,
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
  serialized_start=102,
  serialized_end=474,
)

_PLAYERAVATAR.fields_by_name['gender'].enum_type = pogoprotos_dot_enums_dot_gender__pb2._GENDER
DESCRIPTOR.message_types_by_name['PlayerAvatar'] = _PLAYERAVATAR

PlayerAvatar = _reflection.GeneratedProtocolMessageType('PlayerAvatar', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERAVATAR,
  __module__ = 'pogoprotos.data.player.player_avatar_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.player.PlayerAvatar)
  ))
_sym_db.RegisterMessage(PlayerAvatar)


# @@protoc_insertion_point(module_scope)
