# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/inventory/item/item_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory.item import item_id_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/inventory/item/item_data.proto',
  package='pogoprotos.inventory.item',
  syntax='proto3',
  serialized_pb=_b('\n)pogoprotos/inventory/item/item_data.proto\x12\x19pogoprotos.inventory.item\x1a\'pogoprotos/inventory/item/item_id.proto\"]\n\x08ItemData\x12\x32\n\x07item_id\x18\x01 \x01(\x0e\x32!.pogoprotos.inventory.item.ItemId\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\x0e\n\x06unseen\x18\x03 \x01(\x08\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_item_dot_item__id__pb2.DESCRIPTOR,])




_ITEMDATA = _descriptor.Descriptor(
  name='ItemData',
  full_name='pogoprotos.inventory.item.ItemData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='pogoprotos.inventory.item.ItemData.item_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='pogoprotos.inventory.item.ItemData.count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unseen', full_name='pogoprotos.inventory.item.ItemData.unseen', index=2,
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
  serialized_start=113,
  serialized_end=206,
)

_ITEMDATA.fields_by_name['item_id'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__id__pb2._ITEMID
DESCRIPTOR.message_types_by_name['ItemData'] = _ITEMDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ItemData = _reflection.GeneratedProtocolMessageType('ItemData', (_message.Message,), dict(
  DESCRIPTOR = _ITEMDATA,
  __module__ = 'pogoprotos.inventory.item.item_data_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.inventory.item.ItemData)
  ))
_sym_db.RegisterMessage(ItemData)


# @@protoc_insertion_point(module_scope)
