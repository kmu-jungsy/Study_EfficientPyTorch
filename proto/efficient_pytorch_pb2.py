# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: efficient_pytorch.proto

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
  name='efficient_pytorch.proto',
  package='efficient_pytorch',
  serialized_pb=_b('\n\x17\x65\x66\x66icient_pytorch.proto\x12\x11\x65\x66\x66icient_pytorch\"\x8e\x08\n\nHyperParam\x12\x37\n\tmain_file\x18\x01 \x01(\t:$examples/classifier_imagenet/main.py\x12\x15\n\x04\x61rch\x18\x02 \x01(\t:\x07\x61lexnet\x12?\n\x0cmodel_source\x18\x03 \x01(\x0e\x32).efficient_pytorch.HyperParam.ModelSource\x12\x1a\n\x08log_name\x18\x04 \x01(\t:\x08template\x12\x0c\n\x04\x64\x61ta\x18\x05 \x02(\t\x12\r\n\x05\x64\x65\x62ug\x18\x06 \x01(\x08\x12\x14\n\x0coverfit_test\x18\x07 \x01(\x08\x12\x0f\n\x02lr\x18\n \x01(\x02:\x03\x30.1\x12\x12\n\x06\x65pochs\x18\x0b \x01(\x05:\x02\x39\x30\x12\x17\n\nbatch_size\x18\x0c \x01(\x05:\x03\x32\x35\x36\x12\x12\n\x07workers\x18\r \x01(\x05:\x01\x34\x12\x16\n\nprint_freq\x18\x0e \x01(\x05:\x02\x35\x30\x12\x10\n\x08\x65valuate\x18\x0f \x01(\x08\x12\x12\n\npretrained\x18\x10 \x01(\x08\x12\x0c\n\x04seed\x18\x11 \x01(\x05\x12\x13\n\x0b\x65xport_onnx\x18\x12 \x01(\x08\x12\x0e\n\x06resume\x18\x13 \x01(\t\x12\x0e\n\x06weight\x18\x16 \x01(\t\x12&\n\x06gpu_id\x18\x14 \x01(\x0e\x32\x16.efficient_pytorch.GPU\x12.\n\tmulti_gpu\x18\x15 \x01(\x0b\x32\x1b.efficient_pytorch.MultiGPU\x12\'\n\x05qmode\x18\x32 \x01(\x0e\x32\x18.efficient_pytorch.Qmode\x12)\n\x06warmup\x18\x63 \x01(\x0b\x32\x19.efficient_pytorch.Warmup\x12\x37\n\x0clr_scheduler\x18\x64 \x01(\x0e\x32!.efficient_pytorch.LRScheduleType\x12/\n\x07step_lr\x18\x65 \x01(\x0b\x32\x1e.efficient_pytorch.StepLRParam\x12:\n\rmulti_step_lr\x18\x66 \x01(\x0b\x32#.efficient_pytorch.MultiStepLRParam\x12\x33\n\tcyclic_lr\x18g \x01(\x0b\x32 .efficient_pytorch.CyclicLRParam\x12\x34\n\toptimizer\x18\xc8\x01 \x01(\x0e\x32 .efficient_pytorch.OptimizerType\x12)\n\x03sgd\x18\xc9\x01 \x01(\x0b\x32\x1b.efficient_pytorch.SGDParam\x12+\n\x04\x61\x64\x61m\x18\xca\x01 \x01(\x0b\x32\x1c.efficient_pytorch.AdamParam\"8\n\x0bModelSource\x12\x0f\n\x0bTorchVision\x10\x01\x12\r\n\tPyTorchCV\x10\x02\x12\t\n\x05Local\x10\x03\"\x9d\x01\n\x08MultiGPU\x12\x16\n\nworld_size\x18\x01 \x01(\x05:\x02-1\x12\x0f\n\x04rank\x18\x02 \x01(\x05:\x01\x30\x12\'\n\x08\x64ist_url\x18\x03 \x01(\t:\x15tcp://127.0.0.1:23456\x12\x1a\n\x0c\x64ist_backend\x18\x04 \x01(\t:\x04nccl\x12#\n\x1bmultiprocessing_distributed\x18\x05 \x01(\x08\"?\n\x08SGDParam\x12\x1c\n\x0cweight_decay\x18\x01 \x01(\x02:\x06\x30.0001\x12\x15\n\x08momentum\x18\x02 \x01(\x02:\x03\x30.9\")\n\tAdamParam\x12\x1c\n\x0cweight_decay\x18\x01 \x01(\x02:\x06\x30.0001\"4\n\x06Warmup\x12\x12\n\x06\x65pochs\x18\x01 \x01(\x05:\x02\x31\x30\x12\x16\n\nmultiplier\x18\x02 \x01(\x02:\x02\x31\x30\"8\n\x0bStepLRParam\x12\x15\n\tstep_size\x18\x03 \x01(\x05:\x02\x32\x30\x12\x12\n\x05gamma\x18\x04 \x01(\x02:\x03\x30.1\":\n\x10MultiStepLRParam\x12\x12\n\nmilestones\x18\x03 \x03(\x05\x12\x12\n\x05gamma\x18\x04 \x01(\x02:\x03\x30.1\"\xe3\x01\n\rCyclicLRParam\x12\x0f\n\x07\x62\x61se_lr\x18\x01 \x01(\x02\x12\x0e\n\x06max_lr\x18\x02 \x01(\x02\x12\x1a\n\x0cstep_size_up\x18\x03 \x01(\x05:\x04\x32\x30\x30\x30\x12\x16\n\x0estep_size_down\x18\x04 \x01(\x05\x12\x33\n\x04mode\x18\x05 \x01(\x0e\x32%.efficient_pytorch.CyclicLRParam.Mode\x12\x10\n\x05gamma\x18\x06 \x01(\x02:\x01\x31\"6\n\x04Mode\x12\x0e\n\ntriangular\x10\x01\x12\x0f\n\x0btriangular2\x10\x02\x12\r\n\texp_range\x10\x03*\x18\n\x03GPU\x12\x07\n\x03\x41NY\x10\x01\x12\x08\n\x04NONE\x10\x02*(\n\x05Qmode\x12\x0e\n\nlayer_wise\x10\x01\x12\x0f\n\x0bkernel_wise\x10\x02*:\n\x05Pmode\x12\x0e\n\npixel_wise\x10\x01\x12\x10\n\x0c\x63hannel_wise\x10\x02\x12\x0f\n\x0bpattern_npu\x10\x03*\"\n\rOptimizerType\x12\x07\n\x03SGD\x10\x01\x12\x08\n\x04\x41\x64\x61m\x10\x02*R\n\x0eLRScheduleType\x12\n\n\x06StepLR\x10\x01\x12\x0f\n\x0bMultiStepLR\x10\x02\x12\x15\n\x11\x43osineAnnealingLR\x10\x03\x12\x0c\n\x08\x43yclicLR\x10\x04')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_GPU = _descriptor.EnumDescriptor(
  name='GPU',
  full_name='efficient_pytorch.GPU',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ANY', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NONE', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1757,
  serialized_end=1781,
)
_sym_db.RegisterEnumDescriptor(_GPU)

