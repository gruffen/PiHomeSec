const express = require('express');
const cors = require('cors');

const app = express();

app.use(cors())

app.get('/', (req, res, next) => {
  res.send('hello world! Testing, testing 1,2,3!');
});

app.post('/pi', (req, res, next) => {
  console.log(req, res)
});

app.listen(1337, () => {
  console.log('listening on port 3000!');
});

///testing out canvas

const { createCanvas, loadImage } = require('canvas')
const canvas = createCanvas(200, 200)
const ctx = canvas.getContext('2d')

ctx.font = '30px Impact'
ctx.rotate(0.1)
ctx.fillText('Security Images', 50, 100)

var text = ctx.measureText('Security Images')
ctx.strokeStyle = 'rgba(0,0,0,0,5)'
ctx.beginPath()
ctx.lineTo(50, 102)
ctx.lineTo(50 + text.width, 102)
ctx.stroke()

//load example picture of security cam - test
loadImage('https://imgur.com/VDTnPg6').then((image) => {
  ctx.drawImage(image, 50, 0, 70, 70)

  console.log('<img src="' + canvas.toDataURL() + '" />')
})


