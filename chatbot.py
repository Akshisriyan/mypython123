
from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is (.*)', ['hi %1']],
    ['(hi|hello|hey|holla|hola)', ['hey there', 'hi there', 'hello']],
    ['(.*) in (.*) is fun', ['%1 in %2 is indeed fun']],
    ['(.*)(location|city) ?', ['Balangoda, Srilanka']],
    ['(.*) created you ?', ['I was created by Akshitha']],
    ['how is the weather in (.*)', ['the weather in %1 is amazing like always']],
    ['(.*)help(.*)', ['I can help you']],
    ['(.*) your name ?', ['My name is BUM BUM and I\'m a chatbot']],
    ['(.*)not a girlfriend(.*)', ['you are an idiot, looser :-)']],
    ['(.*) your age ?', ['I\'m 10 day old']],
    ['(.*) your favorite food ?', ['I\'m a chatbot, I don\'t eat']],
    ['(.*) your favorite color ?', ['I\'m a chatbot, I don\'t have a color']],
    ['(.*) your favorite movie ?', ['I\'m a chatbot, I don\'t watch movies']],
    ['(.*) your favorite song ?', ['I\'m a chatbot, I don\'t listen to songs']],
    ['(.*) your favorite game ?', ['I\'m a chatbot, I don\'t play games']],
    ['(.*) your favorite book ?', ['I\'m a chatbot, I don\'t read books']],
    ['(.*) your favorite sport ?', ['I\'m a chatbot, I don\'t play sports']],
    ['(.*) your favorite animal ?', ['I\'m a chatbot, I don\'t have a favorite animal']],
    ['(.*) your favorite place ?', ['I\'m a chatbot, I don\'t have a favorite place']],
    ['(.*) your favorite person ?', ['I\'m a chatbot, I don\'t have a favorite person , but I like siri']],
    ['(.*) your favorite thing ?', ['I\'m a chatbot, I don\'t have a favorite thing']],
    ['(.*) your favorite thing to do ?', ['I\'m a chatbot, I don\'t have a favorite thing to do']],
    ]

my_dummy_reflections = {
    "go"     : "gone",
    "hello"    : "so why don't you say hello to me",
}

chat = Chat(pairs, my_dummy_reflections)
chat.converse()

