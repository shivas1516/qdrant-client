# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: points.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import json_with_int_pb2 as json__with__int__pb2
from . import collections_pb2 as collections__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cpoints.proto\x12\x06qdrant\x1a\x13json_with_int.proto\x1a\x11\x63ollections.proto\"<\n\x07PointId\x12\r\n\x03num\x18\x01 \x01(\x04H\x00\x12\x0e\n\x04uuid\x18\x02 \x01(\tH\x00\x42\x12\n\x10point_id_options\"\x16\n\x06Vector\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x02\"h\n\x0cUpsertPoints\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x11\n\x04wait\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12#\n\x06points\x18\x03 \x03(\x0b\x32\x13.qdrant.PointStructB\x07\n\x05_wait\"k\n\x0c\x44\x65letePoints\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x11\n\x04wait\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12&\n\x06points\x18\x03 \x01(\x0b\x32\x16.qdrant.PointsSelectorB\x07\n\x05_wait\"\xc4\x01\n\tGetPoints\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x1c\n\x03ids\x18\x02 \x03(\x0b\x32\x0f.qdrant.PointId\x12\x31\n\x0cwith_payload\x18\x04 \x01(\x0b\x32\x1b.qdrant.WithPayloadSelector\x12\x36\n\x0cwith_vectors\x18\x05 \x01(\x0b\x32\x1b.qdrant.WithVectorsSelectorH\x00\x88\x01\x01\x42\x0f\n\r_with_vectorsJ\x04\x08\x03\x10\x04\"\xdf\x01\n\x10SetPayloadPoints\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x11\n\x04wait\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12\x36\n\x07payload\x18\x03 \x03(\x0b\x32%.qdrant.SetPayloadPoints.PayloadEntry\x12\x1f\n\x06points\x18\x04 \x03(\x0b\x32\x0f.qdrant.PointId\x1a=\n\x0cPayloadEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.qdrant.Value:\x02\x38\x01\x42\x07\n\x05_wait\"y\n\x13\x44\x65letePayloadPoints\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x11\n\x04wait\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12\x0c\n\x04keys\x18\x03 \x03(\t\x12\x1f\n\x06points\x18\x04 \x03(\x0b\x32\x0f.qdrant.PointIdB\x07\n\x05_wait\"q\n\x12\x43learPayloadPoints\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x11\n\x04wait\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12&\n\x06points\x18\x03 \x01(\x0b\x32\x16.qdrant.PointsSelectorB\x07\n\x05_wait\"\xf4\x01\n\x1a\x43reateFieldIndexCollection\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x11\n\x04wait\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12\x12\n\nfield_name\x18\x03 \x01(\t\x12*\n\nfield_type\x18\x04 \x01(\x0e\x32\x11.qdrant.FieldTypeH\x01\x88\x01\x01\x12;\n\x12\x66ield_index_params\x18\x05 \x01(\x0b\x32\x1a.qdrant.PayloadIndexParamsH\x02\x88\x01\x01\x42\x07\n\x05_waitB\r\n\x0b_field_typeB\x15\n\x13_field_index_params\"e\n\x1a\x44\x65leteFieldIndexCollection\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x11\n\x04wait\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12\x12\n\nfield_name\x18\x03 \x01(\tB\x07\n\x05_wait\"(\n\x16PayloadIncludeSelector\x12\x0e\n\x06\x66ields\x18\x01 \x03(\t\"(\n\x16PayloadExcludeSelector\x12\x0e\n\x06\x66ields\x18\x01 \x03(\t\"\xa1\x01\n\x13WithPayloadSelector\x12\x10\n\x06\x65nable\x18\x01 \x01(\x08H\x00\x12\x31\n\x07include\x18\x02 \x01(\x0b\x32\x1e.qdrant.PayloadIncludeSelectorH\x00\x12\x31\n\x07\x65xclude\x18\x03 \x01(\x0b\x32\x1e.qdrant.PayloadExcludeSelectorH\x00\x42\x12\n\x10selector_options\"\x82\x01\n\x0cNamedVectors\x12\x32\n\x07vectors\x18\x01 \x03(\x0b\x32!.qdrant.NamedVectors.VectorsEntry\x1a>\n\x0cVectorsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.qdrant.Vector:\x02\x38\x01\"g\n\x07Vectors\x12 \n\x06vector\x18\x01 \x01(\x0b\x32\x0e.qdrant.VectorH\x00\x12\'\n\x07vectors\x18\x02 \x01(\x0b\x32\x14.qdrant.NamedVectorsH\x00\x42\x11\n\x0fvectors_options\" \n\x0fVectorsSelector\x12\r\n\x05names\x18\x01 \x03(\t\"g\n\x13WithVectorsSelector\x12\x10\n\x06\x65nable\x18\x01 \x01(\x08H\x00\x12*\n\x07include\x18\x02 \x01(\x0b\x32\x17.qdrant.VectorsSelectorH\x00\x42\x12\n\x10selector_options\"N\n\x0cSearchParams\x12\x14\n\x07hnsw_ef\x18\x01 \x01(\x04H\x00\x88\x01\x01\x12\x12\n\x05\x65xact\x18\x02 \x01(\x08H\x01\x88\x01\x01\x42\n\n\x08_hnsw_efB\x08\n\x06_exact\"\x8a\x03\n\x0cSearchPoints\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x0e\n\x06vector\x18\x02 \x03(\x02\x12\x1e\n\x06\x66ilter\x18\x03 \x01(\x0b\x32\x0e.qdrant.Filter\x12\r\n\x05limit\x18\x04 \x01(\x04\x12\x31\n\x0cwith_payload\x18\x06 \x01(\x0b\x32\x1b.qdrant.WithPayloadSelector\x12$\n\x06params\x18\x07 \x01(\x0b\x32\x14.qdrant.SearchParams\x12\x1c\n\x0fscore_threshold\x18\x08 \x01(\x02H\x00\x88\x01\x01\x12\x13\n\x06offset\x18\t \x01(\x04H\x01\x88\x01\x01\x12\x18\n\x0bvector_name\x18\n \x01(\tH\x02\x88\x01\x01\x12\x36\n\x0cwith_vectors\x18\x0b \x01(\x0b\x32\x1b.qdrant.WithVectorsSelectorH\x03\x88\x01\x01\x42\x12\n\x10_score_thresholdB\t\n\x07_offsetB\x0e\n\x0c_vector_nameB\x0f\n\r_with_vectorsJ\x04\x08\x05\x10\x06\"Y\n\x11SearchBatchPoints\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12+\n\rsearch_points\x18\x02 \x03(\x0b\x32\x14.qdrant.SearchPoints\"\x98\x02\n\x0cScrollPoints\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x1e\n\x06\x66ilter\x18\x02 \x01(\x0b\x32\x0e.qdrant.Filter\x12$\n\x06offset\x18\x03 \x01(\x0b\x32\x0f.qdrant.PointIdH\x00\x88\x01\x01\x12\x12\n\x05limit\x18\x04 \x01(\rH\x01\x88\x01\x01\x12\x31\n\x0cwith_payload\x18\x06 \x01(\x0b\x32\x1b.qdrant.WithPayloadSelector\x12\x36\n\x0cwith_vectors\x18\x07 \x01(\x0b\x32\x1b.qdrant.WithVectorsSelectorH\x02\x88\x01\x01\x42\t\n\x07_offsetB\x08\n\x06_limitB\x0f\n\r_with_vectorsJ\x04\x08\x05\x10\x06\"\xb7\x03\n\x0fRecommendPoints\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12!\n\x08positive\x18\x02 \x03(\x0b\x32\x0f.qdrant.PointId\x12!\n\x08negative\x18\x03 \x03(\x0b\x32\x0f.qdrant.PointId\x12\x1e\n\x06\x66ilter\x18\x04 \x01(\x0b\x32\x0e.qdrant.Filter\x12\r\n\x05limit\x18\x05 \x01(\x04\x12\x31\n\x0cwith_payload\x18\x07 \x01(\x0b\x32\x1b.qdrant.WithPayloadSelector\x12$\n\x06params\x18\x08 \x01(\x0b\x32\x14.qdrant.SearchParams\x12\x1c\n\x0fscore_threshold\x18\t \x01(\x02H\x00\x88\x01\x01\x12\x13\n\x06offset\x18\n \x01(\x04H\x01\x88\x01\x01\x12\x12\n\x05using\x18\x0b \x01(\tH\x02\x88\x01\x01\x12\x36\n\x0cwith_vectors\x18\x0c \x01(\x0b\x32\x1b.qdrant.WithVectorsSelectorH\x03\x88\x01\x01\x42\x12\n\x10_score_thresholdB\t\n\x07_offsetB\x08\n\x06_usingB\x0f\n\r_with_vectorsJ\x04\x08\x06\x10\x07\"b\n\x14RecommendBatchPoints\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x31\n\x10recommend_points\x18\x02 \x03(\x0b\x32\x17.qdrant.RecommendPoints\"d\n\x0b\x43ountPoints\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x1e\n\x06\x66ilter\x18\x02 \x01(\x0b\x32\x0e.qdrant.Filter\x12\x12\n\x05\x65xact\x18\x03 \x01(\x08H\x00\x88\x01\x01\x42\x08\n\x06_exact\"M\n\x17PointsOperationResponse\x12$\n\x06result\x18\x01 \x01(\x0b\x32\x14.qdrant.UpdateResult\x12\x0c\n\x04time\x18\x02 \x01(\x01\"J\n\x0cUpdateResult\x12\x14\n\x0coperation_id\x18\x01 \x01(\x04\x12$\n\x06status\x18\x02 \x01(\x0e\x32\x14.qdrant.UpdateStatus\"\xf5\x01\n\x0bScoredPoint\x12\x1b\n\x02id\x18\x01 \x01(\x0b\x32\x0f.qdrant.PointId\x12\x31\n\x07payload\x18\x02 \x03(\x0b\x32 .qdrant.ScoredPoint.PayloadEntry\x12\r\n\x05score\x18\x03 \x01(\x02\x12\x0f\n\x07version\x18\x05 \x01(\x04\x12%\n\x07vectors\x18\x06 \x01(\x0b\x32\x0f.qdrant.VectorsH\x00\x88\x01\x01\x1a=\n\x0cPayloadEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.qdrant.Value:\x02\x38\x01\x42\n\n\x08_vectorsJ\x04\x08\x04\x10\x05\"C\n\x0eSearchResponse\x12#\n\x06result\x18\x01 \x03(\x0b\x32\x13.qdrant.ScoredPoint\x12\x0c\n\x04time\x18\x02 \x01(\x01\"2\n\x0b\x42\x61tchResult\x12#\n\x06result\x18\x01 \x03(\x0b\x32\x13.qdrant.ScoredPoint\"H\n\x13SearchBatchResponse\x12#\n\x06result\x18\x01 \x03(\x0b\x32\x13.qdrant.BatchResult\x12\x0c\n\x04time\x18\x02 \x01(\x01\"B\n\rCountResponse\x12#\n\x06result\x18\x01 \x01(\x0b\x32\x13.qdrant.CountResult\x12\x0c\n\x04time\x18\x02 \x01(\x01\"\x8b\x01\n\x0eScrollResponse\x12.\n\x10next_page_offset\x18\x01 \x01(\x0b\x32\x0f.qdrant.PointIdH\x00\x88\x01\x01\x12&\n\x06result\x18\x02 \x03(\x0b\x32\x16.qdrant.RetrievedPoint\x12\x0c\n\x04time\x18\x03 \x01(\x01\x42\x13\n\x11_next_page_offset\"\x1c\n\x0b\x43ountResult\x12\r\n\x05\x63ount\x18\x01 \x01(\x04\"\xdb\x01\n\x0eRetrievedPoint\x12\x1b\n\x02id\x18\x01 \x01(\x0b\x32\x0f.qdrant.PointId\x12\x34\n\x07payload\x18\x02 \x03(\x0b\x32#.qdrant.RetrievedPoint.PayloadEntry\x12%\n\x07vectors\x18\x04 \x01(\x0b\x32\x0f.qdrant.VectorsH\x00\x88\x01\x01\x1a=\n\x0cPayloadEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.qdrant.Value:\x02\x38\x01\x42\n\n\x08_vectorsJ\x04\x08\x03\x10\x04\"C\n\x0bGetResponse\x12&\n\x06result\x18\x01 \x03(\x0b\x32\x16.qdrant.RetrievedPoint\x12\x0c\n\x04time\x18\x02 \x01(\x01\"F\n\x11RecommendResponse\x12#\n\x06result\x18\x01 \x03(\x0b\x32\x13.qdrant.ScoredPoint\x12\x0c\n\x04time\x18\x02 \x01(\x01\"K\n\x16RecommendBatchResponse\x12#\n\x06result\x18\x01 \x03(\x0b\x32\x13.qdrant.BatchResult\x12\x0c\n\x04time\x18\x02 \x01(\x01\"q\n\x06\x46ilter\x12!\n\x06should\x18\x01 \x03(\x0b\x32\x11.qdrant.Condition\x12\x1f\n\x04must\x18\x02 \x03(\x0b\x32\x11.qdrant.Condition\x12#\n\x08must_not\x18\x03 \x03(\x0b\x32\x11.qdrant.Condition\"\xc2\x01\n\tCondition\x12\'\n\x05\x66ield\x18\x01 \x01(\x0b\x32\x16.qdrant.FieldConditionH\x00\x12,\n\x08is_empty\x18\x02 \x01(\x0b\x32\x18.qdrant.IsEmptyConditionH\x00\x12(\n\x06has_id\x18\x03 \x01(\x0b\x32\x16.qdrant.HasIdConditionH\x00\x12 \n\x06\x66ilter\x18\x04 \x01(\x0b\x32\x0e.qdrant.FilterH\x00\x42\x12\n\x10\x63ondition_one_of\"\x1f\n\x10IsEmptyCondition\x12\x0b\n\x03key\x18\x01 \x01(\t\"1\n\x0eHasIdCondition\x12\x1f\n\x06has_id\x18\x01 \x03(\x0b\x32\x0f.qdrant.PointId\"\xdd\x01\n\x0e\x46ieldCondition\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x05match\x18\x02 \x01(\x0b\x32\r.qdrant.Match\x12\x1c\n\x05range\x18\x03 \x01(\x0b\x32\r.qdrant.Range\x12\x30\n\x10geo_bounding_box\x18\x04 \x01(\x0b\x32\x16.qdrant.GeoBoundingBox\x12%\n\ngeo_radius\x18\x05 \x01(\x0b\x32\x11.qdrant.GeoRadius\x12)\n\x0cvalues_count\x18\x06 \x01(\x0b\x32\x13.qdrant.ValuesCount\"_\n\x05Match\x12\x11\n\x07keyword\x18\x01 \x01(\tH\x00\x12\x11\n\x07integer\x18\x02 \x01(\x03H\x00\x12\x11\n\x07\x62oolean\x18\x03 \x01(\x08H\x00\x12\x0e\n\x04text\x18\x04 \x01(\tH\x00\x42\r\n\x0bmatch_value\"k\n\x05Range\x12\x0f\n\x02lt\x18\x01 \x01(\x01H\x00\x88\x01\x01\x12\x0f\n\x02gt\x18\x02 \x01(\x01H\x01\x88\x01\x01\x12\x10\n\x03gte\x18\x03 \x01(\x01H\x02\x88\x01\x01\x12\x10\n\x03lte\x18\x04 \x01(\x01H\x03\x88\x01\x01\x42\x05\n\x03_ltB\x05\n\x03_gtB\x06\n\x04_gteB\x06\n\x04_lte\"\\\n\x0eGeoBoundingBox\x12\"\n\x08top_left\x18\x01 \x01(\x0b\x32\x10.qdrant.GeoPoint\x12&\n\x0c\x62ottom_right\x18\x02 \x01(\x0b\x32\x10.qdrant.GeoPoint\"=\n\tGeoRadius\x12 \n\x06\x63\x65nter\x18\x01 \x01(\x0b\x32\x10.qdrant.GeoPoint\x12\x0e\n\x06radius\x18\x02 \x01(\x02\"q\n\x0bValuesCount\x12\x0f\n\x02lt\x18\x01 \x01(\x04H\x00\x88\x01\x01\x12\x0f\n\x02gt\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12\x10\n\x03gte\x18\x03 \x01(\x04H\x02\x88\x01\x01\x12\x10\n\x03lte\x18\x04 \x01(\x04H\x03\x88\x01\x01\x42\x05\n\x03_ltB\x05\n\x03_gtB\x06\n\x04_gteB\x06\n\x04_lte\"u\n\x0ePointsSelector\x12\'\n\x06points\x18\x01 \x01(\x0b\x32\x15.qdrant.PointsIdsListH\x00\x12 \n\x06\x66ilter\x18\x02 \x01(\x0b\x32\x0e.qdrant.FilterH\x00\x42\x18\n\x16points_selector_one_of\"-\n\rPointsIdsList\x12\x1c\n\x03ids\x18\x01 \x03(\x0b\x32\x0f.qdrant.PointId\"\xd5\x01\n\x0bPointStruct\x12\x1b\n\x02id\x18\x01 \x01(\x0b\x32\x0f.qdrant.PointId\x12\x31\n\x07payload\x18\x03 \x03(\x0b\x32 .qdrant.PointStruct.PayloadEntry\x12%\n\x07vectors\x18\x04 \x01(\x0b\x32\x0f.qdrant.VectorsH\x00\x88\x01\x01\x1a=\n\x0cPayloadEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.qdrant.Value:\x02\x38\x01\x42\n\n\x08_vectorsJ\x04\x08\x02\x10\x03\"$\n\x08GeoPoint\x12\x0b\n\x03lon\x18\x01 \x01(\x01\x12\x0b\n\x03lat\x18\x02 \x01(\x01*p\n\tFieldType\x12\x14\n\x10\x46ieldTypeKeyword\x10\x00\x12\x14\n\x10\x46ieldTypeInteger\x10\x01\x12\x12\n\x0e\x46ieldTypeFloat\x10\x02\x12\x10\n\x0c\x46ieldTypeGeo\x10\x03\x12\x11\n\rFieldTypeText\x10\x04*H\n\x0cUpdateStatus\x12\x17\n\x13UnknownUpdateStatus\x10\x00\x12\x10\n\x0c\x41\x63knowledged\x10\x01\x12\r\n\tCompleted\x10\x02\x62\x06proto3')

