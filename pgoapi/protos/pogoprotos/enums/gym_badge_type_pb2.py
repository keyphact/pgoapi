# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/gym_badge_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/gym_badge_type.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_pb=_b('\n%pogoprotos/enums/gym_badge_type.proto\x12\x10pogoprotos.enums*z\n\x0cGymBadgeType\x12\x13\n\x0fGYM_BADGE_UNSET\x10\x00\x12\x15\n\x11GYM_BADGE_VANILLA\x10\x01\x12\x14\n\x10GYM_BADGE_BRONZE\x10\x02\x12\x14\n\x10GYM_BADGE_SILVER\x10\x03\x12\x12\n\x0eGYM_BADGE_GOLD\x10\x04\x62\x06proto3')
)

_GYMBADGETYPE = _descriptor.EnumDescriptor(
  name='GymBadgeType',
  full_name='pogoprotos.enums.GymBadgeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GYM_BADGE_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_BADGE_VANILLA', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_BADGE_BRONZE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_BADGE_SILVER', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_BADGE_GOLD', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=59,
  serialized_end=181,
)
_sym_db.RegisterEnumDescriptor(_GYMBADGETYPE)

GymBadgeType = enum_type_wrapper.EnumTypeWrapper(_GYMBADGETYPE)
GYM_BADGE_UNSET = 0
GYM_BADGE_VANILLA = 1
GYM_BADGE_BRONZE = 2
GYM_BADGE_SILVER = 3
GYM_BADGE_GOLD = 4


DESCRIPTOR.enum_types_by_name['GymBadgeType'] = _GYMBADGETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
