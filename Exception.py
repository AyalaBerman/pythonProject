import datetime

class Exceptions:

    def print(self, message):
        name = "Ayala"
        time = datetime.datetime.now().strftime("%d.%m.%y, %H:%M")
        error_message = f"<{name}, {time}> {message} <{name}>"
        print(error_message)