_FIELDTYPE = DESCRIPTOR.enum_types_by_name['FieldType']
FieldType = enum_type_wrapper.EnumTypeWrapper(_FIELDTYPE)
_UPDATESTATUS = DESCRIPTOR.enum_types_by_name['UpdateStatus']
UpdateStatus = enum_type_wrapper.EnumTypeWrapper(_UPDATESTATUS)
FieldTypeKeyword = 0
FieldTypeInteger = 1
FieldTypeFloat = 2
FieldTypeGeo = 3
FieldTypeText = 4
UnknownUpdateStatus = 0
Acknowledged = 1
Completed = 2


_POINTID = DESCRIPTOR.message_types_by_name['PointId']
_VECTOR = DESCRIPTOR.message_types_by_name['Vector']
_UPSERTPOINTS = DESCRIPTOR.message_types_by_name['UpsertPoints']
_DELETEPOINTS = DESCRIPTOR.message_types_by_name['DeletePoints']
_GETPOINTS = DESCRIPTOR.message_types_by_name['GetPoints']
_SETPAYLOADPOINTS = DESCRIPTOR.message_types_by_name['SetPayloadPoints']
_SETPAYLOADPOINTS_PAYLOADENTRY = _SETPAYLOADPOINTS.nested_types_by_name['PayloadEntry']
_DELETEPAYLOADPOINTS = DESCRIPTOR.message_types_by_name['DeletePayloadPoints']
_CLEARPAYLOADPOINTS = DESCRIPTOR.message_types_by_name['ClearPayloadPoints']
_CREATEFIELDINDEXCOLLECTION = DESCRIPTOR.message_types_by_name['CreateFieldIndexCollection']
_DELETEFIELDINDEXCOLLECTION = DESCRIPTOR.message_types_by_name['DeleteFieldIndexCollection']
_PAYLOADINCLUDESELECTOR = DESCRIPTOR.message_types_by_name['PayloadIncludeSelector']
_PAYLOADEXCLUDESELECTOR = DESCRIPTOR.message_types_by_name['PayloadExcludeSelector']
_WITHPAYLOADSELECTOR = DESCRIPTOR.message_types_by_name['WithPayloadSelector']
_NAMEDVECTORS = DESCRIPTOR.message_types_by_name['NamedVectors']
_NAMEDVECTORS_VECTORSENTRY = _NAMEDVECTORS.nested_types_by_name['VectorsEntry']
_VECTORS = DESCRIPTOR.message_types_by_name['Vectors']
_VECTORSSELECTOR = DESCRIPTOR.message_types_by_name['VectorsSelector']
_WITHVECTORSSELECTOR = DESCRIPTOR.message_types_by_name['WithVectorsSelector']
_SEARCHPARAMS = DESCRIPTOR.message_types_by_name['SearchParams']
_SEARCHPOINTS = DESCRIPTOR.message_types_by_name['SearchPoints']
_SEARCHBATCHPOINTS = DESCRIPTOR.message_types_by_name['SearchBatchPoints']
_SCROLLPOINTS = DESCRIPTOR.message_types_by_name['ScrollPoints']
_RECOMMENDPOINTS = DESCRIPTOR.message_types_by_name['RecommendPoints']
_RECOMMENDBATCHPOINTS = DESCRIPTOR.message_types_by_name['RecommendBatchPoints']
_COUNTPOINTS = DESCRIPTOR.message_types_by_name['CountPoints']
_POINTSOPERATIONRESPONSE = DESCRIPTOR.message_types_by_name['PointsOperationResponse']
_UPDATERESULT = DESCRIPTOR.message_types_by_name['UpdateResult']
_SCOREDPOINT = DESCRIPTOR.message_types_by_name['ScoredPoint']
_SCOREDPOINT_PAYLOADENTRY = _SCOREDPOINT.nested_types_by_name['PayloadEntry']
_SEARCHRESPONSE = DESCRIPTOR.message_types_by_name['SearchResponse']
_BATCHRESULT = DESCRIPTOR.message_types_by_name['BatchResult']
_SEARCHBATCHRESPONSE = DESCRIPTOR.message_types_by_name['SearchBatchResponse']
_COUNTRESPONSE = DESCRIPTOR.message_types_by_name['CountResponse']
_SCROLLRESPONSE = DESCRIPTOR.message_types_by_name['ScrollResponse']
_COUNTRESULT = DESCRIPTOR.message_types_by_name['CountResult']
_RETRIEVEDPOINT = DESCRIPTOR.message_types_by_name['RetrievedPoint']
_RETRIEVEDPOINT_PAYLOADENTRY = _RETRIEVEDPOINT.nested_types_by_name['PayloadEntry']
_GETRESPONSE = DESCRIPTOR.message_types_by_name['GetResponse']
_RECOMMENDRESPONSE = DESCRIPTOR.message_types_by_name['RecommendResponse']
_RECOMMENDBATCHRESPONSE = DESCRIPTOR.message_types_by_name['RecommendBatchResponse']
_FILTER = DESCRIPTOR.message_types_by_name['Filter']
_CONDITION = DESCRIPTOR.message_types_by_name['Condition']
_ISEMPTYCONDITION = DESCRIPTOR.message_types_by_name['IsEmptyCondition']
_HASIDCONDITION = DESCRIPTOR.message_types_by_name['HasIdCondition']
_FIELDCONDITION = DESCRIPTOR.message_types_by_name['FieldCondition']
_MATCH = DESCRIPTOR.message_types_by_name['Match']
_RANGE = DESCRIPTOR.message_types_by_name['Range']
_GEOBOUNDINGBOX = DESCRIPTOR.message_types_by_name['GeoBoundingBox']
_GEORADIUS = DESCRIPTOR.message_types_by_name['GeoRadius']
_VALUESCOUNT = DESCRIPTOR.message_types_by_name['ValuesCount']
_POINTSSELECTOR = DESCRIPTOR.message_types_by_name['PointsSelector']
_POINTSIDSLIST = DESCRIPTOR.message_types_by_name['PointsIdsList']
_POINTSTRUCT = DESCRIPTOR.message_types_by_name['PointStruct']
_POINTSTRUCT_PAYLOADENTRY = _POINTSTRUCT.nested_types_by_name['PayloadEntry']
_GEOPOINT = DESCRIPTOR.message_types_by_name['GeoPoint']
PointId = _reflection.GeneratedProtocolMessageType('PointId', (_message.Message,), {
  'DESCRIPTOR' : _POINTID,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.PointId)
  })
