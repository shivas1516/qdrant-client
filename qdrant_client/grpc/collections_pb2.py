# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: collections.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x63ollections.proto\x12\x06qdrant\"@\n\x0cVectorParams\x12\x0c\n\x04size\x18\x01 \x01(\x04\x12\"\n\x08\x64istance\x18\x02 \x01(\x0e\x32\x10.qdrant.Distance\"\x82\x01\n\x0fVectorParamsMap\x12-\n\x03map\x18\x01 \x03(\x0b\x32 .qdrant.VectorParamsMap.MapEntry\x1a@\n\x08MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.qdrant.VectorParams:\x02\x38\x01\"p\n\rVectorsConfig\x12&\n\x06params\x18\x01 \x01(\x0b\x32\x14.qdrant.VectorParamsH\x00\x12-\n\nparams_map\x18\x02 \x01(\x0b\x32\x17.qdrant.VectorParamsMapH\x00\x42\x08\n\x06\x63onfig\"3\n\x18GetCollectionInfoRequest\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\"\x18\n\x16ListCollectionsRequest\"%\n\x15\x43ollectionDescription\x12\x0c\n\x04name\x18\x01 \x01(\t\"Q\n\x19GetCollectionInfoResponse\x12&\n\x06result\x18\x01 \x01(\x0b\x32\x16.qdrant.CollectionInfo\x12\x0c\n\x04time\x18\x02 \x01(\x01\"[\n\x17ListCollectionsResponse\x12\x32\n\x0b\x63ollections\x18\x01 \x03(\x0b\x32\x1d.qdrant.CollectionDescription\x12\x0c\n\x04time\x18\x02 \x01(\x01\",\n\x0fOptimizerStatus\x12\n\n\x02ok\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"\xc8\x01\n\x0eHnswConfigDiff\x12\x0e\n\x01m\x18\x01 \x01(\x04H\x00\x88\x01\x01\x12\x19\n\x0c\x65\x66_construct\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12 \n\x13\x66ull_scan_threshold\x18\x03 \x01(\x04H\x02\x88\x01\x01\x12!\n\x14max_indexing_threads\x18\x04 \x01(\x04H\x03\x88\x01\x01\x42\x04\n\x02_mB\x0f\n\r_ef_constructB\x16\n\x14_full_scan_thresholdB\x17\n\x15_max_indexing_threads\"y\n\rWalConfigDiff\x12\x1c\n\x0fwal_capacity_mb\x18\x01 \x01(\x04H\x00\x88\x01\x01\x12\x1f\n\x12wal_segments_ahead\x18\x02 \x01(\x04H\x01\x88\x01\x01\x42\x12\n\x10_wal_capacity_mbB\x15\n\x13_wal_segments_ahead\"\xec\x03\n\x14OptimizersConfigDiff\x12\x1e\n\x11\x64\x65leted_threshold\x18\x01 \x01(\x01H\x00\x88\x01\x01\x12%\n\x18vacuum_min_vector_number\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12#\n\x16\x64\x65\x66\x61ult_segment_number\x18\x03 \x01(\x04H\x02\x88\x01\x01\x12\x1d\n\x10max_segment_size\x18\x04 \x01(\x04H\x03\x88\x01\x01\x12\x1d\n\x10memmap_threshold\x18\x05 \x01(\x04H\x04\x88\x01\x01\x12\x1f\n\x12indexing_threshold\x18\x06 \x01(\x04H\x05\x88\x01\x01\x12\x1f\n\x12\x66lush_interval_sec\x18\x07 \x01(\x04H\x06\x88\x01\x01\x12%\n\x18max_optimization_threads\x18\x08 \x01(\x04H\x07\x88\x01\x01\x42\x14\n\x12_deleted_thresholdB\x1b\n\x19_vacuum_min_vector_numberB\x19\n\x17_default_segment_numberB\x13\n\x11_max_segment_sizeB\x13\n\x11_memmap_thresholdB\x15\n\x13_indexing_thresholdB\x15\n\x13_flush_interval_secB\x1b\n\x19_max_optimization_threads\"\xcf\x04\n\x10\x43reateCollection\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x30\n\x0bhnsw_config\x18\x04 \x01(\x0b\x32\x16.qdrant.HnswConfigDiffH\x00\x88\x01\x01\x12.\n\nwal_config\x18\x05 \x01(\x0b\x32\x15.qdrant.WalConfigDiffH\x01\x88\x01\x01\x12<\n\x11optimizers_config\x18\x06 \x01(\x0b\x32\x1c.qdrant.OptimizersConfigDiffH\x02\x88\x01\x01\x12\x19\n\x0cshard_number\x18\x07 \x01(\rH\x03\x88\x01\x01\x12\x1c\n\x0fon_disk_payload\x18\x08 \x01(\x08H\x04\x88\x01\x01\x12\x14\n\x07timeout\x18\t \x01(\x04H\x05\x88\x01\x01\x12\x32\n\x0evectors_config\x18\n \x01(\x0b\x32\x15.qdrant.VectorsConfigH\x06\x88\x01\x01\x12\x1f\n\x12replication_factor\x18\x0b \x01(\rH\x07\x88\x01\x01\x12%\n\x18write_consistency_factor\x18\x0c \x01(\rH\x08\x88\x01\x01\x42\x0e\n\x0c_hnsw_configB\r\n\x0b_wal_configB\x14\n\x12_optimizers_configB\x0f\n\r_shard_numberB\x12\n\x10_on_disk_payloadB\n\n\x08_timeoutB\x11\n\x0f_vectors_configB\x15\n\x13_replication_factorB\x1b\n\x19_write_consistency_factorJ\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04\"\xdf\x01\n\x10UpdateCollection\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12<\n\x11optimizers_config\x18\x02 \x01(\x0b\x32\x1c.qdrant.OptimizersConfigDiffH\x00\x88\x01\x01\x12\x14\n\x07timeout\x18\x03 \x01(\x04H\x01\x88\x01\x01\x12\x31\n\x06params\x18\x04 \x01(\x0b\x32\x1c.qdrant.CollectionParamsDiffH\x02\x88\x01\x01\x42\x14\n\x12_optimizers_configB\n\n\x08_timeoutB\t\n\x07_params\"M\n\x10\x44\x65leteCollection\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x14\n\x07timeout\x18\x02 \x01(\x04H\x00\x88\x01\x01\x42\n\n\x08_timeout\";\n\x1b\x43ollectionOperationResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x0c\n\x04time\x18\x02 \x01(\x01\"\x90\x02\n\x10\x43ollectionParams\x12\x14\n\x0cshard_number\x18\x03 \x01(\r\x12\x17\n\x0fon_disk_payload\x18\x04 \x01(\x08\x12\x32\n\x0evectors_config\x18\x05 \x01(\x0b\x32\x15.qdrant.VectorsConfigH\x00\x88\x01\x01\x12\x1f\n\x12replication_factor\x18\x06 \x01(\rH\x01\x88\x01\x01\x12%\n\x18write_consistency_factor\x18\x07 \x01(\rH\x02\x88\x01\x01\x42\x11\n\x0f_vectors_configB\x15\n\x13_replication_factorB\x1b\n\x19_write_consistency_factorJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03\"\x92\x01\n\x14\x43ollectionParamsDiff\x12\x1f\n\x12replication_factor\x18\x01 \x01(\rH\x00\x88\x01\x01\x12%\n\x18write_consistency_factor\x18\x02 \x01(\rH\x01\x88\x01\x01\x42\x15\n\x13_replication_factorB\x1b\n\x19_write_consistency_factor\"\xcc\x01\n\x10\x43ollectionConfig\x12(\n\x06params\x18\x01 \x01(\x0b\x32\x18.qdrant.CollectionParams\x12+\n\x0bhnsw_config\x18\x02 \x01(\x0b\x32\x16.qdrant.HnswConfigDiff\x12\x36\n\x10optimizer_config\x18\x03 \x01(\x0b\x32\x1c.qdrant.OptimizersConfigDiff\x12)\n\nwal_config\x18\x04 \x01(\x0b\x32\x15.qdrant.WalConfigDiff\"\xbd\x01\n\x0fTextIndexParams\x12(\n\ttokenizer\x18\x01 \x01(\x0e\x32\x15.qdrant.TokenizerType\x12\x16\n\tlowercase\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12\x1a\n\rmin_token_len\x18\x03 \x01(\x04H\x01\x88\x01\x01\x12\x1a\n\rmax_token_len\x18\x04 \x01(\x04H\x02\x88\x01\x01\x42\x0c\n\n_lowercaseB\x10\n\x0e_min_token_lenB\x10\n\x0e_max_token_len\"Z\n\x12PayloadIndexParams\x12\x34\n\x11text_index_params\x18\x01 \x01(\x0b\x32\x17.qdrant.TextIndexParamsH\x00\x42\x0e\n\x0cindex_params\"\x9d\x01\n\x11PayloadSchemaInfo\x12,\n\tdata_type\x18\x01 \x01(\x0e\x32\x19.qdrant.PayloadSchemaType\x12/\n\x06params\x18\x02 \x01(\x0b\x32\x1a.qdrant.PayloadIndexParamsH\x00\x88\x01\x01\x12\x13\n\x06points\x18\x03 \x01(\x04H\x01\x88\x01\x01\x42\t\n\x07_paramsB\t\n\x07_points\"\xba\x03\n\x0e\x43ollectionInfo\x12(\n\x06status\x18\x01 \x01(\x0e\x32\x18.qdrant.CollectionStatus\x12\x31\n\x10optimizer_status\x18\x02 \x01(\x0b\x32\x17.qdrant.OptimizerStatus\x12\x15\n\rvectors_count\x18\x03 \x01(\x04\x12\x16\n\x0esegments_count\x18\x04 \x01(\x04\x12(\n\x06\x63onfig\x18\x07 \x01(\x0b\x32\x18.qdrant.CollectionConfig\x12\x41\n\x0epayload_schema\x18\x08 \x03(\x0b\x32).qdrant.CollectionInfo.PayloadSchemaEntry\x12\x14\n\x0cpoints_count\x18\t \x01(\x04\x12\"\n\x15indexed_vectors_count\x18\n \x01(\x04H\x00\x88\x01\x01\x1aO\n\x12PayloadSchemaEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.qdrant.PayloadSchemaInfo:\x02\x38\x01\x42\x18\n\x16_indexed_vectors_countJ\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07\"[\n\rChangeAliases\x12(\n\x07\x61\x63tions\x18\x01 \x03(\x0b\x32\x17.qdrant.AliasOperations\x12\x14\n\x07timeout\x18\x02 \x01(\x04H\x00\x88\x01\x01\x42\n\n\x08_timeout\"\xa2\x01\n\x0f\x41liasOperations\x12+\n\x0c\x63reate_alias\x18\x01 \x01(\x0b\x32\x13.qdrant.CreateAliasH\x00\x12+\n\x0crename_alias\x18\x02 \x01(\x0b\x32\x13.qdrant.RenameAliasH\x00\x12+\n\x0c\x64\x65lete_alias\x18\x03 \x01(\x0b\x32\x13.qdrant.DeleteAliasH\x00\x42\x08\n\x06\x61\x63tion\":\n\x0b\x43reateAlias\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x12\n\nalias_name\x18\x02 \x01(\t\"=\n\x0bRenameAlias\x12\x16\n\x0eold_alias_name\x18\x01 \x01(\t\x12\x16\n\x0enew_alias_name\x18\x02 \x01(\t\"!\n\x0b\x44\x65leteAlias\x12\x12\n\nalias_name\x18\x01 \x01(\t*@\n\x08\x44istance\x12\x13\n\x0fUnknownDistance\x10\x00\x12\n\n\x06\x43osine\x10\x01\x12\n\n\x06\x45uclid\x10\x02\x12\x07\n\x03\x44ot\x10\x03*O\n\x10\x43ollectionStatus\x12\x1b\n\x17UnknownCollectionStatus\x10\x00\x12\t\n\x05Green\x10\x01\x12\n\n\x06Yellow\x10\x02\x12\x07\n\x03Red\x10\x03*\\\n\x11PayloadSchemaType\x12\x0f\n\x0bUnknownType\x10\x00\x12\x0b\n\x07Keyword\x10\x01\x12\x0b\n\x07Integer\x10\x02\x12\t\n\x05\x46loat\x10\x03\x12\x07\n\x03Geo\x10\x04\x12\x08\n\x04Text\x10\x05*B\n\rTokenizerType\x12\x0b\n\x07Unknown\x10\x00\x12\n\n\x06Prefix\x10\x01\x12\x0e\n\nWhitespace\x10\x02\x12\x08\n\x04Word\x10\x03\x62\x06proto3')

