import wave
from pyaudio import PyAudio,paInt16

# 录制的音频质量参数
framerate=16000
NUM_SAMPLES=2000
channels=1
sampwidth=2
TIME=16   #单位为s，实际录音时间会缩小两倍

# 录音函数
def save_wave_file(param, my_buf):
    pass


def start():
    pa=PyAudio()
    stream=pa.open(format = paInt16,channels=1,
                   rate=framerate,input=True,
                   frames_per_buffer=NUM_SAMPLES)
    my_buf=[]
    count=0
    while count<TIME:
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)
        count+=1
        print('.')
    save_wave_file('music/yinpin.wav',my_buf)
    stream.close()
    return my_buf
