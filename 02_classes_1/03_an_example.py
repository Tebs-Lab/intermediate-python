# There are MANY patterns to explore with "Object Oriented Programming" and you won't
# see all of them in this class. This example file does contain some common concepts 
# and patterns that you'll see, including:
#    composition (using objects within objects)
#    "state" and "behavior"
#    pythons "magic method" / "dunder method" system

class NewsletterAccount:
    def __init__(self, title, operator_email):
        self.title = title
        self.operator_email = operator_email
        self.mailing_list = []

    
    def register_signup(self, subscriber):
        if not subscriber in self.mailing_list:
            self.mailing_list.append(subscriber)


    def unsubscribe(self, subscriber):
        if subscriber in self.mailing_list:
            self.mailing_list.remove(subscriber)


    def publish(self, email_content):
        for subscriber in self.mailing_list:
            send_email(subscriber.email_address, self.operator_email, email_content)


    def __str__(self):
        return f'Newsletter: {self.title} has {len(self.mailing_list)} subscribers and is sent from {self.operator_email}.'



class NewsletterSubscriber:
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address

    # Two subscribers are the equal if they have the same email address.
    def __eq__(self, other):
        if type(other) == NewsletterSubscriber and other.email_address == self.email_address:
            return True
        
        return False


    def __str__(self):
        return f'NewsletterSubscriber: {self.name}, {self.email_address}'


# Just pretend this actually sends emails...
def send_email(to_address, from_address, content):
    print(f"{content} was sent to {to_address} from {from_address}")


# This is a common pattern in many languages. Main is the "entry point"
# for any given program. It creates a scope to encapsulate variables
# and is generally considered more robust.
def main():
    lab_report = NewsletterAccount('The Lab Report', 'teb@tebs-lab.com')
    print(lab_report)

    pupdate = NewsletterAccount('Pupdates: Whats New With Dogs', 'bingo@weLoveDogs.com')
    print(pupdate)

    buzz = NewsletterSubscriber("Buzz Aldrin", 'moonboy1969@fakemail.com')
    sara = NewsletterSubscriber("Sara Conner", 'robot.hater55@fakemail.com')
    sharif = NewsletterSubscriber("Sharif Sakar", 's.sakar@fakemail.com')
    sakura = NewsletterSubscriber("Sakura Nakamoto", 'cherryblossomgurl89@fakemail.com')
    print(sharif) 

    lab_report.register_signup(buzz)
    lab_report.register_signup(sara)
    print(lab_report)

    pupdate.register_signup(sharif)
    pupdate.register_signup(sakura)
    print(pupdate)

    # We won't "reregister" a member
    lab_report.register_signup(buzz)

    # Explicitly invoking the "__eq__" method.
    buzz_alt = NewsletterSubscriber("Edwin Eugene Aldrin Jr.", "moonboy1969@fakemail.com")
    print(buzz == buzz_alt) # True even though they are different objects with a different name
    print(buzz is buzz_alt) # False, compares memory location of the objects.

    # under the hood, __eq__ being invoked by the 'is in' in register account
    lab_report.register_signup(buzz_alt)

    lab_report.publish('Welcome to the Lab Report!')
    pupdate.publish('Breaking News: local dog is very cute.')

    # Micro-exercise: the following is generally considered a bad idea.
    # Take a couple minutes and try to explain why, then consider the
    # subsequent lines of code and their behavior
    lab_report.mailing_list.append(buzz_alt)

    # Subsequent lines:
    lab_report.unsubscribe(buzz_alt)
    lab_report.publish("Programming is neat!")


# __name__ will be main if we ran this file like a script, it will be 
# something else if this file was imported by another file.
if __name__ == '__main__':
    main()