'''
File: PKT_tests.py
Purpose: Provide unit tests to test the RMAP packet creation functions
Author: Alexander Clark
'''
# System imports
import unittest
import sys

# Local imports
sys.path.insert(0, '../SPW_RMAP/')
import RMAP_PKT


class TestPKTMethods(unittest.TestCase):

  def test_pkt_1(self):
    # Expected values
    expected_data = bytearray([0xDE, 0xAD, 0xBE, 0xEF])
    expected_dst_logical = 0x20

    # Create data stream and get CRC
    data_array = [
      0x20, 0x01, 0x60, 0x56,
      0x21, 0x60, 0x70, 0x00,
      0x80, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x04, 0x00,
      0xDE, 0xAD, 0xBE, 0xEF,
      0x00,
    ]
    data_stream = bytearray(data_array)
    # Use a bytearray to create the packet
    packet = RMAP_PKT.RMAP_PKT(data_stream)

    # Compare results
    self.assertEqual(packet.data, expected_data)
    self.assertEqual(packet.dest_logical_addr, expected_dst_logical)
  # End test_pkt_1


  def test_pkt_2(self):
    # Expected values
    expected_data = bytearray([0xDE, 0xAD, 0xBE, 0xEF])
    expected_dst_logical = 0x20

    # Create data stream and get CRC
    data_array = [
      0x20, 0x01, 0x60, 0x56,
      0x21, 0x60, 0x70, 0x00,
      0x80, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x04, 0x00,
      0xDE, 0xAD, 0xBE, 0xEF,
      0x00,
    ]
    # Use a list of bytes to create the packet
    packet = RMAP_PKT.RMAP_PKT(data_array)

    # Compare results
    self.assertEqual(packet.data, expected_data)
    self.assertEqual(packet.dest_logical_addr, expected_dst_logical)
  # End test_pkt_2


  def test_pkt_3(self):
    # Expected values
    expected_data = bytearray([0xDE, 0xAD, 0xBE, 0xEF])
    expected_dst_logical = 0x20

    # Create data stream and get CRC
    data_array = [
      0x20, 0x01, 0x60, 0x56,
      0x21, 0x60, 0x70, 0x00,
      0x80, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x04, 0x00,
      0xDE, 0xAD, 0xBE, 0xEF,
      0x00,
    ]
    data_stream = bytearray(data_array)
    # Use a bytearray to create the packet
    packet = RMAP_PKT.RMAP_PKT(data_stream)

    # Compare results to ensure packet parsed
    self.assertEqual(packet.data, expected_data)
    self.assertEqual(packet.dest_logical_addr, expected_dst_logical)
  
    # Encode the packet to make sure it matches 
    encoded_packet = packet.encode()

    # Compare encoding results
    self.assertEqual(encoded_packet, data_stream)
  # End encode_test


if __name__ == '__main__':
  unittest.main()