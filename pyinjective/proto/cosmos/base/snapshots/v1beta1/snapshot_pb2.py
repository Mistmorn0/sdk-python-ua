# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/base/snapshots/v1beta1/snapshot.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,cosmos/base/snapshots/v1beta1/snapshot.proto\x12\x1d\x63osmos.base.snapshots.v1beta1\x1a\x14gogoproto/gogo.proto\"\x89\x01\n\x08Snapshot\x12\x0e\n\x06height\x18\x01 \x01(\x04\x12\x0e\n\x06\x66ormat\x18\x02 \x01(\r\x12\x0e\n\x06\x63hunks\x18\x03 \x01(\r\x12\x0c\n\x04hash\x18\x04 \x01(\x0c\x12?\n\x08metadata\x18\x05 \x01(\x0b\x32\'.cosmos.base.snapshots.v1beta1.MetadataB\x04\xc8\xde\x1f\x00\" \n\x08Metadata\x12\x14\n\x0c\x63hunk_hashes\x18\x01 \x03(\x0c\"\xc5\x02\n\x0cSnapshotItem\x12\x41\n\x05store\x18\x01 \x01(\x0b\x32\x30.cosmos.base.snapshots.v1beta1.SnapshotStoreItemH\x00\x12I\n\x04iavl\x18\x02 \x01(\x0b\x32/.cosmos.base.snapshots.v1beta1.SnapshotIAVLItemB\x08\xe2\xde\x1f\x04IAVLH\x00\x12I\n\textension\x18\x03 \x01(\x0b\x32\x34.cosmos.base.snapshots.v1beta1.SnapshotExtensionMetaH\x00\x12T\n\x11\x65xtension_payload\x18\x04 \x01(\x0b\x32\x37.cosmos.base.snapshots.v1beta1.SnapshotExtensionPayloadH\x00\x42\x06\n\x04item\"!\n\x11SnapshotStoreItem\x12\x0c\n\x04name\x18\x01 \x01(\t\"O\n\x10SnapshotIAVLItem\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x0f\n\x07version\x18\x03 \x01(\x03\x12\x0e\n\x06height\x18\x04 \x01(\x05\"5\n\x15SnapshotExtensionMeta\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x02 \x01(\r\"+\n\x18SnapshotExtensionPayload\x12\x0f\n\x07payload\x18\x01 \x01(\x0c\x42.Z,github.com/cosmos/cosmos-sdk/snapshots/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.base.snapshots.v1beta1.snapshot_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/snapshots/types'
  _SNAPSHOT.fields_by_name['metadata']._options = None
  _SNAPSHOT.fields_by_name['metadata']._serialized_options = b'\310\336\037\000'
  _SNAPSHOTITEM.fields_by_name['iavl']._options = None
  _SNAPSHOTITEM.fields_by_name['iavl']._serialized_options = b'\342\336\037\004IAVL'
  _SNAPSHOT._serialized_start=102
  _SNAPSHOT._serialized_end=239
  _METADATA._serialized_start=241
  _METADATA._serialized_end=273
  _SNAPSHOTITEM._serialized_start=276
  _SNAPSHOTITEM._serialized_end=601
  _SNAPSHOTSTOREITEM._serialized_start=603
  _SNAPSHOTSTOREITEM._serialized_end=636
  _SNAPSHOTIAVLITEM._serialized_start=638
  _SNAPSHOTIAVLITEM._serialized_end=717
  _SNAPSHOTEXTENSIONMETA._serialized_start=719
  _SNAPSHOTEXTENSIONMETA._serialized_end=772
  _SNAPSHOTEXTENSIONPAYLOAD._serialized_start=774
  _SNAPSHOTEXTENSIONPAYLOAD._serialized_end=817
# @@protoc_insertion_point(module_scope)
