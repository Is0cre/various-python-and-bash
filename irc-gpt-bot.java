import org.jibble.pircbot.*;
import ai.openai.completion.Completion;
import ai.openai.completion.Engine;
import ai.openai.completion.OpenAIApi;

public class GPTBot extends PircBot {
    private String channel;
    private String gptApiKey;

    public GPTBot(String channel, String nickname, String server, String gptApiKey) {
        this.setName(nickname);
        this.channel = channel;
        this.gptApiKey = gptApiKey;
        OpenAIApi.apiKey = gptApiKey;
        this.setVerbose(true);
        this.setAutoNickChange(true);
    }

    @Override
    protected void onConnect() {
        joinChannel(channel);
    }

    @Override
    protected void onMessage(String channel, String sender, String login, String hostname, String message) {
        if (message.startsWith(getNick() + ":")) {
            String question = message.substring(getNick().length() + 1).trim();
            String response = generateResponse(question);
            sendMessage(channel, response);
        }
    }

    private String generateResponse(String question) {
        try {
            Completion completion = Completion.create(
                    Engine.TEXT_DAVINCI_003,
                    question,
                    50,
                    1,
                    null,
                    0.7,
                    null,
                    null
            );
            return completion.choices.get(0).text.trim();
        } catch (Exception e) {
            e.printStackTrace();
            return "I'm sorry, but I'm currently unable to generate a response.";
        }
    }

    public static void main(String[] args) {
        String channel = "#YOUR_CHANNEL";
        String nickname = "YOUR_NICKNAME";
        String server = "YOUR_IRC_SERVER";
        String gptApiKey = "YOUR_GPT_API_KEY";

        GPTBot bot = new GPTBot(channel, nickname, server, gptApiKey);
        try {
            bot.connect(server);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