_DISTANCE = DESCRIPTOR.enum_types_by_name['Distance']
Distance = enum_type_wrapper.EnumTypeWrapper(_DISTANCE)
_COLLECTIONSTATUS = DESCRIPTOR.enum_types_by_name['CollectionStatus']
CollectionStatus = enum_type_wrapper.EnumTypeWrapper(_COLLECTIONSTATUS)
_PAYLOADSCHEMATYPE = DESCRIPTOR.enum_types_by_name['PayloadSchemaType']
PayloadSchemaType = enum_type_wrapper.EnumTypeWrapper(_PAYLOADSCHEMATYPE)
_TOKENIZERTYPE = DESCRIPTOR.enum_types_by_name['TokenizerType']
TokenizerType = enum_type_wrapper.EnumTypeWrapper(_TOKENIZERTYPE)
UnknownDistance = 0
Cosine = 1
Euclid = 2
Dot = 3
UnknownCollectionStatus = 0
Green = 1
Yellow = 2
Red = 3
UnknownType = 0
Keyword = 1
Integer = 2
Float = 3
Geo = 4
Text = 5
Unknown = 0
Prefix = 1
Whitespace = 2
Word = 3


_VECTORPARAMS = DESCRIPTOR.message_types_by_name['VectorParams']
_VECTORPARAMSMAP = DESCRIPTOR.message_types_by_name['VectorParamsMap']
_VECTORPARAMSMAP_MAPENTRY = _VECTORPARAMSMAP.nested_types_by_name['MapEntry']
_VECTORSCONFIG = DESCRIPTOR.message_types_by_name['VectorsConfig']
_GETCOLLECTIONINFOREQUEST = DESCRIPTOR.message_types_by_name['GetCollectionInfoRequest']
_LISTCOLLECTIONSREQUEST = DESCRIPTOR.message_types_by_name['ListCollectionsRequest']
_COLLECTIONDESCRIPTION = DESCRIPTOR.message_types_by_name['CollectionDescription']
_GETCOLLECTIONINFORESPONSE = DESCRIPTOR.message_types_by_name['GetCollectionInfoResponse']
_LISTCOLLECTIONSRESPONSE = DESCRIPTOR.message_types_by_name['ListCollectionsResponse']
_OPTIMIZERSTATUS = DESCRIPTOR.message_types_by_name['OptimizerStatus']
_HNSWCONFIGDIFF = DESCRIPTOR.message_types_by_name['HnswConfigDiff']
_WALCONFIGDIFF = DESCRIPTOR.message_types_by_name['WalConfigDiff']
_OPTIMIZERSCONFIGDIFF = DESCRIPTOR.message_types_by_name['OptimizersConfigDiff']
_CREATECOLLECTION = DESCRIPTOR.message_types_by_name['CreateCollection']
_UPDATECOLLECTION = DESCRIPTOR.message_types_by_name['UpdateCollection']
_DELETECOLLECTION = DESCRIPTOR.message_types_by_name['DeleteCollection']
_COLLECTIONOPERATIONRESPONSE = DESCRIPTOR.message_types_by_name['CollectionOperationResponse']
_COLLECTIONPARAMS = DESCRIPTOR.message_types_by_name['CollectionParams']
_COLLECTIONPARAMSDIFF = DESCRIPTOR.message_types_by_name['CollectionParamsDiff']
_COLLECTIONCONFIG = DESCRIPTOR.message_types_by_name['CollectionConfig']
_TEXTINDEXPARAMS = DESCRIPTOR.message_types_by_name['TextIndexParams']
_PAYLOADINDEXPARAMS = DESCRIPTOR.message_types_by_name['PayloadIndexParams']
_PAYLOADSCHEMAINFO = DESCRIPTOR.message_types_by_name['PayloadSchemaInfo']
_COLLECTIONINFO = DESCRIPTOR.message_types_by_name['CollectionInfo']
_COLLECTIONINFO_PAYLOADSCHEMAENTRY = _COLLECTIONINFO.nested_types_by_name['PayloadSchemaEntry']
_CHANGEALIASES = DESCRIPTOR.message_types_by_name['ChangeAliases']
_ALIASOPERATIONS = DESCRIPTOR.message_types_by_name['AliasOperations']
_CREATEALIAS = DESCRIPTOR.message_types_by_name['CreateAlias']
_RENAMEALIAS = DESCRIPTOR.message_types_by_name['RenameAlias']
_DELETEALIAS = DESCRIPTOR.message_types_by_name['DeleteAlias']
VectorParams = _reflection.GeneratedProtocolMessageType('VectorParams', (_message.Message,), {
  'DESCRIPTOR' : _VECTORPARAMS,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.VectorParams)
  })
