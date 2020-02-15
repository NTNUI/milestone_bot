import slack

from settings import SLACK_API_TOKEN

client = slack.WebClient(token=SLACK_API_TOKEN)


def run():
    print(SLACK_API_TOKEN)
    client.channels_list()
    client.chat_postMessage(
      channel="CU3SUNN3H",
      text="Hello from your app! :tada:"
    )


if __name__ == '__main__':
    run()
