import sys
import os
sys.path.append('../../software/models/')
from utilFunctions import wavread, wavwrite
from scipy.io.wavfile import write
from A1Part3 import hopSamples
import copy

"""
A1-Part-4: Downsampling audio: Changing the sampling rate

One of the required processes to represent a signal inside a computer is sampling. The sampling rate is the number of samples obtained in one second when sampling a continuous analog signal to a discrete digital signal. As mentioned earlier, most of the time we will be working with wav audio files that have a sampling rate of 44100 Hz, which is a typical value. For some applications, changing the sampling rate of an audio signal can be necessary. This optional part shows how to do this, from a higher sampling rate to a lower one.

Complete the function downsampleAudio(inputFile,M) in the file A1Part4.py so that given an audio file, it applies downsampling by a factor of M and create a wav audio file <input_name>_downsampled.wav at a lower sampling rate.

In Part1 you learned how to read a wav file and the function from Part3 can be used to perform the downsampling of a signal contained in an array. To create a wav audio file from an array, you can use the wavwrite function from the utilFunctions module. Be careful with the sampling rate parameter since it should be different from that of the original audio.

You can test your code using the file `vibraphone-C6.wav' and a downsampling factor of M=16. 
Listen to the `vibraphone-C6_downsampled.wav' sound. What happened to the signal?
How could we avoid damaging the signal when downsampling it?
You can find some related information in https://en.wikipedia.org/wiki/Decimation_%28signal_processing%29.
"""

INT16_FAC = (2**15)-1
INT32_FAC = (2**31)-1
INT64_FAC = (2**63)-1
norm_fact = {'int16':INT16_FAC, 'int32':INT32_FAC, 'int64':INT64_FAC,'float32':1.0,'float64':1.0}


def downsampleAudio(inputFile, M):
    """
    Inputs:
        inputFile: file name of the wav file (including path)
        	M: downsampling factor (positive integer)
    """
    ## Your code here
    if (M == 1):
        raise ValueError('M must larger than 1')
    
    fs, x = wavread(inputFile)
    
    out = copy.deepcopy(x)   # deep copy the array
    write('vibraphone-C6_downsampled.wav', float(fs/M), out)