_sym_db.RegisterMessage(VectorParams)

VectorParamsMap = _reflection.GeneratedProtocolMessageType('VectorParamsMap', (_message.Message,), {

  'MapEntry' : _reflection.GeneratedProtocolMessageType('MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _VECTORPARAMSMAP_MAPENTRY,
    '__module__' : 'collections_pb2'
    # @@protoc_insertion_point(class_scope:qdrant.VectorParamsMap.MapEntry)
    })
  ,
  'DESCRIPTOR' : _VECTORPARAMSMAP,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.VectorParamsMap)
  })
_sym_db.RegisterMessage(VectorParamsMap)
_sym_db.RegisterMessage(VectorParamsMap.MapEntry)

VectorsConfig = _reflection.GeneratedProtocolMessageType('VectorsConfig', (_message.Message,), {
  'DESCRIPTOR' : _VECTORSCONFIG,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.VectorsConfig)
  })
_sym_db.RegisterMessage(VectorsConfig)

GetCollectionInfoRequest = _reflection.GeneratedProtocolMessageType('GetCollectionInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCOLLECTIONINFOREQUEST,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.GetCollectionInfoRequest)
  })
_sym_db.RegisterMessage(GetCollectionInfoRequest)

ListCollectionsRequest = _reflection.GeneratedProtocolMessageType('ListCollectionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTCOLLECTIONSREQUEST,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.ListCollectionsRequest)
  })
