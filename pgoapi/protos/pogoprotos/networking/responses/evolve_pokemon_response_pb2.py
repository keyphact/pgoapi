# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/evolve_pokemon_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data import pokemon_data_pb2 as pogoprotos_dot_data_dot_pokemon__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/evolve_pokemon_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\n=pogoprotos/networking/responses/evolve_pokemon_response.proto\x12\x1fpogoprotos.networking.responses\x1a\"pogoprotos/data/pokemon_data.proto\"\x9e\x03\n\x15\x45volvePokemonResponse\x12M\n\x06result\x18\x01 \x01(\x0e\x32=.pogoprotos.networking.responses.EvolvePokemonResponse.Result\x12:\n\x14\x65volved_pokemon_data\x18\x02 \x01(\x0b\x32\x1c.pogoprotos.data.PokemonData\x12\x1a\n\x12\x65xperience_awarded\x18\x03 \x01(\x05\x12\x15\n\rcandy_awarded\x18\x04 \x01(\x05\"\xc6\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1a\n\x16\x46\x41ILED_POKEMON_MISSING\x10\x02\x12!\n\x1d\x46\x41ILED_INSUFFICIENT_RESOURCES\x10\x03\x12 \n\x1c\x46\x41ILED_POKEMON_CANNOT_EVOLVE\x10\x04\x12\x1e\n\x1a\x46\x41ILED_POKEMON_IS_DEPLOYED\x10\x05\x12#\n\x1f\x46\x41ILED_INVALID_ITEM_REQUIREMENT\x10\x06\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_pokemon__data__pb2.DESCRIPTOR,])



_EVOLVEPOKEMONRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.EvolvePokemonResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED_POKEMON_MISSING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED_INSUFFICIENT_RESOURCES', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED_POKEMON_CANNOT_EVOLVE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED_POKEMON_IS_DEPLOYED', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED_INVALID_ITEM_REQUIREMENT', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=351,
  serialized_end=549,
)
_sym_db.RegisterEnumDescriptor(_EVOLVEPOKEMONRESPONSE_RESULT)


_EVOLVEPOKEMONRESPONSE = _descriptor.Descriptor(
  name='EvolvePokemonResponse',
  full_name='pogoprotos.networking.responses.EvolvePokemonResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.EvolvePokemonResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evolved_pokemon_data', full_name='pogoprotos.networking.responses.EvolvePokemonResponse.evolved_pokemon_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='experience_awarded', full_name='pogoprotos.networking.responses.EvolvePokemonResponse.experience_awarded', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='candy_awarded', full_name='pogoprotos.networking.responses.EvolvePokemonResponse.candy_awarded', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EVOLVEPOKEMONRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=549,
)

_EVOLVEPOKEMONRESPONSE.fields_by_name['result'].enum_type = _EVOLVEPOKEMONRESPONSE_RESULT
_EVOLVEPOKEMONRESPONSE.fields_by_name['evolved_pokemon_data'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
_EVOLVEPOKEMONRESPONSE_RESULT.containing_type = _EVOLVEPOKEMONRESPONSE
DESCRIPTOR.message_types_by_name['EvolvePokemonResponse'] = _EVOLVEPOKEMONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EvolvePokemonResponse = _reflection.GeneratedProtocolMessageType('EvolvePokemonResponse', (_message.Message,), dict(
  DESCRIPTOR = _EVOLVEPOKEMONRESPONSE,
  __module__ = 'pogoprotos.networking.responses.evolve_pokemon_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.EvolvePokemonResponse)
  ))
_sym_db.RegisterMessage(EvolvePokemonResponse)


# @@protoc_insertion_point(module_scope)
