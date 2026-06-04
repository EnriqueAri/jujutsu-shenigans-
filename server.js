const { WebSocketServer } = require('ws');

// Railway automatically injects the PORT environment variable
const port = process.env.PORT || 8080;
const wss = new WebSocketServer({ port });

console.log(`Jujutsu Server is expanding its domain on port ${port}`);

// Keep track of connected players
let players = new Map();

wss.on('connection', (ws) => {
    console.log('A sorcerer has entered the arena!');

    ws.on('message', (message) => {
        try {
            const data = JSON.parse(message);
            
            // Broadcast player movement/attacks to everyone else
            const broadcastData = JSON.stringify(data);
            wss.clients.forEach((client) => {
                if (client !== ws && client.readyState === 1) {
                    client.send(broadcastData);
                }
            });
        } catch (err) {
            console.error('Error handling message:', err);
        }
    });

    ws.on('close', () => {
        console.log('A sorcerer has left the arena.');
    });
});
