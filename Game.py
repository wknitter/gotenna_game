from connection.Connection import ConnectionManager


def on_incoming_message(message):
    print(message)


connection = ConnectionManager(on_incoming_message)
