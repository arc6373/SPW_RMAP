'''
File: PKT_RSP_tests.py
Purpose: Provide unit tests to test the RMAP response packet creation functions
Author: Alexander Clark
'''
# System imports
import unittest
import sys

# Local imports
sys.path.insert(0, '../SPW_RMAP/')
import RMAP_PKT
import RMAP


class TestPKTMethods(unittest.TestCase):

  def test_pkt_1(self):
    # This test will test creation of write reply packets
    # Ensures that added response data is not used
    # Expected values
    expected_data = bytearray([
      0x21, 0x01, 0x20, 0x00,
      0x20, 0x60, 0x70, 0xC6
    ])

    # Create data stream
    data_array = [
      0x20, 0x01, 0x60, 0x56,
      0x21, 0x60, 0x70, 0x00,
      0x80, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x04, 0x00,
      0xDE, 0xAD, 0xBE, 0xEF,
      0x00,
    ]
    # Use a bytearray to create the packet
    packet = RMAP_PKT.RMAP_PKT(data_array)

    # Add response data to the packet
    response_data = [0xF0, 0x0D, 0xCA, 0xFE]
    packet.add_response_data(response_data)

    # Build the response packet
    response_packet = packet.build_reply(RMAP.ERR_NO_ERROR)

    # Compare results
    self.assertEqual(response_packet, expected_data)

  # End test_pkt_1


if __name__ == '__main__':
  unittest.main()