GPU = enum_type_wrapper.EnumTypeWrapper(_GPU)
_QMODE = _descriptor.EnumDescriptor(
  name='Qmode',
  full_name='efficient_pytorch.Qmode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='layer_wise', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kernel_wise', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1783,
  serialized_end=1823,
)
_sym_db.RegisterEnumDescriptor(_QMODE)

Qmode = enum_type_wrapper.EnumTypeWrapper(_QMODE)
_PMODE = _descriptor.EnumDescriptor(
  name='Pmode',
  full_name='efficient_pytorch.Pmode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='pixel_wise', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='channel_wise', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='pattern_npu', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1825,
  serialized_end=1883,
)
_sym_db.RegisterEnumDescriptor(_PMODE)

Pmode = enum_type_wrapper.EnumTypeWrapper(_PMODE)
_OPTIMIZERTYPE = _descriptor.EnumDescriptor(
  name='OptimizerType',
  full_name='efficient_pytorch.OptimizerType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SGD', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Adam', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1885,
  serialized_end=1919,
)
_sym_db.RegisterEnumDescriptor(_OPTIMIZERTYPE)

OptimizerType = enum_type_wrapper.EnumTypeWrapper(_OPTIMIZERTYPE)
_LRSCHEDULETYPE = _descriptor.EnumDescriptor(
  name='LRScheduleType',
  full_name='efficient_pytorch.LRScheduleType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='StepLR', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MultiStepLR', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CosineAnnealingLR', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CyclicLR', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1921,
  serialized_end=2003,
)
_sym_db.RegisterEnumDescriptor(_LRSCHEDULETYPE)

