import whatsapp


def main():
    # Create a new instance of the Whatsapp class
    whatsapp = Whatsapp()

    # Connect to WhatsApp
    whatsapp.connect()

    # Get the list of chats
    chats = whatsapp.get_chats()

    # Send a message to the first chat
    whatsapp.send_message(chats[1], "Hello, world!")

    # Close the connection
    whatsapp.close()


if __name__ == "__main__":
    main()