_sym_db.RegisterMessage(ListCollectionsRequest)

CollectionDescription = _reflection.GeneratedProtocolMessageType('CollectionDescription', (_message.Message,), {
  'DESCRIPTOR' : _COLLECTIONDESCRIPTION,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.CollectionDescription)
  })
_sym_db.RegisterMessage(CollectionDescription)

GetCollectionInfoResponse = _reflection.GeneratedProtocolMessageType('GetCollectionInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCOLLECTIONINFORESPONSE,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.GetCollectionInfoResponse)
  })
_sym_db.RegisterMessage(GetCollectionInfoResponse)

ListCollectionsResponse = _reflection.GeneratedProtocolMessageType('ListCollectionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTCOLLECTIONSRESPONSE,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.ListCollectionsResponse)
  })
_sym_db.RegisterMessage(ListCollectionsResponse)

OptimizerStatus = _reflection.GeneratedProtocolMessageType('OptimizerStatus', (_message.Message,), {
  'DESCRIPTOR' : _OPTIMIZERSTATUS,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.OptimizerStatus)
  })
_sym_db.RegisterMessage(OptimizerStatus)

HnswConfigDiff = _reflection.GeneratedProtocolMessageType('HnswConfigDiff', (_message.Message,), {
  'DESCRIPTOR' : _HNSWCONFIGDIFF,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.HnswConfigDiff)
  })
