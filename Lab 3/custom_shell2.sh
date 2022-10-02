espeak -ven+f2 -k5 -s150 --stdout  "How many siblings you have" | aplay
arecord -D hw:2,0 -f cd -c1 -r 16000 -d 5 -t wav recorded_mono.wav
python3 test_words.py recorded_mono.wav