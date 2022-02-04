# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: foo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='foo.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\016UnixSocketDemo',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tfoo.proto\"\x1d\n\nFooRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1e\n\x0b\x46ooResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2*\n\x03\x46oo\x12#\n\x06GetFoo\x12\x0b.FooRequest\x1a\x0c.FooResponseB\x11\xaa\x02\x0eUnixSocketDemob\x06proto3'
)




_FOOREQUEST = _descriptor.Descriptor(
  name='FooRequest',
  full_name='FooRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='FooRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13,
  serialized_end=42,
)


_FOORESPONSE = _descriptor.Descriptor(
  name='FooResponse',
  full_name='FooResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='FooResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=74,
)

DESCRIPTOR.message_types_by_name['FooRequest'] = _FOOREQUEST
DESCRIPTOR.message_types_by_name['FooResponse'] = _FOORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FooRequest = _reflection.GeneratedProtocolMessageType('FooRequest', (_message.Message,), {
  'DESCRIPTOR' : _FOOREQUEST,
  '__module__' : 'foo_pb2'
  # @@protoc_insertion_point(class_scope:FooRequest)
  })
_sym_db.RegisterMessage(FooRequest)

FooResponse = _reflection.GeneratedProtocolMessageType('FooResponse', (_message.Message,), {
  'DESCRIPTOR' : _FOORESPONSE,
  '__module__' : 'foo_pb2'
  # @@protoc_insertion_point(class_scope:FooResponse)
  })
_sym_db.RegisterMessage(FooResponse)


DESCRIPTOR._options = None

_FOO = _descriptor.ServiceDescriptor(
  name='Foo',
  full_name='Foo',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=76,
  serialized_end=118,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFoo',
    full_name='Foo.GetFoo',
    index=0,
    containing_service=None,
    input_type=_FOOREQUEST,
    output_type=_FOORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FOO)

DESCRIPTOR.services_by_name['Foo'] = _FOO

# @@protoc_insertion_point(module_scope)
