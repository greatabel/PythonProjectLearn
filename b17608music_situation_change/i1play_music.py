import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file('data/1q.wav')
# load the file

# wave_obj = sa.WaveObject.from_wave_file("alarm.wav")
play_obj = wave_obj.play()
#play_obj.wait_done() #blocking call
while True:
    if(play_obj.is_playing()):
        print('Playing')
    else:
        print('Ended')
        break