_sym_db.RegisterMessage(HnswConfigDiff)

WalConfigDiff = _reflection.GeneratedProtocolMessageType('WalConfigDiff', (_message.Message,), {
  'DESCRIPTOR' : _WALCONFIGDIFF,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.WalConfigDiff)
  })
_sym_db.RegisterMessage(WalConfigDiff)

OptimizersConfigDiff = _reflection.GeneratedProtocolMessageType('OptimizersConfigDiff', (_message.Message,), {
  'DESCRIPTOR' : _OPTIMIZERSCONFIGDIFF,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.OptimizersConfigDiff)
  })
_sym_db.RegisterMessage(OptimizersConfigDiff)

CreateCollection = _reflection.GeneratedProtocolMessageType('CreateCollection', (_message.Message,), {
  'DESCRIPTOR' : _CREATECOLLECTION,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.CreateCollection)
  })
_sym_db.RegisterMessage(CreateCollection)

UpdateCollection = _reflection.GeneratedProtocolMessageType('UpdateCollection', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECOLLECTION,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.UpdateCollection)
  })
_sym_db.RegisterMessage(UpdateCollection)

DeleteCollection = _reflection.GeneratedProtocolMessageType('DeleteCollection', (_message.Message,), {
  'DESCRIPTOR' : _DELETECOLLECTION,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.DeleteCollection)
  })
_sym_db.RegisterMessage(DeleteCollection)

