# License Plate Recognition
## How it works
- Open [local host](localhost:5000) index page.
- Upload your file in browser 
- Click recognition button
![example](./doc/detected_bbox.png?raw=true)
## Heroku
- Since Heroku free version use up to 500MB size, you should carefully chose your depenencies. Thus we are using tensorflow-cpu which is 180 MB
- Booting time takes up to 50 seconds because of downloading  CNN weights from dropbox server.If the heroku server goes to sleeping mode, this will cause temporary hanging on server.
![example](./doc/detected_alert.png?raw=true)
- In free heroku servers detection is up top 20 seconds.
- In free heroku servers booting is up top 50 seconds.