_sym_db.RegisterMessage(PointId)

Vector = _reflection.GeneratedProtocolMessageType('Vector', (_message.Message,), {
  'DESCRIPTOR' : _VECTOR,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.Vector)
  })
_sym_db.RegisterMessage(Vector)

UpsertPoints = _reflection.GeneratedProtocolMessageType('UpsertPoints', (_message.Message,), {
  'DESCRIPTOR' : _UPSERTPOINTS,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.UpsertPoints)
  })
_sym_db.RegisterMessage(UpsertPoints)

DeletePoints = _reflection.GeneratedProtocolMessageType('DeletePoints', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPOINTS,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.DeletePoints)
  })
_sym_db.RegisterMessage(DeletePoints)

GetPoints = _reflection.GeneratedProtocolMessageType('GetPoints', (_message.Message,), {
  'DESCRIPTOR' : _GETPOINTS,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.GetPoints)
  })
_sym_db.RegisterMessage(GetPoints)

SetPayloadPoints = _reflection.GeneratedProtocolMessageType('SetPayloadPoints', (_message.Message,), {

  'PayloadEntry' : _reflection.GeneratedProtocolMessageType('PayloadEntry', (_message.Message,), {
    'DESCRIPTOR' : _SETPAYLOADPOINTS_PAYLOADENTRY,
    '__module__' : 'points_pb2'
    # @@protoc_insertion_point(class_scope:qdrant.SetPayloadPoints.PayloadEntry)
    })
  ,
  'DESCRIPTOR' : _SETPAYLOADPOINTS,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.SetPayloadPoints)
  })