LRScheduleType = enum_type_wrapper.EnumTypeWrapper(_LRSCHEDULETYPE)
ANY = 1
NONE = 2
layer_wise = 1
kernel_wise = 2
pixel_wise = 1
channel_wise = 2
pattern_npu = 3
SGD = 1
Adam = 2
StepLR = 1
MultiStepLR = 2
CosineAnnealingLR = 3
CyclicLR = 4


_HYPERPARAM_MODELSOURCE = _descriptor.EnumDescriptor(
  name='ModelSource',
  full_name='efficient_pytorch.HyperParam.ModelSource',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TorchVision', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PyTorchCV', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Local', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1029,
  serialized_end=1085,
)
_sym_db.RegisterEnumDescriptor(_HYPERPARAM_MODELSOURCE)

_CYCLICLRPARAM_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='efficient_pytorch.CyclicLRParam.Mode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='triangular', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='triangular2', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='exp_range', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1701,
  serialized_end=1755,
)
_sym_db.RegisterEnumDescriptor(_CYCLICLRPARAM_MODE)


_HYPERPARAM = _descriptor.Descriptor(
  name='HyperParam',
  full_name='efficient_pytorch.HyperParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='main_file', full_name='efficient_pytorch.HyperParam.main_file', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("examples/classifier_imagenet/main.py").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='arch', full_name='efficient_pytorch.HyperParam.arch', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("alexnet").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='model_source', full_name='efficient_pytorch.HyperParam.model_source', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='log_name', full_name='efficient_pytorch.HyperParam.log_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("template").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='efficient_pytorch.HyperParam.data', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='debug', full_name='efficient_pytorch.HyperParam.debug', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='overfit_test', full_name='efficient_pytorch.HyperParam.overfit_test', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lr', full_name='efficient_pytorch.HyperParam.lr', index=7,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='epochs', full_name='efficient_pytorch.HyperParam.epochs', index=8,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=90,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='efficient_pytorch.HyperParam.batch_size', index=9,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=256,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='workers', full_name='efficient_pytorch.HyperParam.workers', index=10,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=4,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='print_freq', full_name='efficient_pytorch.HyperParam.print_freq', index=11,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=50,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evaluate', full_name='efficient_pytorch.HyperParam.evaluate', index=12,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pretrained', full_name='efficient_pytorch.HyperParam.pretrained', index=13,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seed', full_name='efficient_pytorch.HyperParam.seed', index=14,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='export_onnx', full_name='efficient_pytorch.HyperParam.export_onnx', index=15,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resume', full_name='efficient_pytorch.HyperParam.resume', index=16,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight', full_name='efficient_pytorch.HyperParam.weight', index=17,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gpu_id', full_name='efficient_pytorch.HyperParam.gpu_id', index=18,
      number=20, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='multi_gpu', full_name='efficient_pytorch.HyperParam.multi_gpu', index=19,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='qmode', full_name='efficient_pytorch.HyperParam.qmode', index=20,
      number=50, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='warmup', full_name='efficient_pytorch.HyperParam.warmup', index=21,
      number=99, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lr_scheduler', full_name='efficient_pytorch.HyperParam.lr_scheduler', index=22,
      number=100, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='step_lr', full_name='efficient_pytorch.HyperParam.step_lr', index=23,
      number=101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='multi_step_lr', full_name='efficient_pytorch.HyperParam.multi_step_lr', index=24,
      number=102, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cyclic_lr', full_name='efficient_pytorch.HyperParam.cyclic_lr', index=25,
      number=103, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='optimizer', full_name='efficient_pytorch.HyperParam.optimizer', index=26,
      number=200, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sgd', full_name='efficient_pytorch.HyperParam.sgd', index=27,
      number=201, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='adam', full_name='efficient_pytorch.HyperParam.adam', index=28,
      number=202, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HYPERPARAM_MODELSOURCE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=1085,
)


