# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/responses/get_store_items_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.player import currency_pb2 as pogoprotos_dot_data_dot_player_dot_currency__pb2
from pogoprotos.inventory.item import item_data_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/platform/responses/get_store_items_response.proto',
  package='pogoprotos.networking.platform.responses',
  syntax='proto3',
  serialized_pb=_b('\nGpogoprotos/networking/platform/responses/get_store_items_response.proto\x12(pogoprotos.networking.platform.responses\x1a%pogoprotos/data/player/currency.proto\x1a)pogoprotos/inventory/item/item_data.proto\"\xbc\x05\n\x15GetStoreItemsResponse\x12V\n\x06status\x18\x01 \x01(\x0e\x32\x46.pogoprotos.networking.platform.responses.GetStoreItemsResponse.Status\x12X\n\x05items\x18\x02 \x03(\x0b\x32I.pogoprotos.networking.platform.responses.GetStoreItemsResponse.StoreItem\x12;\n\x11player_currencies\x18\x03 \x03(\x0b\x32 .pogoprotos.data.player.Currency\x12\x10\n\x08unknown4\x18\x04 \x01(\t\x1a\xfe\x02\n\tStoreItem\x12\x0f\n\x07item_id\x18\x01 \x01(\t\x12\x0e\n\x06is_iap\x18\x02 \x01(\x08\x12\x39\n\x0f\x63urrency_to_buy\x18\x03 \x01(\x0b\x32 .pogoprotos.data.player.Currency\x12\x39\n\x0fyields_currency\x18\x04 \x01(\x0b\x32 .pogoprotos.data.player.Currency\x12\x38\n\x0byields_item\x18\x05 \x01(\x0b\x32#.pogoprotos.inventory.item.ItemData\x12\x61\n\x04tags\x18\x06 \x03(\x0b\x32S.pogoprotos.networking.platform.responses.GetStoreItemsResponse.StoreItem.TagsEntry\x12\x10\n\x08unknown7\x18\x07 \x01(\x05\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"!\n\x06Status\x12\r\n\tUNDEFINED\x10\x00\x12\x08\n\x04OKAY\x10\x01\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_player_dot_currency__pb2.DESCRIPTOR,pogoprotos_dot_inventory_dot_item_dot_item__data__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GETSTOREITEMSRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.platform.responses.GetStoreItemsResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OKAY', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=867,
  serialized_end=900,
)
_sym_db.RegisterEnumDescriptor(_GETSTOREITEMSRESPONSE_STATUS)


_GETSTOREITEMSRESPONSE_STOREITEM_TAGSENTRY = _descriptor.Descriptor(
  name='TagsEntry',
  full_name='pogoprotos.networking.platform.responses.GetStoreItemsResponse.StoreItem.TagsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='pogoprotos.networking.platform.responses.GetStoreItemsResponse.StoreItem.TagsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='pogoprotos.networking.platform.responses.GetStoreItemsResponse.StoreItem.TagsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=822,
  serialized_end=865,
)

_GETSTOREITEMSRESPONSE_STOREITEM = _descriptor.Descriptor(
  name='StoreItem',
  full_name='pogoprotos.networking.platform.responses.GetStoreItemsResponse.StoreItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='pogoprotos.networking.platform.responses.GetStoreItemsResponse.StoreItem.item_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_iap', full_name='pogoprotos.networking.platform.responses.GetStoreItemsResponse.StoreItem.is_iap', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currency_to_buy', full_name='pogoprotos.networking.platform.responses.GetStoreItemsResponse.StoreItem.currency_to_buy', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='yields_currency', full_name='pogoprotos.networking.platform.responses.GetStoreItemsResponse.StoreItem.yields_currency', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='yields_item', full_name='pogoprotos.networking.platform.responses.GetStoreItemsResponse.StoreItem.yields_item', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tags', full_name='pogoprotos.networking.platform.responses.GetStoreItemsResponse.StoreItem.tags', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown7', full_name='pogoprotos.networking.platform.responses.GetStoreItemsResponse.StoreItem.unknown7', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GETSTOREITEMSRESPONSE_STOREITEM_TAGSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=483,
  serialized_end=865,
)

