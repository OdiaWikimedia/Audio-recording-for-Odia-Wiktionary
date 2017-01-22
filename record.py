import pyaudio
import wave
import sys


def record_audio(filename):

	chunk = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 1
	RATE = 44100
	RECORD_SECONDS = 3
	filename = filename + ".wav"
	WAVE_OUTPUT_FILENAME = filename

	p = pyaudio.PyAudio()

	stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = chunk)

	print "* recording"
	all = []
	for i in range(0, RATE / chunk * RECORD_SECONDS):
    		data = stream.read(chunk)
    		all.append(data)
	print "* Recording complete."

	stream.close()
	p.terminate()

	# write data to WAVE file
	data = ''.join(all)
	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(data)
	wf.close()
