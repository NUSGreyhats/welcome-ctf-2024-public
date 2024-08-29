const express = require('express');
const { visitUrl } = require('./admin.js');
const path = require('path');
const { lutimes } = require('fs');
const app = express();
const port = 3000;

app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.get('/feedback', async (req, res) => {
    let url = req.query.url
    console.log('received url: ', url)

    let parsedURL
    try {
        parsedURL = new URL(url)
    }
    catch (e) {
        res.send(escape(e.message))
        return
    }

    if (parsedURL.protocol !== 'http:' && parsedURL.protocol != 'https:') {
        res.send('Please provide a URL with the http or https protocol.')
        return
    }

    if (parsedURL.hostname !== req.hostname) {
        res.send(`Please provide a URL with a hostname of: ${escape(req.hostname)}, your parsed hostname was: escape(${parsedURL.hostname})`)
        return
    }

    url = "http://localhost:3000/?markdown="+url.split("/?markdown=")[1]

    try {
        console.log('visiting url: ', url)
        await visitUrl(url, 'localhost:3000')
        res.send('The admin has viewed your feedback!')
    } catch (e) {
        console.log('error visiting: ', url, ', ', e.message)
        res.send('Error, admin unable to view your feedback')
    } finally {
        console.log('done visiting url: ', url)
    }

})

app.listen(port, () => {
    console.log(`Markdown parser app listening at http://localhost:${port}`);
});
