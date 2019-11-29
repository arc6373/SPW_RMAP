'''
File: RMAP_PKT.py
Purpose: Define an RMAP packet that contains all needed information.
Author: Alexander Clark

Note: All information came from spacewire manual on RMAP
'''
# System imports
# None

# Local imports
import RMAP


class RMAP_PKT:

  def __init__(self, rmap_cmd=None):
    # This will consist of a bytestream that contains the path
    self.dest_path_addr = bytearray()
    # This will contain a byte representing the dst device ID
    self.dest_logical_addr = None
    # This will consist of a bytestream that contains the path
    self.src_path_addr = bytearray()
    # This will contain a byte representing the src device ID
    self.src_logical_addr = None
    # Protocol ID for RMAP should be 1
    self.protocol_id = None
    # Packet type - the type of packet it is
    self.packet_type = None
    # Command - the RMAP command to execute
    self.command = None
    # Src Address Length - the length of the source address path if it used
    # It will be set to 0 if it is unused (logical pathing is used instead)
    self.src_addr_len = None
    # Destination key - key used to verify command went to the correct location before using
    self.dest_key = None
    # transaction id - Used to identify command, response, and ack transactions
    self.transation_id = None
    # extended address - Extra 8 bits to support terabyte address - if unused should be 0
    self.extended_addr = None
    # Memory address - 32 lower bits of a memory address to read/write data from/to
    self.mem_addr = None
    # data length - the length of the data that follows in the bytestream
    self.data_len = None
    # Header CRC - The CRC of the data from the dest_logical_addr to the data_len
    self.header_crc = None
    # Data - The data in the command
    self.data = None
    # Data CRC - The CRC of the data that will need to validated
    self.data_crc = None

    # Parse the components out
    if (rmap_cmd is not None):  
      self.decode(rmap_cmd)
  # End __init__


  def decode(self, rmap_cmd):
    # rmap_cmd should be a bytearray or a list of data
    # Create a copy of the bytestream to not destroy it
    rmap_cmd_copy = bytearray(len(rmap_cmd))
    rmap_cmd_copy[:] = rmap_cmd

    # Get the first byte to test if it is path address
    first_byte = rmap_cmd_copy[0]

    while (first_byte < RMAP.LOGICAL_ADDR_MIN):
      # Path address is present and should be processed
      # Remove the path addressing byte from the byte stream
      popped_byte = rmap_cmd_copy.pop(0)

      # Store the byte in the dest path addr
      self.dest_path_addr.extend(popped_byte.to_bytes(length=1, byteorder='big'))

      first_byte = rmap_cmd_copy[0]

    # End while statement

    # The path addressing should be pulled off and 
    # the dst logical address is at the start of the bytestream
    # Store the dst logical bytes
    self.dest_logical_addr = rmap_cmd_copy.pop(0)

    # Protocol ID is now at the front
    # Packet Type, Command, Source Path Addr Len is at the front
    byte_to_parse = rmap_cmd_copy.pop(0)
    # This byte has the format as follows
    # Bit 7 - Reserved
    # Bit 6 - Command = 1
    # Bit 5 - Write = 1, Read = 0
    # Bit 4 - Verify data = 1, dont verify = 0
    # Bit 3 - Ack = 1, no ack = 0
    # Bit 2 - Increment = 1, no inc = 0
    # Bit 1-0 - Source path Address Len

    # Parse out the packet type, command, and source path address length
    packet_type = (byte_to_parse & 0xC0) >> 6
    command = (byte_to_parse & 0x3C) >> 2
    source_packet_length = (byte_to_parse & 0x3)

    # Store the parsed variables
    self.packet_type = packet_type
    self.command = command
    self.source_packet_length = source_packet_length

    # Desination key is now at the front
    # Store the destination id byte
    self.dest_key = rmap_cmd_copy.pop(0)

    # If source packet length is not 0, we need to process the source path address
    if (self.source_packet_length != 0):
      # Process source packet length
      self.src_path_addr = rmap_cmd_copy[0:self.source_packet_length]

      # Pop the bytes that are being used
      rmap_cmd_copy = rmap_cmd_copy[self.source_packet_length:]

    # Source logical address is now at the front
    # Store the source logical address byte
    self.src_logical_addr = rmap_cmd_copy.pop(0)

    # Transaction ID is now at the front (Transaction id is two bytes)
    transaction_id_bytes = rmap_cmd_copy[0:2]
    # Store the transaction id as an int
    self.transation_id = int.from_bytes(transaction_id_bytes, byteorder='big')

    # Remove the two bytes
    rmap_cmd_copy = rmap_cmd_copy[2:]

    # Extended memory address is now at the front
    # Store the extended memory address
    self.extended_addr = rmap_cmd_copy.pop(0)

    # Memory address is now at the front (Mem addr is 4 bytes)
    memory_address_bytes = rmap_cmd_copy[0:4]
    # Store the memory address as a 32 bit int
    self.mem_addr = int.from_bytes(memory_address_bytes, byteorder='big')
    # Clear the used data
    rmap_cmd_copy = rmap_cmd_copy[4:]

    # Data length is at the front (Data length is 3 bytes)
    data_length_bytes = rmap_cmd_copy[0:3]
    # Store the data length as an int
    self.data_len = int.from_bytes(data_length_bytes, byteorder='big')
    # Clear the used data
    rmap_cmd_copy = rmap_cmd_copy[3:]

    # Header CRC is at the front
    self.header_crc = rmap_cmd_copy.pop(0)

    # Data is now at the front (This can be a variable number of bytes)
    # Copy the data byte array into the data object
    self.data = rmap_cmd_copy[0:self.data_len]
    # Clear the used data
    rmap_cmd_copy = rmap_cmd_copy[self.data_len:]

    # Data CRC should be at the front
    self.data_crc = rmap_cmd_copy.pop(0)

    # Completed parsing the bytestrean
  # end decode

  def encode():
    pass