import time

class SMS_store:
    """ store SMS messages"""

    def __init__(self):
        """ create a list for storing messages."""
        self.store = []

    def __str__(self):
        return ('{0}'.format(self.store))

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS, has_been_viewed = False):
        """ append a message to SMS_store object (which is a list).
        Each message is a tuple of 4 elements. """
        self.store.append((has_been_viewed, from_number, time_arrived, text_of_SMS))

    def message_count(self):
        """ return the number of messages in a SMS_store object."""
        return len(self.store)

    def get_unread_indexes(self):
        """ return a list of indexes of unread messages in a SMS_store object."""
        list_index_unread = []
        for (index, message) in enumerate (self.store):
            if message[0] == False:
                list_index_unread.append(index)
        return list_index_unread

    def get_message(self, i):
        """ get the from_number, time_arrived, text_of_SMS of the message at index i.
        change its has_been_viewed status to True."""
        try:
            self.store[i] = (True, self.store[i][1], self.store[i][2], self.store[i][3])
            return self.store[i][1:4]
        except:
            return None

    def delete(self, i):
        """ delete the messsage at index i."""
        del self.store[i]

    def clear(self):
        """ delete all messages from SMS_store object. """
        self.store.clear()

my_inbox = SMS_store()
my_inbox.add_new_arrival('25642599', '09:00','time to school')
my_inbox.add_new_arrival('33333333', '09:00','time to bed')
print(my_inbox)
print('Number of messages: ', my_inbox.message_count())
print('List of indexes of unread messages: ', my_inbox.get_unread_indexes())
print('Get message 1: ', my_inbox.get_message(0))
print('List of indexes of unread messages: ', my_inbox.get_unread_indexes())
my_inbox.delete(0)
print(my_inbox)
my_inbox.clear()
print('Inbox after clear: ', my_inbox)
