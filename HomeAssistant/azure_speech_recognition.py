import azure.cognitiveservices.speech as speechsdk
from PySide6 import QtGui, QtCore, QtWidgets

def recognize_from_microphone(mainWindow):
    # print("ekhane")
    res = ""
    speech_config = speechsdk.SpeechConfig(subscription="db18e008ef87484896e9c241f73bc7de", region="eastus")
    speech_config.speech_recognition_language="en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        res = speech_recognition_result.text

        mainWindow.label.setText('You said: ' + res)
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        mainWindow.label.setText("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        mainWindow.label.setText("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            mainWindow.label.setText("Error details: {}".format(cancellation_details.error_details))
            mainWindow.label.setText("Did you set the speech resource key and region values?")
    
    return res