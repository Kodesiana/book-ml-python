const path = require('path');
const express = require('express');
const mustacheExpress = require('mustache-express');
const bodyParser = require('body-parser');
const axios = require('axios').default;
const FormData = require('form-data');
const multer  = require('multer');

// --- Multer upload
const storage = multer.memoryStorage();
const upload = multer({ storage: storage });

// --- Create app
const app = express();

// --- Middlewares
app.use(bodyParser.urlencoded({extended : true}));
app.use('/static', express.static(path.join(__dirname, 'static')));
app.set('views', `${__dirname}/views`);
app.set('view engine', 'mustache');
app.engine('mustache', mustacheExpress());

// --- Routes
app.get('/', (req, res) => {
    res.render('home');
});

app.post('/predict-house', upload.none(), async (req, res) => {
    const body = new FormData();
    body.append("rm", req.body.ruangan);

    const result = await axios.post('http://localhost:3001/predict', body, {
        headers: body.getHeaders()
    });

    res.render('hasil', {
        hasil: result.data.predicted,
        hasImg: false
    });
});

app.post('/predict-animals', upload.single('file'), async (req, res) => {
    if (!req.file) {
        res.render('hasil', {hasil: 'Gambar belum dipilih', hasImg: false});
        return;
    }

    const body = new FormData();
    body.append("file", Buffer.from(req.file.buffer), {filename: req.file.originalname});

    const result = await axios.post('http://localhost:3002/predict', body, {
        headers: body.getHeaders()
    });

    res.render('hasil', {
        hasil: result.data.predicted,
        hasImg: true,
        img: "data:image/jpg;base64," + Buffer.from(req.file.buffer).toString('base64')
    });
});

// --- Bootstrap
const port = 5000;
app.listen(port, () => {
    console.log(`Server started at http://localhost:${port}`);
});