CollectionOperationResponse = _reflection.GeneratedProtocolMessageType('CollectionOperationResponse', (_message.Message,), {
  'DESCRIPTOR' : _COLLECTIONOPERATIONRESPONSE,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.CollectionOperationResponse)
  })
_sym_db.RegisterMessage(CollectionOperationResponse)

CollectionParams = _reflection.GeneratedProtocolMessageType('CollectionParams', (_message.Message,), {
  'DESCRIPTOR' : _COLLECTIONPARAMS,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.CollectionParams)
  })
_sym_db.RegisterMessage(CollectionParams)

CollectionParamsDiff = _reflection.GeneratedProtocolMessageType('CollectionParamsDiff', (_message.Message,), {
  'DESCRIPTOR' : _COLLECTIONPARAMSDIFF,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.CollectionParamsDiff)
  })
_sym_db.RegisterMessage(CollectionParamsDiff)

CollectionConfig = _reflection.GeneratedProtocolMessageType('CollectionConfig', (_message.Message,), {
  'DESCRIPTOR' : _COLLECTIONCONFIG,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.CollectionConfig)
  })
_sym_db.RegisterMessage(CollectionConfig)

TextIndexParams = _reflection.GeneratedProtocolMessageType('TextIndexParams', (_message.Message,), {
  'DESCRIPTOR' : _TEXTINDEXPARAMS,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.TextIndexParams)
  })
_sym_db.RegisterMessage(TextIndexParams)

PayloadIndexParams = _reflection.GeneratedProtocolMessageType('PayloadIndexParams', (_message.Message,), {
  'DESCRIPTOR' : _PAYLOADINDEXPARAMS,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.PayloadIndexParams)
  })
_sym_db.RegisterMessage(PayloadIndexParams)

PayloadSchemaInfo = _reflection.GeneratedProtocolMessageType('PayloadSchemaInfo', (_message.Message,), {
  'DESCRIPTOR' : _PAYLOADSCHEMAINFO,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.PayloadSchemaInfo)
  })
_sym_db.RegisterMessage(PayloadSchemaInfo)

CollectionInfo = _reflection.GeneratedProtocolMessageType('CollectionInfo', (_message.Message,), {

  'PayloadSchemaEntry' : _reflection.GeneratedProtocolMessageType('PayloadSchemaEntry', (_message.Message,), {
    'DESCRIPTOR' : _COLLECTIONINFO_PAYLOADSCHEMAENTRY,
    '__module__' : 'collections_pb2'
    # @@protoc_insertion_point(class_scope:qdrant.CollectionInfo.PayloadSchemaEntry)
    })
  ,
  'DESCRIPTOR' : _COLLECTIONINFO,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.CollectionInfo)
  })
_sym_db.RegisterMessage(CollectionInfo)
_sym_db.RegisterMessage(CollectionInfo.PayloadSchemaEntry)

ChangeAliases = _reflection.GeneratedProtocolMessageType('ChangeAliases', (_message.Message,), {
  'DESCRIPTOR' : _CHANGEALIASES,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.ChangeAliases)
  })
_sym_db.RegisterMessage(ChangeAliases)

AliasOperations = _reflection.GeneratedProtocolMessageType('AliasOperations', (_message.Message,), {
  'DESCRIPTOR' : _ALIASOPERATIONS,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.AliasOperations)
  })
_sym_db.RegisterMessage(AliasOperations)

CreateAlias = _reflection.GeneratedProtocolMessageType('CreateAlias', (_message.Message,), {
  'DESCRIPTOR' : _CREATEALIAS,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.CreateAlias)
  })
_sym_db.RegisterMessage(CreateAlias)

RenameAlias = _reflection.GeneratedProtocolMessageType('RenameAlias', (_message.Message,), {
  'DESCRIPTOR' : _RENAMEALIAS,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.RenameAlias)
  })
_sym_db.RegisterMessage(RenameAlias)

DeleteAlias = _reflection.GeneratedProtocolMessageType('DeleteAlias', (_message.Message,), {
  'DESCRIPTOR' : _DELETEALIAS,
  '__module__' : 'collections_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.DeleteAlias)
  })
