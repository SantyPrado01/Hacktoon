
require('@tensorflow/tfjs');
const toxicity = require('@tensorflow-models/toxicity');
const express = require('express')
const bodyParser = require('body-parser')

const app = express();
app.use(bodyParser.json())

app.get('/health', (req, res) => {
  res.json({ msje: "Im alive" })
})

app.post('/comment', async (req, res) => {

  const { body } = req;

  const threshold = 0.9;
  try {
    const model = await toxicity.load(threshold);

    const sentences = [body.comment];

    let result = [];
    const predictions = await model.classify(sentences);

    for (let i = 0; i < predictions.length; i++) {
      const label = predictions[i].label
      const predictionsrResult = predictions[i].results[0].match

      if (predictions[i].results[0].match === true) {
        result.push({ label, predictionsrResult });
      }
    }

    return res.status(201).json(result);
  } catch (error) {
    return res.status(500).json(error);
  }
});

app.listen(3000, () => console.log('running on port 3000'))