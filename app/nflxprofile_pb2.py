# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nflxprofile.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='nflxprofile.proto',
  package='nflxprofile',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x11nflxprofile.proto\x12\x0bnflxprofile\"\xf7\x03\n\x07Profile\x12\x12\n\nstart_time\x18\x01 \x02(\x01\x12\x10\n\x08\x65nd_time\x18\x02 \x02(\x01\x12\x13\n\x07samples\x18\x03 \x03(\rB\x02\x10\x01\x12\x17\n\x0btime_deltas\x18\x04 \x03(\x01\x42\x02\x10\x01\x12.\n\x05nodes\x18\x05 \x03(\x0b\x32\x1f.nflxprofile.Profile.NodesEntry\x12\r\n\x05title\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\x12\x30\n\x06params\x18\x08 \x03(\x0b\x32 .nflxprofile.Profile.ParamsEntry\x1a\x99\x01\n\x04Node\x12\x15\n\rfunction_name\x18\x01 \x02(\t\x12\x11\n\thit_count\x18\x02 \x02(\r\x12\x10\n\x08\x63hildren\x18\x03 \x03(\r\x12\x0f\n\x07libtype\x18\x04 \x01(\t\x12\x0e\n\x06parent\x18\x05 \x01(\r\x12\x0b\n\x03pid\x18\x06 \x01(\r\x12\x0b\n\x03tid\x18\x07 \x01(\r\x12\x0b\n\x03\x63pu\x18\x08 \x01(\r\x12\r\n\x05value\x18\t \x01(\x04\x1aG\n\nNodesEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.nflxprofile.Profile.Node:\x02\x38\x01\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01')
)




_PROFILE_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='nflxprofile.Profile.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='function_name', full_name='nflxprofile.Profile.Node.function_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hit_count', full_name='nflxprofile.Profile.Node.hit_count', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='children', full_name='nflxprofile.Profile.Node.children', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='libtype', full_name='nflxprofile.Profile.Node.libtype', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent', full_name='nflxprofile.Profile.Node.parent', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pid', full_name='nflxprofile.Profile.Node.pid', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tid', full_name='nflxprofile.Profile.Node.tid', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpu', full_name='nflxprofile.Profile.Node.cpu', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='nflxprofile.Profile.Node.value', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=265,
  serialized_end=418,
)

_PROFILE_NODESENTRY = _descriptor.Descriptor(
  name='NodesEntry',
  full_name='nflxprofile.Profile.NodesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='nflxprofile.Profile.NodesEntry.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='nflxprofile.Profile.NodesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=420,
  serialized_end=491,
)

_PROFILE_PARAMSENTRY = _descriptor.Descriptor(
  name='ParamsEntry',
  full_name='nflxprofile.Profile.ParamsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='nflxprofile.Profile.ParamsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='nflxprofile.Profile.ParamsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=493,
  serialized_end=538,
)

_PROFILE = _descriptor.Descriptor(
  name='Profile',
  full_name='nflxprofile.Profile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='nflxprofile.Profile.start_time', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='nflxprofile.Profile.end_time', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='samples', full_name='nflxprofile.Profile.samples', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_deltas', full_name='nflxprofile.Profile.time_deltas', index=3,
      number=4, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodes', full_name='nflxprofile.Profile.nodes', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='nflxprofile.Profile.title', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='nflxprofile.Profile.description', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='params', full_name='nflxprofile.Profile.params', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PROFILE_NODE, _PROFILE_NODESENTRY, _PROFILE_PARAMSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=538,
)

_PROFILE_NODE.containing_type = _PROFILE
_PROFILE_NODESENTRY.fields_by_name['value'].message_type = _PROFILE_NODE
_PROFILE_NODESENTRY.containing_type = _PROFILE
_PROFILE_PARAMSENTRY.containing_type = _PROFILE
_PROFILE.fields_by_name['nodes'].message_type = _PROFILE_NODESENTRY
_PROFILE.fields_by_name['params'].message_type = _PROFILE_PARAMSENTRY
DESCRIPTOR.message_types_by_name['Profile'] = _PROFILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Profile = _reflection.GeneratedProtocolMessageType('Profile', (_message.Message,), dict(

  Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), dict(
    DESCRIPTOR = _PROFILE_NODE,
    __module__ = 'nflxprofile_pb2'
    # @@protoc_insertion_point(class_scope:nflxprofile.Profile.Node)
    ))
  ,

  NodesEntry = _reflection.GeneratedProtocolMessageType('NodesEntry', (_message.Message,), dict(
    DESCRIPTOR = _PROFILE_NODESENTRY,
    __module__ = 'nflxprofile_pb2'
    # @@protoc_insertion_point(class_scope:nflxprofile.Profile.NodesEntry)
    ))
  ,

  ParamsEntry = _reflection.GeneratedProtocolMessageType('ParamsEntry', (_message.Message,), dict(
    DESCRIPTOR = _PROFILE_PARAMSENTRY,
    __module__ = 'nflxprofile_pb2'
    # @@protoc_insertion_point(class_scope:nflxprofile.Profile.ParamsEntry)
    ))
  ,
  DESCRIPTOR = _PROFILE,
  __module__ = 'nflxprofile_pb2'
  # @@protoc_insertion_point(class_scope:nflxprofile.Profile)
  ))
_sym_db.RegisterMessage(Profile)
_sym_db.RegisterMessage(Profile.Node)
_sym_db.RegisterMessage(Profile.NodesEntry)
_sym_db.RegisterMessage(Profile.ParamsEntry)


_PROFILE_NODESENTRY._options = None
_PROFILE_PARAMSENTRY._options = None
_PROFILE.fields_by_name['samples']._options = None
_PROFILE.fields_by_name['time_deltas']._options = None
# @@protoc_insertion_point(module_scope)