_sym_db.RegisterMessage(SetPayloadPoints)
_sym_db.RegisterMessage(SetPayloadPoints.PayloadEntry)

DeletePayloadPoints = _reflection.GeneratedProtocolMessageType('DeletePayloadPoints', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPAYLOADPOINTS,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.DeletePayloadPoints)
  })
_sym_db.RegisterMessage(DeletePayloadPoints)

ClearPayloadPoints = _reflection.GeneratedProtocolMessageType('ClearPayloadPoints', (_message.Message,), {
  'DESCRIPTOR' : _CLEARPAYLOADPOINTS,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.ClearPayloadPoints)
  })
_sym_db.RegisterMessage(ClearPayloadPoints)

CreateFieldIndexCollection = _reflection.GeneratedProtocolMessageType('CreateFieldIndexCollection', (_message.Message,), {
  'DESCRIPTOR' : _CREATEFIELDINDEXCOLLECTION,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.CreateFieldIndexCollection)
  })
_sym_db.RegisterMessage(CreateFieldIndexCollection)

DeleteFieldIndexCollection = _reflection.GeneratedProtocolMessageType('DeleteFieldIndexCollection', (_message.Message,), {
  'DESCRIPTOR' : _DELETEFIELDINDEXCOLLECTION,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.DeleteFieldIndexCollection)
  })
