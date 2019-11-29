'''
File: CRC_tests.py
Purpose: Provide unit tests to test the RMAP CRC functions
Author: Alexander Clark
'''
# System imports
import unittest
import sys

# Local imports
sys.path.insert(0, '../SPW_RMAP/')
import RMAP

class TestCRCMethods(unittest.TestCase):

  def test_crc_1(self):
    # Expected values
    expected_crc = 0xB0

    # Create data stream and get CRC
    data_stream = bytearray([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08])
    data_stream_crc = RMAP.calculate_crc(data_stream)

    # Compare results
    self.assertEqual(data_stream_crc, expected_crc)
  # End test_crc_1

  def test_crc_2(self):
    # Expected values
    expected_crc = 0x84

    # Create data stream and get CRC
    data_stream_array = [
      0x53, 0x70, 0x61, 0x63, 0x65, 0x57, 0x69, 0x72,
      0x65, 0x20, 0x69, 0x73, 0x20, 0x62, 0x65, 0x61,
      0x75, 0x74, 0x69, 0x66, 0x75, 0x6C, 0x21, 0x21,
    ]
    data_stream = bytearray(data_stream_array)
    data_stream_crc = RMAP.calculate_crc(data_stream)

    # Compare results
    self.assertEqual(data_stream_crc, expected_crc)
  # End test_crc_2

  def test_crc_3(self):
    # Expected values
    expected_crc = 0x18

    # Create data stream and get CRC
    data_stream_array = [
      0x10, 0x56, 0xC3, 0x95, 0xA5, 0x75, 0x38, 0x63,
      0x2F, 0x86, 0x7B, 0x01, 0x32, 0xDE, 0x35, 0x7A,
    ]
    data_stream = bytearray(data_stream_array)
    data_stream_crc = RMAP.calculate_crc(data_stream)

    # Compare results
    self.assertEqual(data_stream_crc, expected_crc)
  # End test_crc_2

if __name__ == '__main__':
  unittest.main()