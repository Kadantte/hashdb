#!/usr/bin/env python

DESCRIPTION = "ROL 6 and ADD and SUB 0x20"
TYPE = 'unsigned_int'
TEST_1 = 650671921


def hash(data):
    val = 0
    for i in data:
        val = ((val << 6) | (val >> 26)) & 0xffffffff
        val += i if i < 97 else i - 32
        val &= 0xffffffff
    return val
