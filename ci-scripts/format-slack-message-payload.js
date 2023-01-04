import { writeFileSync } from 'fs';

// take arguments for the message payload
const args = process.argv.slice(2);
const [message, icon_emoji] = args;

// format the message payload
const payload = {
    text: message,
    type: 'mrkdwn',
    icon_emoji: icon_emoji,
};

writeFileSync('slack-message.json', JSON.stringify(payload));
