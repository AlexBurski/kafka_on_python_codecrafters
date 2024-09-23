import socket  # noqa: F401
import struct


def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    server = socket.create_server(("localhost", 9092), reuse_port=True)

    while True:
        print("Server is listening on localhost:9092...")
        client_socket, address = server.accept()
        print(f"Accepted connection from {address}")
        try:
            # Receive the client request, we to receive it to not get an error
            client_request = client_socket.recv(1024)
            print(f"Client request: {client_request}")

            # Construct the response
            # First 4 bytes: message length (8 bytes total)
            message_length = struct.pack(">I", 8)  # '>I' means big-endian unsigned int

            # Next 4 bytes: correlation ID (7)
            correlation_id = struct.pack(">I", 7)

            response = message_length + correlation_id
            print(f"Sending response: {response.hex()}")  # hex() for nicer printing

            # Send the response
            client_socket.sendall(response)
            print("Sent response")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            client_socket.close()
            print(f"Connection with {address} closed\n")


if __name__ == "__main__":
    main()