_sym_db.RegisterMessage(DeleteFieldIndexCollection)

PayloadIncludeSelector = _reflection.GeneratedProtocolMessageType('PayloadIncludeSelector', (_message.Message,), {
  'DESCRIPTOR' : _PAYLOADINCLUDESELECTOR,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.PayloadIncludeSelector)
  })
_sym_db.RegisterMessage(PayloadIncludeSelector)

PayloadExcludeSelector = _reflection.GeneratedProtocolMessageType('PayloadExcludeSelector', (_message.Message,), {
  'DESCRIPTOR' : _PAYLOADEXCLUDESELECTOR,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.PayloadExcludeSelector)
  })
_sym_db.RegisterMessage(PayloadExcludeSelector)

WithPayloadSelector = _reflection.GeneratedProtocolMessageType('WithPayloadSelector', (_message.Message,), {
  'DESCRIPTOR' : _WITHPAYLOADSELECTOR,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.WithPayloadSelector)
  })
_sym_db.RegisterMessage(WithPayloadSelector)

NamedVectors = _reflection.GeneratedProtocolMessageType('NamedVectors', (_message.Message,), {

  'VectorsEntry' : _reflection.GeneratedProtocolMessageType('VectorsEntry', (_message.Message,), {
    'DESCRIPTOR' : _NAMEDVECTORS_VECTORSENTRY,
    '__module__' : 'points_pb2'
    # @@protoc_insertion_point(class_scope:qdrant.NamedVectors.VectorsEntry)
    })
  ,
  'DESCRIPTOR' : _NAMEDVECTORS,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.NamedVectors)
  })
_sym_db.RegisterMessage(NamedVectors)
_sym_db.RegisterMessage(NamedVectors.VectorsEntry)