_MULTIGPU = _descriptor.Descriptor(
  name='MultiGPU',
  full_name='efficient_pytorch.MultiGPU',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='world_size', full_name='efficient_pytorch.MultiGPU.world_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rank', full_name='efficient_pytorch.MultiGPU.rank', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dist_url', full_name='efficient_pytorch.MultiGPU.dist_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("tcp://127.0.0.1:23456").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dist_backend', full_name='efficient_pytorch.MultiGPU.dist_backend', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("nccl").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='multiprocessing_distributed', full_name='efficient_pytorch.MultiGPU.multiprocessing_distributed', index=4,
      number=5, type=8, cpp_type=7, label=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1088,
  serialized_end=1245,
)


_SGDPARAM = _descriptor.Descriptor(
  name='SGDParam',
  full_name='efficient_pytorch.SGDParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weight_decay', full_name='efficient_pytorch.SGDParam.weight_decay', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.0001,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='momentum', full_name='efficient_pytorch.SGDParam.momentum', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.9,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1247,
  serialized_end=1310,
)


_ADAMPARAM = _descriptor.Descriptor(
  name='AdamParam',
  full_name='efficient_pytorch.AdamParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weight_decay', full_name='efficient_pytorch.AdamParam.weight_decay', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.0001,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1312,
  serialized_end=1353,
)


_WARMUP = _descriptor.Descriptor(
  name='Warmup',
  full_name='efficient_pytorch.Warmup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='epochs', full_name='efficient_pytorch.Warmup.epochs', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=10,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='multiplier', full_name='efficient_pytorch.Warmup.multiplier', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=10,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1355,
  serialized_end=1407,
)


_STEPLRPARAM = _descriptor.Descriptor(
  name='StepLRParam',
  full_name='efficient_pytorch.StepLRParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='step_size', full_name='efficient_pytorch.StepLRParam.step_size', index=0,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=20,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gamma', full_name='efficient_pytorch.StepLRParam.gamma', index=1,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1409,
  serialized_end=1465,
)


_MULTISTEPLRPARAM = _descriptor.Descriptor(
  name='MultiStepLRParam',
  full_name='efficient_pytorch.MultiStepLRParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='milestones', full_name='efficient_pytorch.MultiStepLRParam.milestones', index=0,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gamma', full_name='efficient_pytorch.MultiStepLRParam.gamma', index=1,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1467,
  serialized_end=1525,
)


_CYCLICLRPARAM = _descriptor.Descriptor(
  name='CyclicLRParam',
  full_name='efficient_pytorch.CyclicLRParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_lr', full_name='efficient_pytorch.CyclicLRParam.base_lr', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_lr', full_name='efficient_pytorch.CyclicLRParam.max_lr', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='step_size_up', full_name='efficient_pytorch.CyclicLRParam.step_size_up', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=2000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='step_size_down', full_name='efficient_pytorch.CyclicLRParam.step_size_down', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mode', full_name='efficient_pytorch.CyclicLRParam.mode', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gamma', full_name='efficient_pytorch.CyclicLRParam.gamma', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CYCLICLRPARAM_MODE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1528,
  serialized_end=1755,
)

_HYPERPARAM.fields_by_name['model_source'].enum_type = _HYPERPARAM_MODELSOURCE
_HYPERPARAM.fields_by_name['gpu_id'].enum_type = _GPU
_HYPERPARAM.fields_by_name['multi_gpu'].message_type = _MULTIGPU
_HYPERPARAM.fields_by_name['qmode'].enum_type = _QMODE
_HYPERPARAM.fields_by_name['warmup'].message_type = _WARMUP
_HYPERPARAM.fields_by_name['lr_scheduler'].enum_type = _LRSCHEDULETYPE
_HYPERPARAM.fields_by_name['step_lr'].message_type = _STEPLRPARAM
_HYPERPARAM.fields_by_name['multi_step_lr'].message_type = _MULTISTEPLRPARAM
_HYPERPARAM.fields_by_name['cyclic_lr'].message_type = _CYCLICLRPARAM
_HYPERPARAM.fields_by_name['optimizer'].enum_type = _OPTIMIZERTYPE
_HYPERPARAM.fields_by_name['sgd'].message_type = _SGDPARAM
_HYPERPARAM.fields_by_name['adam'].message_type = _ADAMPARAM
_HYPERPARAM_MODELSOURCE.containing_type = _HYPERPARAM
_CYCLICLRPARAM.fields_by_name['mode'].enum_type = _CYCLICLRPARAM_MODE
_CYCLICLRPARAM_MODE.containing_type = _CYCLICLRPARAM
DESCRIPTOR.message_types_by_name['HyperParam'] = _HYPERPARAM
DESCRIPTOR.message_types_by_name['MultiGPU'] = _MULTIGPU
DESCRIPTOR.message_types_by_name['SGDParam'] = _SGDPARAM
DESCRIPTOR.message_types_by_name['AdamParam'] = _ADAMPARAM
DESCRIPTOR.message_types_by_name['Warmup'] = _WARMUP
DESCRIPTOR.message_types_by_name['StepLRParam'] = _STEPLRPARAM
DESCRIPTOR.message_types_by_name['MultiStepLRParam'] = _MULTISTEPLRPARAM
DESCRIPTOR.message_types_by_name['CyclicLRParam'] = _CYCLICLRPARAM
DESCRIPTOR.enum_types_by_name['GPU'] = _GPU
DESCRIPTOR.enum_types_by_name['Qmode'] = _QMODE
DESCRIPTOR.enum_types_by_name['Pmode'] = _PMODE
DESCRIPTOR.enum_types_by_name['OptimizerType'] = _OPTIMIZERTYPE
DESCRIPTOR.enum_types_by_name['LRScheduleType'] = _LRSCHEDULETYPE

