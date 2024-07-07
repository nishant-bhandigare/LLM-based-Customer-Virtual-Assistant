import 'package:avatar_glow/avatar_glow.dart';
import 'package:flutter/material.dart';
import 'package:lottie/lottie.dart';
import 'package:speech_to_text/speech_to_text.dart' as stt;
import 'package:flutter_tts/flutter_tts.dart';

class Talk extends StatefulWidget {
  const Talk({super.key});

  @override
  State<Talk> createState() => _TalkState();
}

class _TalkState extends State<Talk> {
  late stt.SpeechToText _speechToText;
  late FlutterTts _textToSpeech;
  bool _isListening = false;
  String _text = '';
  double _confidence = 1.0;
  List<Map<String, String>> _voices = [];
  Map<String, String>? _currentVoice;

  @override
  void initState() {
    super.initState();
    _initializeSpeechToText();
    _initializeTextToSpeech();
  }

  void _initializeSpeechToText() {
    _speechToText = stt.SpeechToText();
    _speechToText.initialize(
      onStatus: _onSpeechStatus,
      onError: (val) => print('Speech Recognition Error: $val'),
    );
  }

  void _initializeTextToSpeech() async {
    _textToSpeech = FlutterTts();
    _textToSpeech.setVoice({"name": "Karen", "locale": "en-AU"});
    var voices = await _textToSpeech.getVoices;
    if (voices != null && voices.isNotEmpty) {
      setState(() {
        _voices = List<Map<String, String>>.from(voices)
            .where((voice) => voice["name"]?.contains("en") ?? false)
            .toList();
        if (_voices.isNotEmpty) {
          _currentVoice = _voices.first;
          _setVoice(_currentVoice!);
        }
      });
    }
  }

  void _setVoice(Map<String, String> voice) {
    _textToSpeech.setVoice(voice);
  }

  void _onSpeechStatus(String status) {
    if (status == 'notListening' && _isListening) {
      setState(() {
        _isListening = false;
      });
      _speak();
    }
  }

  void _speak() async {
    if (_currentVoice != null) {
      _textToSpeech.setVoice(_currentVoice!);
    }
    await _textToSpeech.speak(_text);
  }

  void _listen() async {
    if (!_isListening) {
      bool available = await _speechToText.initialize(
        onStatus: _onSpeechStatus,
        onError: (val) => print('Speech Recognition Error: $val'),
      );
      if (available) {
        setState(() => _isListening = true);
        _speechToText.listen(
          listenFor: const Duration(seconds: 30),
          pauseFor: const Duration(seconds: 5),
          onResult: (val) {
            setState(() {
              _text = val.recognizedWords;
              if (val.hasConfidenceRating && val.confidence > 0) {
                _confidence = val.confidence;
              }
            });
          },
        );
      }
    } else {
      _speechToText.stop();
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
            _buildHeader(),
            _buildAnimation(),
            _buildTextDisplay(),
            _buildMicButton(),
          ],
        ),
      ),
    );
  }

  Widget _buildHeader() {
    return Column(
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
    );
  }

  Widget _buildAnimation() {
    return Lottie.asset(
      "assets/animations/Animation - 1711215962765.json",
      width: 300,
    );
  }

  Widget _buildTextDisplay() {
    return Container(
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
    );
  }

  Widget _buildMicButton() {
    return InkWell(
      onTap: _listen,
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
    );
  }
}