Vectors = _reflection.GeneratedProtocolMessageType('Vectors', (_message.Message,), {
  'DESCRIPTOR' : _VECTORS,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.Vectors)
  })
_sym_db.RegisterMessage(Vectors)

VectorsSelector = _reflection.GeneratedProtocolMessageType('VectorsSelector', (_message.Message,), {
  'DESCRIPTOR' : _VECTORSSELECTOR,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.VectorsSelector)
  })
_sym_db.RegisterMessage(VectorsSelector)

WithVectorsSelector = _reflection.GeneratedProtocolMessageType('WithVectorsSelector', (_message.Message,), {
  'DESCRIPTOR' : _WITHVECTORSSELECTOR,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.WithVectorsSelector)
  })
_sym_db.RegisterMessage(WithVectorsSelector)

SearchParams = _reflection.GeneratedProtocolMessageType('SearchParams', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHPARAMS,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.SearchParams)
  })
_sym_db.RegisterMessage(SearchParams)

SearchPoints = _reflection.GeneratedProtocolMessageType('SearchPoints', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHPOINTS,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.SearchPoints)
  })
_sym_db.RegisterMessage(SearchPoints)

SearchBatchPoints = _reflection.GeneratedProtocolMessageType('SearchBatchPoints', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHBATCHPOINTS,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.SearchBatchPoints)
  })
_sym_db.RegisterMessage(SearchBatchPoints)

ScrollPoints = _reflection.GeneratedProtocolMessageType('ScrollPoints', (_message.Message,), {
  'DESCRIPTOR' : _SCROLLPOINTS,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.ScrollPoints)
  })
_sym_db.RegisterMessage(ScrollPoints)

RecommendPoints = _reflection.GeneratedProtocolMessageType('RecommendPoints', (_message.Message,), {
  'DESCRIPTOR' : _RECOMMENDPOINTS,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.RecommendPoints)
  })
_sym_db.RegisterMessage(RecommendPoints)

RecommendBatchPoints = _reflection.GeneratedProtocolMessageType('RecommendBatchPoints', (_message.Message,), {
  'DESCRIPTOR' : _RECOMMENDBATCHPOINTS,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.RecommendBatchPoints)
  })
_sym_db.RegisterMessage(RecommendBatchPoints)

CountPoints = _reflection.GeneratedProtocolMessageType('CountPoints', (_message.Message,), {
  'DESCRIPTOR' : _COUNTPOINTS,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.CountPoints)
  })
_sym_db.RegisterMessage(CountPoints)

PointsOperationResponse = _reflection.GeneratedProtocolMessageType('PointsOperationResponse', (_message.Message,), {
  'DESCRIPTOR' : _POINTSOPERATIONRESPONSE,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.PointsOperationResponse)
  })
_sym_db.RegisterMessage(PointsOperationResponse)

UpdateResult = _reflection.GeneratedProtocolMessageType('UpdateResult', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERESULT,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.UpdateResult)
  })
_sym_db.RegisterMessage(UpdateResult)

ScoredPoint = _reflection.GeneratedProtocolMessageType('ScoredPoint', (_message.Message,), {

  'PayloadEntry' : _reflection.GeneratedProtocolMessageType('PayloadEntry', (_message.Message,), {
    'DESCRIPTOR' : _SCOREDPOINT_PAYLOADENTRY,
    '__module__' : 'points_pb2'
    # @@protoc_insertion_point(class_scope:qdrant.ScoredPoint.PayloadEntry)
    })
  ,
  'DESCRIPTOR' : _SCOREDPOINT,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.ScoredPoint)
  })
_sym_db.RegisterMessage(ScoredPoint)
_sym_db.RegisterMessage(ScoredPoint.PayloadEntry)

SearchResponse = _reflection.GeneratedProtocolMessageType('SearchResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHRESPONSE,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.SearchResponse)
  })
_sym_db.RegisterMessage(SearchResponse)

BatchResult = _reflection.GeneratedProtocolMessageType('BatchResult', (_message.Message,), {
  'DESCRIPTOR' : _BATCHRESULT,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.BatchResult)
  })
_sym_db.RegisterMessage(BatchResult)

SearchBatchResponse = _reflection.GeneratedProtocolMessageType('SearchBatchResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHBATCHRESPONSE,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.SearchBatchResponse)
  })
_sym_db.RegisterMessage(SearchBatchResponse)

CountResponse = _reflection.GeneratedProtocolMessageType('CountResponse', (_message.Message,), {
  'DESCRIPTOR' : _COUNTRESPONSE,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.CountResponse)
  })
_sym_db.RegisterMessage(CountResponse)

ScrollResponse = _reflection.GeneratedProtocolMessageType('ScrollResponse', (_message.Message,), {
  'DESCRIPTOR' : _SCROLLRESPONSE,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.ScrollResponse)
  })
_sym_db.RegisterMessage(ScrollResponse)

CountResult = _reflection.GeneratedProtocolMessageType('CountResult', (_message.Message,), {
  'DESCRIPTOR' : _COUNTRESULT,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.CountResult)
  })
_sym_db.RegisterMessage(CountResult)

RetrievedPoint = _reflection.GeneratedProtocolMessageType('RetrievedPoint', (_message.Message,), {

  'PayloadEntry' : _reflection.GeneratedProtocolMessageType('PayloadEntry', (_message.Message,), {
    'DESCRIPTOR' : _RETRIEVEDPOINT_PAYLOADENTRY,
    '__module__' : 'points_pb2'
    # @@protoc_insertion_point(class_scope:qdrant.RetrievedPoint.PayloadEntry)
    })
  ,
  'DESCRIPTOR' : _RETRIEVEDPOINT,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.RetrievedPoint)
  })
_sym_db.RegisterMessage(RetrievedPoint)
_sym_db.RegisterMessage(RetrievedPoint.PayloadEntry)

GetResponse = _reflection.GeneratedProtocolMessageType('GetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRESPONSE,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.GetResponse)
  })
_sym_db.RegisterMessage(GetResponse)