HyperParam = _reflection.GeneratedProtocolMessageType('HyperParam', (_message.Message,), dict(
  DESCRIPTOR = _HYPERPARAM,
  __module__ = 'efficient_pytorch_pb2'
  # @@protoc_insertion_point(class_scope:efficient_pytorch.HyperParam)
  ))
_sym_db.RegisterMessage(HyperParam)

MultiGPU = _reflection.GeneratedProtocolMessageType('MultiGPU', (_message.Message,), dict(
  DESCRIPTOR = _MULTIGPU,
  __module__ = 'efficient_pytorch_pb2'
  # @@protoc_insertion_point(class_scope:efficient_pytorch.MultiGPU)
  ))
_sym_db.RegisterMessage(MultiGPU)

SGDParam = _reflection.GeneratedProtocolMessageType('SGDParam', (_message.Message,), dict(
  DESCRIPTOR = _SGDPARAM,
  __module__ = 'efficient_pytorch_pb2'
  # @@protoc_insertion_point(class_scope:efficient_pytorch.SGDParam)
  ))
_sym_db.RegisterMessage(SGDParam)

AdamParam = _reflection.GeneratedProtocolMessageType('AdamParam', (_message.Message,), dict(
  DESCRIPTOR = _ADAMPARAM,
  __module__ = 'efficient_pytorch_pb2'
  # @@protoc_insertion_point(class_scope:efficient_pytorch.AdamParam)
  ))
_sym_db.RegisterMessage(AdamParam)

Warmup = _reflection.GeneratedProtocolMessageType('Warmup', (_message.Message,), dict(
  DESCRIPTOR = _WARMUP,
  __module__ = 'efficient_pytorch_pb2'
  # @@protoc_insertion_point(class_scope:efficient_pytorch.Warmup)
  ))
_sym_db.RegisterMessage(Warmup)

StepLRParam = _reflection.GeneratedProtocolMessageType('StepLRParam', (_message.Message,), dict(
  DESCRIPTOR = _STEPLRPARAM,
  __module__ = 'efficient_pytorch_pb2'
  # @@protoc_insertion_point(class_scope:efficient_pytorch.StepLRParam)
  ))
_sym_db.RegisterMessage(StepLRParam)

MultiStepLRParam = _reflection.GeneratedProtocolMessageType('MultiStepLRParam', (_message.Message,), dict(
  DESCRIPTOR = _MULTISTEPLRPARAM,
  __module__ = 'efficient_pytorch_pb2'
  # @@protoc_insertion_point(class_scope:efficient_pytorch.MultiStepLRParam)
  ))
_sym_db.RegisterMessage(MultiStepLRParam)

CyclicLRParam = _reflection.GeneratedProtocolMessageType('CyclicLRParam', (_message.Message,), dict(
  DESCRIPTOR = _CYCLICLRPARAM,
  __module__ = 'efficient_pytorch_pb2'
  # @@protoc_insertion_point(class_scope:efficient_pytorch.CyclicLRParam)
  ))
_sym_db.RegisterMessage(CyclicLRParam)


# @@protoc_insertion_point(module_scope)
