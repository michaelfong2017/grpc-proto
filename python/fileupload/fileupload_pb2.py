# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fileupload.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fileupload.proto',
  package='fileupload',
  syntax='proto3',
  serialized_options=b'\n\026com.michael.fileuploadP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x66ileupload.proto\x12\nfileupload\"&\n\x08MetaData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\"\x17\n\x04\x46ile\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\"j\n\x11\x46ileUploadRequest\x12(\n\x08metadata\x18\x01 \x01(\x0b\x32\x14.fileupload.MetaDataH\x00\x12 \n\x04\x66ile\x18\x02 \x01(\x0b\x32\x10.fileupload.FileH\x00\x42\t\n\x07request\"F\n\x12\x46ileUploadResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\"\n\x06status\x18\x02 \x01(\x0e\x32\x12.fileupload.Status*?\n\x06Status\x12\x0b\n\x07PENDING\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\x0b\n\x07SUCCESS\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x03\x32X\n\x0b\x46ileService\x12I\n\x06upload\x12\x1d.fileupload.FileUploadRequest\x1a\x1e.fileupload.FileUploadResponse(\x01\x42\x1a\n\x16\x63om.michael.fileuploadP\x01\x62\x06proto3'
)

_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='fileupload.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IN_PROGRESS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=277,
  serialized_end=340,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
PENDING = 0
IN_PROGRESS = 1
SUCCESS = 2
FAILED = 3



_METADATA = _descriptor.Descriptor(
  name='MetaData',
  full_name='fileupload.MetaData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='fileupload.MetaData.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='fileupload.MetaData.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=32,
  serialized_end=70,
)


_FILE = _descriptor.Descriptor(
  name='File',
  full_name='fileupload.File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='fileupload.File.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=72,
  serialized_end=95,
)


_FILEUPLOADREQUEST = _descriptor.Descriptor(
  name='FileUploadRequest',
  full_name='fileupload.FileUploadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='fileupload.FileUploadRequest.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file', full_name='fileupload.FileUploadRequest.file', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='request', full_name='fileupload.FileUploadRequest.request',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=97,
  serialized_end=203,
)


_FILEUPLOADRESPONSE = _descriptor.Descriptor(
  name='FileUploadResponse',
  full_name='fileupload.FileUploadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='fileupload.FileUploadResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='fileupload.FileUploadResponse.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=205,
  serialized_end=275,
)

_FILEUPLOADREQUEST.fields_by_name['metadata'].message_type = _METADATA
_FILEUPLOADREQUEST.fields_by_name['file'].message_type = _FILE
_FILEUPLOADREQUEST.oneofs_by_name['request'].fields.append(
  _FILEUPLOADREQUEST.fields_by_name['metadata'])
_FILEUPLOADREQUEST.fields_by_name['metadata'].containing_oneof = _FILEUPLOADREQUEST.oneofs_by_name['request']
_FILEUPLOADREQUEST.oneofs_by_name['request'].fields.append(
  _FILEUPLOADREQUEST.fields_by_name['file'])
_FILEUPLOADREQUEST.fields_by_name['file'].containing_oneof = _FILEUPLOADREQUEST.oneofs_by_name['request']
_FILEUPLOADRESPONSE.fields_by_name['status'].enum_type = _STATUS
DESCRIPTOR.message_types_by_name['MetaData'] = _METADATA
DESCRIPTOR.message_types_by_name['File'] = _FILE
DESCRIPTOR.message_types_by_name['FileUploadRequest'] = _FILEUPLOADREQUEST
DESCRIPTOR.message_types_by_name['FileUploadResponse'] = _FILEUPLOADRESPONSE
DESCRIPTOR.enum_types_by_name['Status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MetaData = _reflection.GeneratedProtocolMessageType('MetaData', (_message.Message,), {
  'DESCRIPTOR' : _METADATA,
  '__module__' : 'fileupload_pb2'
  # @@protoc_insertion_point(class_scope:fileupload.MetaData)
  })
_sym_db.RegisterMessage(MetaData)

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), {
  'DESCRIPTOR' : _FILE,
  '__module__' : 'fileupload_pb2'
  # @@protoc_insertion_point(class_scope:fileupload.File)
  })
_sym_db.RegisterMessage(File)

FileUploadRequest = _reflection.GeneratedProtocolMessageType('FileUploadRequest', (_message.Message,), {
  'DESCRIPTOR' : _FILEUPLOADREQUEST,
  '__module__' : 'fileupload_pb2'
  # @@protoc_insertion_point(class_scope:fileupload.FileUploadRequest)
  })
_sym_db.RegisterMessage(FileUploadRequest)

FileUploadResponse = _reflection.GeneratedProtocolMessageType('FileUploadResponse', (_message.Message,), {
  'DESCRIPTOR' : _FILEUPLOADRESPONSE,
  '__module__' : 'fileupload_pb2'
  # @@protoc_insertion_point(class_scope:fileupload.FileUploadResponse)
  })
_sym_db.RegisterMessage(FileUploadResponse)


DESCRIPTOR._options = None

_FILESERVICE = _descriptor.ServiceDescriptor(
  name='FileService',
  full_name='fileupload.FileService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=342,
  serialized_end=430,
  methods=[
  _descriptor.MethodDescriptor(
    name='upload',
    full_name='fileupload.FileService.upload',
    index=0,
    containing_service=None,
    input_type=_FILEUPLOADREQUEST,
    output_type=_FILEUPLOADRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FILESERVICE)

DESCRIPTOR.services_by_name['FileService'] = _FILESERVICE

# @@protoc_insertion_point(module_scope)
