# Initial code by Jashandeep Sohi (2013, jashandeep.s.sohi@gmail.com)
# adapted by Marco Job (2019, marco.job@bluewin.ch)

from libc.stdint cimport uint16_t

cdef extern from "c_crc.h":
    uint16_t crc16(const void*, size_t, uint16_t)