_sym_db.RegisterMessage(DeleteAlias)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _VECTORPARAMSMAP_MAPENTRY._options = None
  _VECTORPARAMSMAP_MAPENTRY._serialized_options = b'8\001'
  _COLLECTIONINFO_PAYLOADSCHEMAENTRY._options = None
  _COLLECTIONINFO_PAYLOADSCHEMAENTRY._serialized_options = b'8\001'
  _DISTANCE._serialized_start=4399
  _DISTANCE._serialized_end=4463
  _COLLECTIONSTATUS._serialized_start=4465
  _COLLECTIONSTATUS._serialized_end=4544
  _PAYLOADSCHEMATYPE._serialized_start=4546
  _PAYLOADSCHEMATYPE._serialized_end=4638
  _TOKENIZERTYPE._serialized_start=4640
  _TOKENIZERTYPE._serialized_end=4706
  _VECTORPARAMS._serialized_start=29
  _VECTORPARAMS._serialized_end=93
  _VECTORPARAMSMAP._serialized_start=96
  _VECTORPARAMSMAP._serialized_end=226
  _VECTORPARAMSMAP_MAPENTRY._serialized_start=162
  _VECTORPARAMSMAP_MAPENTRY._serialized_end=226
  _VECTORSCONFIG._serialized_start=228
  _VECTORSCONFIG._serialized_end=340
  _GETCOLLECTIONINFOREQUEST._serialized_start=342
  _GETCOLLECTIONINFOREQUEST._serialized_end=393
  _LISTCOLLECTIONSREQUEST._serialized_start=395
  _LISTCOLLECTIONSREQUEST._serialized_end=419
  _COLLECTIONDESCRIPTION._serialized_start=421
  _COLLECTIONDESCRIPTION._serialized_end=458
  _GETCOLLECTIONINFORESPONSE._serialized_start=460
  _GETCOLLECTIONINFORESPONSE._serialized_end=541
  _LISTCOLLECTIONSRESPONSE._serialized_start=543
  _LISTCOLLECTIONSRESPONSE._serialized_end=634
  _OPTIMIZERSTATUS._serialized_start=636
  _OPTIMIZERSTATUS._serialized_end=680
  _HNSWCONFIGDIFF._serialized_start=683
  _HNSWCONFIGDIFF._serialized_end=883
  _WALCONFIGDIFF._serialized_start=885
  _WALCONFIGDIFF._serialized_end=1006
  _OPTIMIZERSCONFIGDIFF._serialized_start=1009
  _OPTIMIZERSCONFIGDIFF._serialized_end=1501
  _CREATECOLLECTION._serialized_start=1504
  _CREATECOLLECTION._serialized_end=2095
  _UPDATECOLLECTION._serialized_start=2098
  _UPDATECOLLECTION._serialized_end=2321
  _DELETECOLLECTION._serialized_start=2323
  _DELETECOLLECTION._serialized_end=2400
  _COLLECTIONOPERATIONRESPONSE._serialized_start=2402
  _COLLECTIONOPERATIONRESPONSE._serialized_end=2461
  _COLLECTIONPARAMS._serialized_start=2464
  _COLLECTIONPARAMS._serialized_end=2736
  _COLLECTIONPARAMSDIFF._serialized_start=2739
  _COLLECTIONPARAMSDIFF._serialized_end=2885
  _COLLECTIONCONFIG._serialized_start=2888
  _COLLECTIONCONFIG._serialized_end=3092
  _TEXTINDEXPARAMS._serialized_start=3095
  _TEXTINDEXPARAMS._serialized_end=3284
  _PAYLOADINDEXPARAMS._serialized_start=3286
  _PAYLOADINDEXPARAMS._serialized_end=3376
  _PAYLOADSCHEMAINFO._serialized_start=3379
  _PAYLOADSCHEMAINFO._serialized_end=3536
  _COLLECTIONINFO._serialized_start=3539
  _COLLECTIONINFO._serialized_end=3981
  _COLLECTIONINFO_PAYLOADSCHEMAENTRY._serialized_start=3864
  _COLLECTIONINFO_PAYLOADSCHEMAENTRY._serialized_end=3943
  _CHANGEALIASES._serialized_start=3983
  _CHANGEALIASES._serialized_end=4074
  _ALIASOPERATIONS._serialized_start=4077
  _ALIASOPERATIONS._serialized_end=4239
  _CREATEALIAS._serialized_start=4241
  _CREATEALIAS._serialized_end=4299
  _RENAMEALIAS._serialized_start=4301
  _RENAMEALIAS._serialized_end=4362
  _DELETEALIAS._serialized_start=4364
  _DELETEALIAS._serialized_end=4397
# @@protoc_insertion_point(module_scope)