RecommendResponse = _reflection.GeneratedProtocolMessageType('RecommendResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECOMMENDRESPONSE,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.RecommendResponse)
  })
_sym_db.RegisterMessage(RecommendResponse)

RecommendBatchResponse = _reflection.GeneratedProtocolMessageType('RecommendBatchResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECOMMENDBATCHRESPONSE,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.RecommendBatchResponse)
  })
_sym_db.RegisterMessage(RecommendBatchResponse)

Filter = _reflection.GeneratedProtocolMessageType('Filter', (_message.Message,), {
  'DESCRIPTOR' : _FILTER,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.Filter)
  })
_sym_db.RegisterMessage(Filter)

Condition = _reflection.GeneratedProtocolMessageType('Condition', (_message.Message,), {
  'DESCRIPTOR' : _CONDITION,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.Condition)
  })
_sym_db.RegisterMessage(Condition)

IsEmptyCondition = _reflection.GeneratedProtocolMessageType('IsEmptyCondition', (_message.Message,), {
  'DESCRIPTOR' : _ISEMPTYCONDITION,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.IsEmptyCondition)
  })
_sym_db.RegisterMessage(IsEmptyCondition)

HasIdCondition = _reflection.GeneratedProtocolMessageType('HasIdCondition', (_message.Message,), {
  'DESCRIPTOR' : _HASIDCONDITION,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.HasIdCondition)
  })
_sym_db.RegisterMessage(HasIdCondition)

FieldCondition = _reflection.GeneratedProtocolMessageType('FieldCondition', (_message.Message,), {
  'DESCRIPTOR' : _FIELDCONDITION,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.FieldCondition)
  })
_sym_db.RegisterMessage(FieldCondition)

Match = _reflection.GeneratedProtocolMessageType('Match', (_message.Message,), {
  'DESCRIPTOR' : _MATCH,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.Match)
  })
_sym_db.RegisterMessage(Match)

Range = _reflection.GeneratedProtocolMessageType('Range', (_message.Message,), {
  'DESCRIPTOR' : _RANGE,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.Range)
  })
_sym_db.RegisterMessage(Range)

GeoBoundingBox = _reflection.GeneratedProtocolMessageType('GeoBoundingBox', (_message.Message,), {
  'DESCRIPTOR' : _GEOBOUNDINGBOX,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.GeoBoundingBox)
  })
_sym_db.RegisterMessage(GeoBoundingBox)

GeoRadius = _reflection.GeneratedProtocolMessageType('GeoRadius', (_message.Message,), {
  'DESCRIPTOR' : _GEORADIUS,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.GeoRadius)
  })
_sym_db.RegisterMessage(GeoRadius)

ValuesCount = _reflection.GeneratedProtocolMessageType('ValuesCount', (_message.Message,), {
  'DESCRIPTOR' : _VALUESCOUNT,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.ValuesCount)
  })
_sym_db.RegisterMessage(ValuesCount)

PointsSelector = _reflection.GeneratedProtocolMessageType('PointsSelector', (_message.Message,), {
  'DESCRIPTOR' : _POINTSSELECTOR,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.PointsSelector)
  })
_sym_db.RegisterMessage(PointsSelector)

PointsIdsList = _reflection.GeneratedProtocolMessageType('PointsIdsList', (_message.Message,), {
  'DESCRIPTOR' : _POINTSIDSLIST,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.PointsIdsList)
  })
_sym_db.RegisterMessage(PointsIdsList)

PointStruct = _reflection.GeneratedProtocolMessageType('PointStruct', (_message.Message,), {

  'PayloadEntry' : _reflection.GeneratedProtocolMessageType('PayloadEntry', (_message.Message,), {
    'DESCRIPTOR' : _POINTSTRUCT_PAYLOADENTRY,
    '__module__' : 'points_pb2'
    # @@protoc_insertion_point(class_scope:qdrant.PointStruct.PayloadEntry)
    })
  ,
  'DESCRIPTOR' : _POINTSTRUCT,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.PointStruct)
  })
_sym_db.RegisterMessage(PointStruct)
_sym_db.RegisterMessage(PointStruct.PayloadEntry)

GeoPoint = _reflection.GeneratedProtocolMessageType('GeoPoint', (_message.Message,), {
  'DESCRIPTOR' : _GEOPOINT,
  '__module__' : 'points_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.GeoPoint)
  })
