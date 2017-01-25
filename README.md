# max7219
python scripts for the max7219 LED Matrix board

## matrix_scroll.py
Scrolls a message on the LED board
* Run the script using `./matrix_scroll.py` followed by -m and the message in quotes and -r with the number of times to repeat the message
0 scrolls the message until the script is exited.

## nye_countdown.py
Scrolls a countdown to midnight on New Years Eve on the LED board
* Run the script using `./nye_countdown.py`

## time_scroll.py
Scrolls the current time on the LED board
* Run the script using `./time_scroll.py`

## max7219_pixel_art.py
Runs the zeroMQ server to listen for input from the pixel.py web page

1.  run the script `nohup ./max7219_pixel_art.py`

2.  Open a web browser to `<ip address>/pixel.py`

example: The code for a minecraft sword is `3,7,14,220,120,48,88,136`

## max7219_server.py
Runs the zeroMQ server to listen for input from the msg.py web page

1. run the script `nohup ./max7219_server.py`

2. Open a web browser to `<ip address>/msg.py`

