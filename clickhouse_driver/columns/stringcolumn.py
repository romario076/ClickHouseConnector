
from .. import errors
from ..reader import read_binary_str, read_binary_str_fixed_len
from ..writer import write_binary_str, write_binary_str_fixed_len
from ..util import compat
from .base import CustomItemColumn


class String(CustomItemColumn):
    ch_type = 'String'
    py_types = compat.string_types

    # TODO: pass user encoding here

    def read(self, buf):
        return read_binary_str(buf)

    def _read_null(self, buf):
        self.read(buf)

    def write(self, value, buf):
        write_binary_str(value, buf)

    def _write_null(self, buf):
        self.write('', buf)


class FixedString(String):
    ch_type = 'FixedString'

    def __init__(self, length, **kwargs):
        self.length = length
        super(FixedString, self).__init__(**kwargs)

    def read(self, buf):
        return read_binary_str_fixed_len(buf, self.length).strip('\x00')

    def write(self, value, buf):
        try:
            write_binary_str_fixed_len(value, buf, self.length)
        except ValueError:
            raise errors.TooLargeStringSize()