_GETSTOREITEMSRESPONSE = _descriptor.Descriptor(
  name='GetStoreItemsResponse',
  full_name='pogoprotos.networking.platform.responses.GetStoreItemsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.platform.responses.GetStoreItemsResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='items', full_name='pogoprotos.networking.platform.responses.GetStoreItemsResponse.items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_currencies', full_name='pogoprotos.networking.platform.responses.GetStoreItemsResponse.player_currencies', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown4', full_name='pogoprotos.networking.platform.responses.GetStoreItemsResponse.unknown4', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GETSTOREITEMSRESPONSE_STOREITEM, ],
  enum_types=[
    _GETSTOREITEMSRESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=200,
  serialized_end=900,
)

_GETSTOREITEMSRESPONSE_STOREITEM_TAGSENTRY.containing_type = _GETSTOREITEMSRESPONSE_STOREITEM
_GETSTOREITEMSRESPONSE_STOREITEM.fields_by_name['currency_to_buy'].message_type = pogoprotos_dot_data_dot_player_dot_currency__pb2._CURRENCY
_GETSTOREITEMSRESPONSE_STOREITEM.fields_by_name['yields_currency'].message_type = pogoprotos_dot_data_dot_player_dot_currency__pb2._CURRENCY
_GETSTOREITEMSRESPONSE_STOREITEM.fields_by_name['yields_item'].message_type = pogoprotos_dot_inventory_dot_item_dot_item__data__pb2._ITEMDATA
_GETSTOREITEMSRESPONSE_STOREITEM.fields_by_name['tags'].message_type = _GETSTOREITEMSRESPONSE_STOREITEM_TAGSENTRY
_GETSTOREITEMSRESPONSE_STOREITEM.containing_type = _GETSTOREITEMSRESPONSE
_GETSTOREITEMSRESPONSE.fields_by_name['status'].enum_type = _GETSTOREITEMSRESPONSE_STATUS
_GETSTOREITEMSRESPONSE.fields_by_name['items'].message_type = _GETSTOREITEMSRESPONSE_STOREITEM
_GETSTOREITEMSRESPONSE.fields_by_name['player_currencies'].message_type = pogoprotos_dot_data_dot_player_dot_currency__pb2._CURRENCY
_GETSTOREITEMSRESPONSE_STATUS.containing_type = _GETSTOREITEMSRESPONSE
DESCRIPTOR.message_types_by_name['GetStoreItemsResponse'] = _GETSTOREITEMSRESPONSE

GetStoreItemsResponse = _reflection.GeneratedProtocolMessageType('GetStoreItemsResponse', (_message.Message,), dict(

  StoreItem = _reflection.GeneratedProtocolMessageType('StoreItem', (_message.Message,), dict(

    TagsEntry = _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), dict(
      DESCRIPTOR = _GETSTOREITEMSRESPONSE_STOREITEM_TAGSENTRY,
      __module__ = 'pogoprotos.networking.platform.responses.get_store_items_response_pb2'
      # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.responses.GetStoreItemsResponse.StoreItem.TagsEntry)
      ))
    ,
    DESCRIPTOR = _GETSTOREITEMSRESPONSE_STOREITEM,
    __module__ = 'pogoprotos.networking.platform.responses.get_store_items_response_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.responses.GetStoreItemsResponse.StoreItem)
    ))
  ,
  DESCRIPTOR = _GETSTOREITEMSRESPONSE,
  __module__ = 'pogoprotos.networking.platform.responses.get_store_items_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.responses.GetStoreItemsResponse)
  ))
_sym_db.RegisterMessage(GetStoreItemsResponse)
_sym_db.RegisterMessage(GetStoreItemsResponse.StoreItem)
_sym_db.RegisterMessage(GetStoreItemsResponse.StoreItem.TagsEntry)


_GETSTOREITEMSRESPONSE_STOREITEM_TAGSENTRY.has_options = True
_GETSTOREITEMSRESPONSE_STOREITEM_TAGSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
