import irc.bot
import irc.strings
from irc.client import irc_lower
import openai

class GPTBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.channel = channel

        # Initialize OpenAI GPT
        self.gpt_api_key = 'YOUR_GPT_API_KEY'
        openai.api_key = self.gpt_api_key

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        c.join(self.channel)

    def on_privmsg(self, c, e):
        self.respond(c, e)

    def on_pubmsg(self, c, e):
        self.respond(c, e)

    def respond(self, c, e):
        message = e.arguments[0]
        if message.startswith(self.connection.get_nickname() + ":"):
            question = message.split(":", 1)[1].strip()
            response = self.generate_response(question)
            c.privmsg(e.target, response)

    def generate_response(self, question):
        try:
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=question,
                max_tokens=50,
                n=1,
                stop=None,
                temperature=0.7
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print("Error:", str(e))
            return "I'm sorry, but I'm currently unable to generate a response."

if __name__ == "__main__":
    channel = "#YOUR_CHANNEL"
    nickname = "YOUR_NICKNAME"
    server = "YOUR_IRC_SERVER"

    bot = GPTBot(channel, nickname, server)
    bot.start()
