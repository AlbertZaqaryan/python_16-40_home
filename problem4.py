# import io

# def get_payments_storage():

#     return open('NUL', 'wb')

# def stream_payments_to_storage(storage):
#     for i in range(10):
#         storage.write(bytes([1, 2, 3, 4, 5]))
#     return storage

# def process_payments():

#     with get_payments_storage() as raw_storage:

#         checksum_storage = io.BufferedWriter(raw_storage)
#         # checksum_storage.write(bytes([1, 2, 3]))
#         stream_payments_to_storage(checksum_storage)

#         print("Checksum of bytes written:", checksum_storage)
# process_payments()


# def process_payments():
#     # Create a subclass of io.BufferedWriter to intercept writes and calculate checksum
#     class ChecksumStorage(io.BufferedWriter):
#         def __init__(self, raw):
#             super().__init__(raw)
#             self.checksum = 0  # Initialize checksum
#         def write(self, b):
#             # Calculate the checksum by summing byte values
#             self.checksum += sum(b)
#             return super().write(b)
#     # Create an instance of the custom storage class
#     with get_payments_storage() as raw_storage:
#         checksum_storage = ChecksumStorage(raw_storage)
#         # Process the payments
#         stream_payments_to_storage(checksum_storage)
#         # Print the calculated checksum after processing
#         print("Checksum of bytes written:", checksum_storage.checksum)
# # Call process_payments to test
# process_payments()