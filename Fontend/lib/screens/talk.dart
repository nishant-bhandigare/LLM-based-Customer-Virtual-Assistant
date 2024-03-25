import 'package:flutter/material.dart';
import 'package:lottie/lottie.dart';

class TalkPage extends StatelessWidget {
  const TalkPage({super.key});
  @override
  Widget build(BuildContext context) {
    return(Scaffold(
      body: Column(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          const SizedBox(height: 5,),
          Column(
            children: [
              Container(
                padding: const EdgeInsets.all(10),
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(20),
                  // border: Border.all(color: Colors.black),
                  color: Colors.lightGreenAccent,
                ),
                child: const Text(
                  "AI Buddy",
                  style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Colors.black),
                ),
              ),
              const SizedBox(
                height: 10,
              ),
              const Text(
                "Online",
                style: TextStyle(fontSize: 12,),
              ),
            ],
          ),
          Container(
            child: Lottie.asset("assets/animations/Animation - 1711215962765.json", width: 300),
          ),
          Container(
            width: double.infinity,
            height: 150,
            padding: EdgeInsets.all(12),
            // color: Colors.cyanAccent,
            decoration: BoxDecoration(
              // border: Border.all(color: Colors.white),
            ),
            child: const Center(
              child: Text(
                "What are the top trending interface design tools in 2023", style: TextStyle(color: Colors.white, fontSize: 25),
                textAlign: TextAlign.center,
              ),
            ),
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              CircleAvatar(
                radius: 20,
                backgroundColor: Colors.deepPurple,
                child: Image.asset("assets/icons/keyboard.png", width: 20,),
              ),
              CircleAvatar(
                radius: 40,
                backgroundColor: Colors.lightGreenAccent,
                child: Image.asset("assets/icons/mic.png", width: 40,),
              ),
              CircleAvatar(
                radius: 20,
                backgroundColor: Colors.grey,
                child: Image.asset("assets/icons/wrong.png", width: 10,),
              ),
            ],
          ),
        ],
      ),
    ));
  }
}