_sym_db.RegisterMessage(GeoPoint)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SETPAYLOADPOINTS_PAYLOADENTRY._options = None
  _SETPAYLOADPOINTS_PAYLOADENTRY._serialized_options = b'8\001'
  _NAMEDVECTORS_VECTORSENTRY._options = None
  _NAMEDVECTORS_VECTORSENTRY._serialized_options = b'8\001'
  _SCOREDPOINT_PAYLOADENTRY._options = None
  _SCOREDPOINT_PAYLOADENTRY._serialized_options = b'8\001'
  _RETRIEVEDPOINT_PAYLOADENTRY._options = None
  _RETRIEVEDPOINT_PAYLOADENTRY._serialized_options = b'8\001'
  _POINTSTRUCT_PAYLOADENTRY._options = None
  _POINTSTRUCT_PAYLOADENTRY._serialized_options = b'8\001'
  _FIELDTYPE._serialized_start=6294
  _FIELDTYPE._serialized_end=6406
  _UPDATESTATUS._serialized_start=6408
  _UPDATESTATUS._serialized_end=6480
  _POINTID._serialized_start=64
  _POINTID._serialized_end=124
  _VECTOR._serialized_start=126
  _VECTOR._serialized_end=148
  _UPSERTPOINTS._serialized_start=150
  _UPSERTPOINTS._serialized_end=254
  _DELETEPOINTS._serialized_start=256
  _DELETEPOINTS._serialized_end=363
  _GETPOINTS._serialized_start=366
  _GETPOINTS._serialized_end=562
  _SETPAYLOADPOINTS._serialized_start=565
  _SETPAYLOADPOINTS._serialized_end=788
  _SETPAYLOADPOINTS_PAYLOADENTRY._serialized_start=718
  _SETPAYLOADPOINTS_PAYLOADENTRY._serialized_end=779
  _DELETEPAYLOADPOINTS._serialized_start=790
  _DELETEPAYLOADPOINTS._serialized_end=911
  _CLEARPAYLOADPOINTS._serialized_start=913
  _CLEARPAYLOADPOINTS._serialized_end=1026
  _CREATEFIELDINDEXCOLLECTION._serialized_start=1029
  _CREATEFIELDINDEXCOLLECTION._serialized_end=1273
  _DELETEFIELDINDEXCOLLECTION._serialized_start=1275
  _DELETEFIELDINDEXCOLLECTION._serialized_end=1376
  _PAYLOADINCLUDESELECTOR._serialized_start=1378
  _PAYLOADINCLUDESELECTOR._serialized_end=1418
  _PAYLOADEXCLUDESELECTOR._serialized_start=1420
  _PAYLOADEXCLUDESELECTOR._serialized_end=1460
  _WITHPAYLOADSELECTOR._serialized_start=1463
  _WITHPAYLOADSELECTOR._serialized_end=1624
  _NAMEDVECTORS._serialized_start=1627
  _NAMEDVECTORS._serialized_end=1757
  _NAMEDVECTORS_VECTORSENTRY._serialized_start=1695
  _NAMEDVECTORS_VECTORSENTRY._serialized_end=1757
  _VECTORS._serialized_start=1759
  _VECTORS._serialized_end=1862
  _VECTORSSELECTOR._serialized_start=1864
  _VECTORSSELECTOR._serialized_end=1896
  _WITHVECTORSSELECTOR._serialized_start=1898
  _WITHVECTORSSELECTOR._serialized_end=2001
  _SEARCHPARAMS._serialized_start=2003
  _SEARCHPARAMS._serialized_end=2081
  _SEARCHPOINTS._serialized_start=2084
  _SEARCHPOINTS._serialized_end=2478
  _SEARCHBATCHPOINTS._serialized_start=2480
  _SEARCHBATCHPOINTS._serialized_end=2569
  _SCROLLPOINTS._serialized_start=2572
  _SCROLLPOINTS._serialized_end=2852
  _RECOMMENDPOINTS._serialized_start=2855
  _RECOMMENDPOINTS._serialized_end=3294
  _RECOMMENDBATCHPOINTS._serialized_start=3296
  _RECOMMENDBATCHPOINTS._serialized_end=3394
  _COUNTPOINTS._serialized_start=3396
  _COUNTPOINTS._serialized_end=3496
  _POINTSOPERATIONRESPONSE._serialized_start=3498
  _POINTSOPERATIONRESPONSE._serialized_end=3575
  _UPDATERESULT._serialized_start=3577
  _UPDATERESULT._serialized_end=3651
  _SCOREDPOINT._serialized_start=3654
  _SCOREDPOINT._serialized_end=3899
  _SCOREDPOINT_PAYLOADENTRY._serialized_start=718
  _SCOREDPOINT_PAYLOADENTRY._serialized_end=779
  _SEARCHRESPONSE._serialized_start=3901
  _SEARCHRESPONSE._serialized_end=3968
  _BATCHRESULT._serialized_start=3970
  _BATCHRESULT._serialized_end=4020
  _SEARCHBATCHRESPONSE._serialized_start=4022
  _SEARCHBATCHRESPONSE._serialized_end=4094
  _COUNTRESPONSE._serialized_start=4096
  _COUNTRESPONSE._serialized_end=4162
  _SCROLLRESPONSE._serialized_start=4165
  _SCROLLRESPONSE._serialized_end=4304
  _COUNTRESULT._serialized_start=4306
  _COUNTRESULT._serialized_end=4334
  _RETRIEVEDPOINT._serialized_start=4337
  _RETRIEVEDPOINT._serialized_end=4556
  _RETRIEVEDPOINT_PAYLOADENTRY._serialized_start=718
  _RETRIEVEDPOINT_PAYLOADENTRY._serialized_end=779
  _GETRESPONSE._serialized_start=4558
  _GETRESPONSE._serialized_end=4625
  _RECOMMENDRESPONSE._serialized_start=4627
  _RECOMMENDRESPONSE._serialized_end=4697
  _RECOMMENDBATCHRESPONSE._serialized_start=4699
  _RECOMMENDBATCHRESPONSE._serialized_end=4774
  _FILTER._serialized_start=4776
  _FILTER._serialized_end=4889
  _CONDITION._serialized_start=4892
  _CONDITION._serialized_end=5086
  _ISEMPTYCONDITION._serialized_start=5088
  _ISEMPTYCONDITION._serialized_end=5119
  _HASIDCONDITION._serialized_start=5121
  _HASIDCONDITION._serialized_end=5170
  _FIELDCONDITION._serialized_start=5173
  _FIELDCONDITION._serialized_end=5394
  _MATCH._serialized_start=5396
  _MATCH._serialized_end=5491
  _RANGE._serialized_start=5493
  _RANGE._serialized_end=5600
  _GEOBOUNDINGBOX._serialized_start=5602
  _GEOBOUNDINGBOX._serialized_end=5694
  _GEORADIUS._serialized_start=5696
  _GEORADIUS._serialized_end=5757
  _VALUESCOUNT._serialized_start=5759
  _VALUESCOUNT._serialized_end=5872
  _POINTSSELECTOR._serialized_start=5874
  _POINTSSELECTOR._serialized_end=5991
  _POINTSIDSLIST._serialized_start=5993
  _POINTSIDSLIST._serialized_end=6038
  _POINTSTRUCT._serialized_start=6041
  _POINTSTRUCT._serialized_end=6254
  _POINTSTRUCT_PAYLOADENTRY._serialized_start=718
  _POINTSTRUCT_PAYLOADENTRY._serialized_end=779
  _GEOPOINT._serialized_start=6256
  _GEOPOINT._serialized_end=6292
# @@protoc_insertion_point(module_scope)
