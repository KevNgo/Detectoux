#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 15:28:23 2021

@author: vincenttran
"""
import librosa
import numpy as np

#Def function to preprocess signal in js
def signalPreprocess(audio):
    data,sr=librosa.load(audio, res_type='kaiser_fast',duration=1,mono=True)
    data_fft=np.fft.fft(data)
    
    #magnitude spectrum operations
    magnitude_spectrum=np.abs(data_fft)
    maxmagspec=magnitude_spectrum.max()
    maxfreqmagspec=np.argmax(magnitude_spectrum)
    meanmagspec=magnitude_spectrum.mean()
    
    #raw signal operation
    maxfreqreg=np.argmax(data)
    
    #fft signal operation
    maxfreqfft=np.argmax(data_fft)
    
    #calcul du mfcc moyen sur 128 tronçons
    mfccs=np.mean(librosa.feature.mfcc(y=data,sr=sr,n_mfcc=128).T,axis=0)
    
    maxmfcc=max(mfccs)
    stdmfcc=np.std(mfccs)
    
    return maxmfcc, stdmfcc, maxmagspec, meanmagspec, maxfreqmagspec, maxfreqreg, maxfreqfft
