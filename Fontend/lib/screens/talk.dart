import 'package:avatar_glow/avatar_glow.dart';
import 'package:flutter/material.dart';
import 'package:lottie/lottie.dart';
import 'package:speech_to_text/speech_to_text.dart' as stt;

class Talk extends StatefulWidget {
  const Talk({super.key});

  @override
  State<Talk> createState() => _TalkState();
}

class _TalkState extends State<Talk> {
  stt.SpeechToText _speech = stt.SpeechToText();
  bool _isListening = false;
  String _text = '';
  double _confidence = 1.0;

  @override
  void initState() {
    super.initState();
    _speech = stt.SpeechToText();
    _initializeSpeech();
  }

  void _initializeSpeech() async {
    bool available = await _speech.initialize(
      onStatus: _onSpeechStatus,
      onError: (val) => print('onError: $val'),
    );
    if (!available) {
      setState(() => _text = 'Speech recognition not available');
    }
  }

  void _onSpeechStatus(String status) {
    setState(() {
      _isListening = status == 'listening';
    });
  }

  void listen() async {
    if (!_isListening) {
      bool available = await _speech.initialize(
        onStatus: _onSpeechStatus,
        onError: (val) => print('onError: $val'),
      );
      if (available) {
        setState(() => _isListening = true);
        _speech.listen(
          listenFor: const Duration(seconds: 30),
          pauseFor: const Duration(seconds: 5),
          onResult: (val) => setState(() {
            _text = val.recognizedWords;
            if (val.hasConfidenceRating && val.confidence > 0) {
              _confidence = val.confidence;
            }
          }),
        );
      }
    } else {
      _speech.stop();
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 15, vertical: 10),
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(20),
                    color: Colors.lightGreenAccent,
                  ),
                  child: const Text(
                    "Morgan",
                    style: TextStyle(
                      fontSize: 15,
                      fontWeight: FontWeight.bold,
                      color: Colors.black,
                    ),
                  ),
                ),
                const SizedBox(height: 10),
                const Text(
                  "Online",
                  style: TextStyle(fontSize: 12),
                ),
              ],
            ),
            Lottie.asset(
              "assets/animations/Animation - 1711215962765.json",
              width: 300,
            ),
            Container(
              width: double.maxFinite,
              height: 150,
              margin: const EdgeInsets.symmetric(horizontal: 20),
              decoration: BoxDecoration(
                border: Border.all(),
              ),
              child: Center(
                child: Text(
                  _text,
                  style: const TextStyle(
                    color: Colors.black,
                    fontWeight: FontWeight.w400,
                  ),
                  textAlign: TextAlign.center,
                ),
              ),
            ),
            InkWell(
              onTap: listen,
              child: AvatarGlow(
                animate: _isListening,
                glowColor: Theme.of(context).primaryColor,
                duration: const Duration(milliseconds: 2000),
                repeat: true,
                child: Container(
                  width: 80,
                  height: 80,
                  decoration: const BoxDecoration(
                    shape: BoxShape.circle,
                    color: Colors.lightGreenAccent,
                  ),
                  child: Icon(_isListening ? Icons.mic : Icons.mic_none),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
